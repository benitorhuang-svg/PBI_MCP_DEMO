---
description: Run ML notebooks and refresh Power BI model
---

# ML Pipeline Workflow

This workflow executes the ML notebooks and updates the Power BI model.

## Prerequisites
- Python 3.11+ installed
- Astral UV installed
- Power BI Desktop running with Demo.pbip open

## Steps

1. Navigate to ml folder
```powershell
cd c:\Users\benit\Desktop\PBI_MCP_DEMO\ml
```

2. Sync dependencies (if needed)
// turbo
```powershell
$env:Path = "C:\Users\benit\.local\bin;$env:Path"; uv sync
```

3. Run EDA notebook
// turbo
```powershell
$env:Path = "C:\Users\benit\.local\bin;$env:Path"; uv run jupyter nbconvert --to notebook --execute --inplace notebooks/01_eda.ipynb
```

4. Run Forecasting notebook
// turbo
```powershell
$env:Path = "C:\Users\benit\.local\bin;$env:Path"; uv run jupyter nbconvert --to notebook --execute --inplace notebooks/02_forecasting.ipynb
```

5. Run Segmentation notebook
// turbo
```powershell
$env:Path = "C:\Users\benit\.local\bin;$env:Path"; uv run jupyter nbconvert --to notebook --execute --inplace notebooks/03_segmentation.ipynb
```

6. Verify outputs exist
// turbo
```powershell
Get-ChildItem c:\Users\benit\Desktop\PBI_MCP_DEMO\ml\outputs\predictions\
```

## Output Files
- `ml/outputs/predictions/sales_forecast.csv` - 6-month sales forecast
- `ml/outputs/predictions/customer_segments.csv` - Customer segmentation results

## Next Steps
After running this workflow, refresh the Power BI model to load the updated CSV data:
1. Open Power BI Desktop
2. Click "Refresh" to reload Sales_Forecast and Customer_Segments tables
