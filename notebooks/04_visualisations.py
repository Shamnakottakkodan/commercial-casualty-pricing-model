# 04_visualisations.py
"""
Casualty Pricing Visualisations (Matplotlib)
Generates underwriting-style charts for portfolio insights.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load portfolio dataset
df = pd.read_csv("../data/casualty_portfolio.csv")

# Compute loss ratio
df["loss_ratio"] = df["total_claims_cost_gbp"] / df["earned_premium_gbp"]

# --------------- 1. LOSS RATIO BY INDUSTRY (BOX PLOT) ---------------- #

plt.figure(figsize=(10, 6))
df.boxplot(column="loss_ratio", by="industry", grid=False)
plt.title("Loss Ratio by Industry")
plt.suptitle("")  # remove Matplotlib default title
plt.ylabel("Loss Ratio")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../reports/loss_ratio_by_industry_matplotlib.png")
plt.close()


# --------------- 2. LOSS RATIO BY REGION (BAR CHART) ---------------- #

avg_lr_region = df.groupby("region")["loss_ratio"].mean().sort_values()

plt.figure(figsize=(10, 6))
avg_lr_region.plot(kind="bar")
plt.title("Average Loss Ratio by Region")
plt.ylabel("Average Loss Ratio")
plt.xlabel("Region")
plt.tight_layout()
plt.savefig("../reports/avg_loss_ratio_by_region.png")
plt.close()


# --------------- 3. TECHNICAL PREMIUM vs EARNED PREMIUM ---------------- #

# If technical pricing results exist, load them
try:
    tech_df = pd.read_csv("../reports/technical_pricing_results.csv")

    merged = df.merge(tech_df, on="policy_id", how="inner")

    plt.figure(figsize=(8, 6))
    plt.scatter(
        merged["earned_premium_gbp"],
        merged["technical_premium"],
        alpha=0.6
    )
    plt.plot([0, merged["earned_premium_gbp"].max()],
             [0, merged["earned_premium_gbp"].max()],
             color="red", linestyle="--")  # diagonal reference line

    plt.title("Technical Premium vs Earned Premium")
    plt.xlabel("Earned Premium (£)")
    plt.ylabel("Technical Premium (£)")
    plt.tight_layout()
    plt.savefig("../reports/tech_vs_earned_premium.png")
    plt.close()

except FileNotFoundError:
    print("⚠ technical_pricing_results.csv not found. Run 03_technical_pricing.py first.")


# --------------- 4. SEVERITY DISTRIBUTION (HISTOGRAM) ---------------- #

severity_data = df[df["total_claims_cost_gbp"] > 0]["total_claims_cost_gbp"]

plt.figure(figsize=(10, 6))
plt.hist(severity_data, bins=30, alpha=0.7)
plt.title("Distribution of Claims Severity")
plt.xlabel("Claim Size (£)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("../reports/severity_distribution.png")
plt.close()


print("✅ Visualisations created and saved in /reports")
