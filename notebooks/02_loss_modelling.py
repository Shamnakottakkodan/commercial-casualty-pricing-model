# 02_loss_modelling.py
"""
Frequency and Severity Modelling for Commercial Casualty Portfolio

This script demonstrates how to prepare the data and fit simple regression-style models
similar to actuarial GLMs. For simplicity, it uses basic linear models.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import PoissonRegressor, LinearRegression

df = pd.read_csv("../data/casualty_portfolio.csv")

# Create loss ratio and pure premium
df["frequency"] = df["num_claims"] / df["exposure_turnover_m"].replace({0: np.nan})
df["severity"] = df["total_claims_cost_gbp"] / df["num_claims"].replace({0: np.nan})
df["pure_premium"] = df["total_claims_cost_gbp"] / df["exposure_turnover_m"].replace({0: np.nan})

# Drop rows with undefined values
mod_df = df.dropna(subset=["frequency", "severity", "pure_premium"]).copy()

# Simple encoding of categorical variables
mod_df = pd.get_dummies(mod_df, columns=["industry", "region", "line_of_business"], drop_first=True)

features = [c for c in mod_df.columns if c not in [
    "policy_id", "policy_year", "num_claims", "total_claims_cost_gbp",
    "earned_premium_gbp", "frequency", "severity", "pure_premium"
]]

X = mod_df[features]

# Frequency model (Poisson regression)
y_freq = mod_df["num_claims"]
X_train_f, X_test_f, y_train_f, y_test_f = train_test_split(X, y_freq, test_size=0.2, random_state=42)

freq_model = PoissonRegressor(alpha=0.1, max_iter=1000)
freq_model.fit(X_train_f, y_train_f)
y_pred_f = freq_model.predict(X_test_f)
print("Frequency model RMSE:", mean_squared_error(y_test_f, y_pred_f, squared=False))

# Severity model (Linear regression on log severity)
mod_df["log_severity"] = np.log(mod_df["severity"])
y_sev = mod_df["log_severity"]
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X, y_sev, test_size=0.2, random_state=42)

sev_model = LinearRegression()
sev_model.fit(X_train_s, y_train_s)
y_pred_s = sev_model.predict(X_test_s)
print("Severity model RMSE:", mean_squared_error(y_test_s, y_pred_s, squared=False))

# Save simple model coefficients summary
coef_summary = {
    "frequency_model": dict(zip(features, freq_model.coef_)),
    "severity_model": dict(zip(features, sev_model.coef_)),
}
with open("../reports/model_coefficients.json", "w") as f:
    json.dump(coef_summary, f, indent=2)

print("\nModel coefficients saved to ../reports/model_coefficients.json")
