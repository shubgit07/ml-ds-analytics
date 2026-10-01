# E-Commerce Analytics & Delivery Prediction

End-to-end data analytics and machine learning project using the Olist Brazilian e-commerce dataset.

## Project Goals

- Analyze e-commerce orders, customers, sellers, products, payments, reviews, and delivery performance.
- Build reusable SQL and Pandas analytics workflows.
- Define business KPIs and an interactive Streamlit dashboard.
- Predict late deliveries using classical machine learning.
- Compare baseline and ensemble models with leakage-safe time-based validation.
- Interpret the final model using SHAP.

## Planned Stack

- Python
- Pandas / NumPy
- SQL
- Scikit-learn
- XGBoost
- SHAP
- Matplotlib
- Streamlit

## Repository Structure

```
data/
  raw/          # Local raw dataset; not committed
  processed/    # Generated datasets; not committed unless intentionally selected

notebooks/
  01_data_understanding.ipynb
  02_sql_analysis.ipynb
  03_eda.ipynb
  04_feature_engineering.ipynb
  05_modeling.ipynb
  06_shap_analysis.ipynb

dashboard/
src/
```

## Dataset

The project uses the Olist Brazilian E-Commerce Public Dataset. Raw data is kept outside GitHub and is not committed to the repository.

## Status

Project setup complete. Analysis and modeling will be developed incrementally.
