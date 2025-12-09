# Implementation Plan v1 - Power BI Candy Distributor Data Model

> **Version**: 1.1  
> **Date**: 2025-12-10  
> **Status**: Initial Data Loading Completed

## 🎯 Objective

Build a comprehensive Power BI semantic model for **Candy Distributor Sales Analysis** by loading CSV data sources and establishing a proper data model with relationships, measures, calculated columns, and machine learning predictions.

---

## 📋 Phase Overview

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 1 | Data Source Loading | ✅ Completed |
| Phase 2 | Data Model Design | 🔲 Planned |
| Phase 3 | Measures & Calculations | 🔲 Planned |
| Phase 4 | Visualization | 🔲 Planned |
| Phase 5 | Machine Learning | 🔲 Planned |
| Phase 6 | Deployment & Documentation | 🔲 Planned |

---

## 📊 Phase 1: Data Source Loading (Completed)

### Data Sources

| Source File | Table Name | Description | Status |
|------------|------------|-------------|--------|
| `Candy_Factories.csv` | Candy_Factories | Factory locations | ✅ Loaded |
| `Candy_Products.csv` | Candy_Products | Product catalog | ✅ Loaded |
| `Candy_Sales.csv` | Candy_Sales | Transaction data | ✅ Loaded |
| `Candy_Targets.csv` | Candy_Targets | Sales targets | ✅ Loaded |
| `uszips.csv` | USZips | ZIP code reference | ✅ Loaded |

### Power Query (M) Loading Pattern

Each table was loaded using the following M expression pattern:

```m
let
    Source = Csv.Document(
        File.Contents("C:\path\to\DataSource\filename.csv"),
        [Delimiter=",", Columns=N, Encoding=65001, QuoteStyle=QuoteStyle.None]
    ),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders, {...})
in
    ChangedTypes
```

---

## 📐 Phase 2: Data Model Design

### Proposed Relationships

```
                    ┌──────────────┐
                    │Candy_Factories│
                    └──────┬───────┘
                           │ 1:M
                           ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│Candy_Products │◄───│ Candy_Sales  │───►│   USZips     │
└──────────────┘ 1:M└──────────────┘ M:1└──────────────┘
                           │
                           ▼ M:1
                    ┌──────────────┐
                    │Candy_Targets │
                    └──────────────┘
```

### Key Relationships to Create

| From Table | From Column | To Table | To Column | Cardinality |
|------------|-------------|----------|-----------|-------------|
| Candy_Sales | ProductID | Candy_Products | ProductID | M:1 |
| Candy_Sales | FactoryID | Candy_Factories | FactoryID | M:1 |
| Candy_Sales | ZipCode | USZips | zip | M:1 |

### Date Table

- [ ] Create Date dimension table using DAX or Power Query
- [ ] Mark as Date table for time intelligence

---

## 📈 Phase 3: Measures & Calculations

### Core Measures (Proposed)

```dax
// Total Sales Amount
Total Sales = SUM(Candy_Sales[SalesAmount])

// Total Units Sold
Total Units = SUM(Candy_Sales[Quantity])

// Average Order Value
Avg Order Value = DIVIDE([Total Sales], DISTINCTCOUNT(Candy_Sales[OrderID]))

// Sales vs Target %
Sales Achievement % = DIVIDE([Total Sales], SUM(Candy_Targets[TargetAmount]))
```

### Time Intelligence (Proposed)

- [ ] Date Table generation
- [ ] YTD, MTD, QTD calculations
- [ ] Year-over-Year comparisons
- [ ] Moving averages

### Calculation Groups (Optional)

- [ ] Time Intelligence calculation group
- [ ] Currency conversion group (if applicable)

---

## 🎨 Phase 4: Visualization

### Dashboard Concepts

1. **Sales Overview Dashboard**
   - Total Sales KPI
   - Sales by Product Category
   - Sales by Region (Map)
   - Monthly Trend

2. **Product Performance**
   - Top/Bottom Products
   - Category Analysis
   - Product Mix

3. **Geographic Analysis**
   - Sales by State/Region
   - Factory Coverage Map
   - Distribution Network

4. **Predictive Insights** (ML Integration)
   - Sales Forecast
   - Anomaly Detection Alerts
   - Customer Segmentation View

---

## 🤖 Phase 5: Machine Learning

### Environment Setup

| Tool | Purpose |
|------|---------|
| **Python 3.11+** | Programming language |
| **Astral UV** | Package management (fast, modern alternative to pip) |
| **Jupyter Notebooks** | Interactive development |

### Project Structure

```
PBI_MCP_DEMO/
├── ml/
│   ├── pyproject.toml          # UV project configuration
│   ├── .python-version         # Python version lock
│   ├── notebooks/
│   │   ├── 01_eda.ipynb        # Exploratory Data Analysis
│   │   ├── 02_forecasting.ipynb
│   │   └── 03_segmentation.ipynb
│   ├── src/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── models/
│   │   │   ├── forecasting.py
│   │   │   ├── clustering.py
│   │   │   └── anomaly.py
│   │   └── utils/
│   └── outputs/
│       └── predictions/
```

### ML Use Cases

#### 5.1 Sales Forecasting
- **Objective**: Predict future sales by product/region
- **Algorithms**: Prophet, ARIMA, XGBoost
- **Output**: CSV for Power BI import or DirectQuery via Python script

#### 5.2 Customer Segmentation
- **Objective**: Cluster customers by purchasing behavior
- **Algorithms**: K-Means, DBSCAN, Hierarchical Clustering
- **Output**: Customer segment labels

#### 5.3 Anomaly Detection
- **Objective**: Identify unusual sales patterns
- **Algorithms**: Isolation Forest, DBSCAN, Z-Score
- **Output**: Anomaly flags for sales transactions

#### 5.4 Product Recommendation (Optional)
- **Objective**: Suggest product bundles
- **Algorithms**: Association Rules, Collaborative Filtering

### Python Dependencies (UV)

```toml
[project]
name = "pbi-mcp-demo-ml"
version = "0.1.0"
requires-python = ">=3.11"

[project.dependencies]
pandas = ">=2.0"
numpy = ">=1.24"
scikit-learn = ">=1.3"
prophet = ">=1.1"
xgboost = ">=2.0"
matplotlib = ">=3.7"
seaborn = ">=0.12"
jupyter = ">=1.0"
plotly = ">=5.15"
```

### Integration with Power BI

| Method | Description |
|--------|-------------|
| **CSV Export** | Export predictions to CSV, load via Power Query |
| **Python Visual** | Use Python script visual in Power BI |
| **Dataflow** | Power BI Dataflows with Python |
| **REST API** | Deploy model as API, call from Power BI |

---

## 🚀 Phase 6: Deployment & Documentation

### Deployment Tasks

- [ ] Publish to Power BI Service
- [ ] Configure scheduled refresh
- [ ] Set up workspace and permissions
- [ ] Create Power BI App (optional)

### Documentation Tasks

- [ ] Update README with final project overview
- [ ] Document data dictionary
- [ ] Create user guide for dashboards
- [ ] Document ML model methodology

### Version Control

- [ ] Maintain TMDL files in Git
- [ ] Version ML models and outputs
- [ ] Document change history

### CI/CD (Future Enhancement)

- [ ] GitHub Actions for automated testing
- [ ] Automated deployment to Power BI Service
- [ ] Model retraining pipeline

---

## 📝 Notes

### Technical Decisions

1. **File Path Handling**: Using absolute paths for CSV loading. Consider parameterizing for portability.
2. **Encoding**: Using UTF-8 (65001) for all CSV files
3. **TMDL Format**: Using TMDL for semantic model definition for better version control
4. **Package Manager**: Using Astral UV for Python (faster than pip, modern tooling)

### Known Issues

- None currently identified

### Future Enhancements

- [ ] Add incremental refresh for large tables
- [ ] Create RLS (Row-Level Security) roles
- [ ] Add documentation annotations
- [ ] Create calculation groups for time intelligence
- [ ] Real-time ML model serving with MLflow

---

## 📚 References

- [Power BI MCP Documentation](https://github.com/PowerBI-MCP)
- [TMDL Reference](https://learn.microsoft.com/en-us/analysis-services/tmdl/tmdl-overview)
- [DAX Reference](https://dax.guide/)
- [Astral UV Documentation](https://docs.astral.sh/uv/)
- [Prophet Forecasting](https://facebook.github.io/prophet/)
- [Scikit-learn](https://scikit-learn.org/)

---

*This document serves as a living reference for the project implementation.*
