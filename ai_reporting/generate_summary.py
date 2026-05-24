from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]

FILES = {
    "monthly": BASE_DIR / "revenue_by_month.csv",
    "products": BASE_DIR / "revenue_by_product.csv",
    "regions": BASE_DIR / "revenue_by_region.csv",
    "customers": BASE_DIR / "top_customers.csv",
    "orders": BASE_DIR / "total_order_revenue.csv",
}

OUTPUT_FILE = BASE_DIR / "ai_reporting" / "smartops_kpi_summary.md"


def format_euro(value: float) -> str:
    return f"€{value:,.2f}"


def main() -> None:
    monthly = pd.read_csv(FILES["monthly"])
    products = pd.read_csv(FILES["products"])
    regions = pd.read_csv(FILES["regions"])
    customers = pd.read_csv(FILES["customers"])
    orders = pd.read_csv(FILES["orders"])

    monthly["month"] = pd.to_datetime(monthly["month"])
    monthly["revenue"] = pd.to_numeric(monthly["revenue"])
    products["revenue"] = pd.to_numeric(products["revenue"])
    regions["revenue"] = pd.to_numeric(regions["revenue"])
    customers["revenue"] = pd.to_numeric(customers["revenue"])
    orders["total_revenue"] = pd.to_numeric(orders["total_revenue"])

    total_revenue = orders["total_revenue"].sum()
    number_of_orders = orders["order_id"].nunique()
    avg_monthly_revenue = monthly["revenue"].mean()

    best_month_row = monthly.loc[monthly["revenue"].idxmax()]
    weakest_month_row = monthly.loc[monthly["revenue"].idxmin()]

    top_product_row = products.loc[products["revenue"].idxmax()]
    top_region_row = regions.loc[regions["revenue"].idxmax()]
    top_customer_row = customers.loc[customers["revenue"].idxmax()]

    best_month = best_month_row["month"].strftime("%B %Y")
    weakest_month = weakest_month_row["month"].strftime("%B %Y")

    report = f"""# SmartOps BI – Automated KPI Insight Summary

## Executive Summary

SmartOps BI analyzes sales performance across monthly revenue, products, customers, and regions.

## Key KPIs

| KPI | Value |
|---|---:|
| Total Revenue | {format_euro(total_revenue)} |
| Number of Orders | {number_of_orders} |
| Average Monthly Revenue | {format_euro(avg_monthly_revenue)} |
| Best Revenue Month | {best_month} |
| Weakest Revenue Month | {weakest_month} |

## Business Insights

- **{top_product_row["product_name"]}** is the strongest product with **{format_euro(top_product_row["revenue"])}** in revenue.
- **{top_customer_row["customer_name"]}** is the highest-value customer with **{format_euro(top_customer_row["revenue"])}** in revenue.
- **{top_region_row["region"]}** is the strongest region with **{format_euro(top_region_row["revenue"])}** in revenue.
- **{best_month}** generated the highest monthly revenue.
- **{weakest_month}** generated the lowest monthly revenue and may require further investigation.

## Project Result

This report was generated automatically from exported PostgreSQL KPI views using Python and Pandas.
"""

    OUTPUT_FILE.write_text(report, encoding="utf-8")
    print(f"Business insight summary created: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
