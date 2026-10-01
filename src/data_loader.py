from pathlib import Path
import pandas as pd

ORDER_FILES = {
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "order_payments": "olist_order_payments_dataset.csv",
    "order_reviews": "olist_order_reviews_dataset.csv",
    "customers": "olist_customers_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "products": "olist_products_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "category_translation": "product_category_name_translation.csv",
}

def load_olist_data(data_dir):
    data_dir = Path(data_dir)
    return {name: pd.read_csv(data_dir / filename) for name, filename in ORDER_FILES.items()}

def convert_order_dates(orders):
    date_cols = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]
    orders = orders.copy()
    for col in date_cols:
        orders[col] = pd.to_datetime(orders[col], errors="coerce")
    return orders
