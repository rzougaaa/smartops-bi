import pandas as pd
import psycopg2
from psycopg2.extras import execute_values


DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 5433,
    "database": "smartops_bi",
    "user": "smartops",
    "password": "smartops",
}


def load_dataframe(conn, df, table_name, columns):
    df = df[columns].astype(object)
    values = [tuple(row) for row in df.where(pd.notnull(df), None).values.tolist()]

    query = f"""
        INSERT INTO {table_name} ({", ".join(columns)})
        VALUES %s
        ON CONFLICT DO NOTHING;
    """

    with conn.cursor() as cur:
        execute_values(cur, query, values)


def main():
    conn = psycopg2.connect(**DB_CONFIG)

    customers = pd.read_csv("data/processed/customers_clean.csv")
    products = pd.read_csv("data/processed/products_clean.csv")
    orders = pd.read_csv("data/processed/orders_clean.csv")
    order_items = pd.read_csv("data/processed/order_items_clean.csv")

    load_dataframe(
        conn,
        customers,
        "customers",
        ["customer_id", "customer_name", "region", "signup_date"],
    )

    load_dataframe(
        conn,
        products,
        "products",
        ["product_id", "product_name", "category", "unit_price"],
    )

    load_dataframe(
        conn,
        orders,
        "orders",
        ["order_id", "customer_id", "order_date", "status"],
    )

    load_dataframe(
        conn,
        order_items,
        "order_items",
        ["order_item_id", "order_id", "product_id", "quantity"],
    )

    conn.commit()
    conn.close()

    print("Processed CSV data loaded into PostgreSQL successfully.")


if __name__ == "__main__":
    main()
