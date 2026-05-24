#!/bin/bash

set -e

echo "Starting SmartOps BI reporting workflow..."

echo "Step 1/2: Exporting KPI CSV files from PostgreSQL..."
./etl/export_kpis.sh

echo "Step 2/2: Generating automated business insight summary..."
source venv/bin/activate
python ai_reporting/generate_summary.py
deactivate

echo "SmartOps BI reporting workflow completed successfully."
