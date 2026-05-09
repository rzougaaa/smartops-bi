import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

# Customers
customers = pd.DataFrame({
    "customer_id": [1,2,3,4,5,6,7,8],
    "customer_name": ["Alpha Retail","Beta Supplies","City Market","Delta Stores","Euro Trade","Fresh Foods","Global Mart","Home Essentials"],
    "region": ["North","South","West","East","North","South","West","East"],
    "signup_date": ["2024-01-10","2024-01-15","2024-02-01","2024-02-12","2024-03-05","2024-03-18","2024-04-02","2024-04-20"]
})
customers.to_csv("data/raw/customers.csv", index=False)

# Products
products = pd.DataFrame({
    "product_id":[101,102,103,104,105,106],
    "product_name":["Laptop Stand","Wireless Mouse","Office Chair","Standing Desk","USB-C Hub","Monitor 24 Inch"],
    "category":["Accessories","Accessories","Furniture","Furniture","Electronics","Electronics"],
    "unit_price":[29.99,19.99,149.99,399.99,39.99,179.99]
})
products.to_csv("data/raw/products.csv", index=False)

# Orders
orders = pd.DataFrame({
    "order_id":[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
    "customer_id":[1,2,3,4,5,6,7,8,1,3],
    "order_date":["2024-04-01","2024-04-03","2024-04-05","2024-04-08","2024-04-10","2024-04-12","2024-04-15","2024-04-18","2024-04-21","2024-04-25"],
    "status":["completed","completed","completed","cancelled","completed","completed","completed","pending","completed","completed"]
})
orders.to_csv("data/raw/orders.csv", index=False)

# Order Items
order_items = pd.DataFrame({
    "order_item_id":[1,2,3,4,5,6,7,8,9,10,11,12,13],
    "order_id":[1001,1001,1002,1003,1004,1005,1006,1007,1007,1008,1009,1010,1010],
    "product_id":[101,102,103,105,104,106,102,101,105,103,104,106,102],
    "quantity":[2,1,1,3,1,2,4,1,2,1,1,1,2]
})
order_items.to_csv("data/raw/order_items.csv", index=False)

print("Sample CSVs generated in data/raw/")
