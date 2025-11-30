Commercial Casualty Pricing Model, 
a practical actuarial analytics project applying statistical modelling, underwriting insights, and technical pricing techniques used in commercial insurance.

🌟 Overview

This project simulates the workflow of a Commercial Casualty Pricing Analyst, combining actuarial thinking with modern data science tools.
It was built to demonstrate how portfolio-level insights, statistical modelling, and case pricing come together to support underwriting decisions in real-world insurance environments.

The analysis includes:

📊 Portfolio profitability analysis

🔢 Frequency & severity modelling (GLM-style approach)

💰 Technical premium calculation

📝 Case pricing for a large/complex multi-location risk

📈 Power BI dashboard for underwriting insights

This project reflects the type of work done in Casualty Pricing teams and showcases end-to-end analytical thinking.

🎯 Project Objectives

Understand key drivers of loss cost across industries, regions, and exposure bases

Build interpretable frequency and severity models using statistical techniques

Derive technical prices using actuarial loadings for expenses, risk, and profit

Compare technical premium vs written premium to assess adequacy

Produce a clear, structured case pricing report for underwriter decision support

🛠️ Tools & Technologies

Python: Pandas, NumPy, scikit-learn

SQL: Data extraction & preparation

Power BI: Interactive dashboards for decision-making

Jupyter / Scripts: For portfolio analysis & modelling

Markdown: For structured case pricing reports



📊 1. Portfolio Analysis

The portfolio dataset contains:

Policy-level exposures

Industry and regional attributes

Limits & deductibles

Earned premium

Historical claim frequency and severity

Analysis includes:

Loss ratio trends

Risk heatmaps

Industry and regional segmentation

Outlier and concentration checks

This mirrors the portfolio strategy work done alongside underwriters to understand portfolio performance.




🔢 2. Frequency & Severity Modelling

Using simplified GLM-style techniques, two core models are built:

Frequency Model

Predicts expected claim counts using Poisson regression.

Severity Model

Predicts average claim cost using log-linear regression.

The models incorporate:

Industry relativities

Regional variation

Exposure measures

Policy terms (limits, deductibles)

Outputs contribute to the expected loss cost calculation.



💰 3. Technical Premium Framework

A standard actuarial pricing structure is applied:

Technical Premium
= (Expected Loss Cost × Risk Load)
  ÷ (1 − Expense Ratio − Profit Margin)


The project compares:

Technical premium
vs

Current earned/written premium

and produces premium adequacy indicators for each policy.




📝 4. Case Pricing (Large Account Example)

A realistic multi-location corporate account is priced separately to demonstrate case pricing, including:

Exposure review

Risk assessment

Model-based expected loss cost

Technical premium indication

Clear recommendation for underwriting

This process aligns closely with how pricing analysts support underwriters on complex or bespoke risks.


📈 5. Power BI Dashboard 

A dashboard can be added to visualise:

Loss ratio distribution

Frequency & severity patterns

Adequacy by region or industry

Technical vs written premium

Drill-through pages for case pricing

This demonstrates strong communication skills and ability to translate analytics into meaningful insights.
