# 01_portfolio_analysis.py
"""
Portfolio Analysis for Commercial Casualty Pricing

This script performs exploratory data analysis on the casualty_portfolio.csv dataset.
You can convert it into a Jupyter Notebook if preferred.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("../data/casualty_portfolio.csv")

print("Shape:", df.shape)
print(df.head())

# Basic summaries
print(df.describe())

# Loss ratio
df["loss_ratio"] = df["total_claims_cost_gbp"] / df["earned_premium_gbp"]

print("\nLoss ratio summary:")
print(df["loss_ratio"].describe())

# Example: boxplot of loss ratio by industry
plt.figure()
df.boxplot(column="loss_ratio", by="industry", rot=45)
plt.tight_layout()
plt.savefig("../reports/loss_ratio_by_industry.png")

# Example: average loss ratio by region
avg_lr_region = df.groupby("region")["loss_ratio"].mean().reset_index()
print("\nAverage loss ratio by region:")
print(avg_lr_region)
