#!/bin/bash

set -e

echo "Exporting SmartOps BI KPI CSV files..."

docker compose exec -T db psql -U smartops -d smartops_bi -c \
"COPY (SELECT * FROM revenue_by_month) TO STDOUT WITH CSV HEADER" > revenue_by_month.csv

docker compose exec -T db psql -U smartops -d smartops_bi -c \
"COPY (SELECT * FROM revenue_by_product) TO STDOUT WITH CSV HEADER" > revenue_by_product.csv

docker compose exec -T db psql -U smartops -d smartops_bi -c \
"COPY (SELECT * FROM revenue_by_region) TO STDOUT WITH CSV HEADER" > revenue_by_region.csv

docker compose exec -T db psql -U smartops -d smartops_bi -c \
"COPY (SELECT * FROM top_customers) TO STDOUT WITH CSV HEADER" > top_customers.csv

docker compose exec -T db psql -U smartops -d smartops_bi -c \
"COPY (SELECT * FROM total_order_revenue) TO STDOUT WITH CSV HEADER" > total_order_revenue.csv

echo "Done. KPI CSV files exported successfully."
