# 03_technical_pricing.py
"""
Technical Pricing Framework for Commercial Casualty

This script uses model outputs to approximate a technical premium and compare it to actual written premium.
"""

import pandas as pd
import numpy as np
import json

from sklearn.linear_model import PoissonRegressor, LinearRegression

# Load data
df = pd.read_csv("../data/casualty_portfolio.csv")

# Derived metrics
df["frequency"] = df["num_claims"] / df["exposure_turnover_m"].replace({0: np.nan})
df["severity"] = df["total_claims_cost_gbp"] / df["num_claims"].replace({0: np.nan})
df["pure_premium"] = df["total_claims_cost_gbp"] / df["exposure_turnover_m"].replace({0: np.nan})

mod_df = df.dropna(subset=["frequency", "severity", "pure_premium"]).copy()
mod_df = pd.get_dummies(mod_df, columns=["industry", "region", "line_of_business"], drop_first=True)

features = [c for c in mod_df.columns if c not in [
    "policy_id", "policy_year", "num_claims", "total_claims_cost_gbp",
    "earned_premium_gbp", "frequency", "severity", "pure_premium"
]]
X = mod_df[features]

# Train frequency and severity models in this script for simplicity
y_freq = mod_df["num_claims"]
freq_model = PoissonRegressor(alpha=0.1, max_iter=1000)
freq_model.fit(X, y_freq)

mod_df["log_severity"] = np.log(mod_df["severity"])
y_sev = mod_df["log_severity"]
sev_model = LinearRegression()
sev_model.fit(X, y_sev)

# Predict expected frequency and severity
mod_df["pred_freq"] = freq_model.predict(X)
mod_df["pred_severity"] = np.exp(sev_model.predict(X))

# Expected loss cost per policy
mod_df["expected_loss_cost"] = mod_df["pred_freq"] * mod_df["pred_severity"]

# Simple expense & profit loadings
expense_ratio = 0.25
profit_margin = 0.05
risk_load = 1.10

mod_df["technical_premium"] = (
    mod_df["expected_loss_cost"] * risk_load / (1 - expense_ratio - profit_margin)
)

# Compare to current earned premium
mod_df["premium_adequacy"] = mod_df["earned_premium_gbp"] / mod_df["technical_premium"]

summary = mod_df[["technical_premium", "earned_premium_gbp", "premium_adequacy"]].describe()
print(summary)

# Save results
output_cols = ["policy_id", "technical_premium", "earned_premium_gbp", "premium_adequacy"]
mod_df[output_cols].to_csv("../reports/technical_pricing_results.csv", index=False)
print("\nTechnical pricing results saved to ../reports/technical_pricing_results.csv")
