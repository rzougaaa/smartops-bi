import pandas as pd
import os

# Ensure processed folder exists
os.makedirs("data/processed", exist_ok=True)

# --- Customers ---
customers = pd.read_csv("data/raw/customers.csv")
customers['customer_name'] = customers['customer_name'].str.strip()
customers['region'] = customers['region'].str.upper()
customers.to_csv("data/processed/customers_clean.csv", index=False)
print("Customers cleaned.")

# --- Products ---
products = pd.read_csv("data/raw/products.csv")
products['product_name'] = products['product_name'].str.strip()
products.to_csv("data/processed/products_clean.csv", index=False)
print("Products cleaned.")

# --- Orders ---
orders = pd.read_csv("data/raw/orders.csv")
orders['status'] = orders['status'].str.lower()
orders.to_csv("data/processed/orders_clean.csv", index=False)
print("Orders cleaned.")

# --- Order Items ---
order_items = pd.read_csv("data/raw/order_items.csv")
order_items.to_csv("data/processed/order_items_clean.csv", index=False)
print("Order items cleaned.")
