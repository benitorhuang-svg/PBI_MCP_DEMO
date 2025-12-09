# PBI_MCP_DEMO

A Power BI semantic model demonstration project built with **Power BI MCP (Model Context Protocol)** integration, showcasing how to programmatically create and manage Power BI semantic models using AI-assisted development.

## 🎯 Project Overview

This repository demonstrates the use of **powerbi-modeling-mcp** to:
- Create Power BI semantic models programmatically
- Load CSV data sources using Power Query (M language)
- Build a complete data model for candy sales distribution analysis

## 📁 Project Structure

```
PBI_MCP_DEMO/
├── Demo.pbip                    # Power BI Project file
├── Demo.SemanticModel/          # Semantic model definition
│   ├── definition.pbism
│   └── definition/
│       ├── database.tmdl
│       └── model.tmdl
├── Demo.Report/                 # Report definition
│   └── definition.pbir
├── DataSource/                  # CSV data files
│   ├── Candy_Factories.csv      # Factory locations
│   ├── Candy_Products.csv       # Product catalog
│   ├── Candy_Sales.csv          # Sales transactions
│   ├── Candy_Targets.csv        # Sales targets
│   ├── candy_distributor_data_dictionary.csv
│   └── uszips.csv               # US ZIP code reference
└── docs/                        # Documentation
    └── implementation_plan_v1.md
```

## 📊 Data Model

The semantic model is designed for **Candy Distributor Sales Analysis** with the following entities:

| Table | Description | Records |
|-------|-------------|---------|
| Candy_Factories | Factory locations and details | ~5 |
| Candy_Products | Product catalog with categories | ~50 |
| Candy_Sales | Sales transactions | ~40,000+ |
| Candy_Targets | Sales targets by region | ~4 |
| uszips | US ZIP codes for geo analysis | ~33,000+ |

## 🛠️ Technology Stack

- **Power BI Desktop** - Business intelligence and visualization
- **Power BI MCP** - Model Context Protocol for AI-assisted semantic model development
- **TMDL** - Tabular Model Definition Language
- **Power Query (M)** - Data transformation and loading

## 🚀 Getting Started

### Prerequisites

1. **Power BI Desktop** (latest version recommended)
2. **Power BI MCP Server** (not included in this repo)

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/benitorhuang-svg/PBI_MCP_DEMO.git
   ```

2. Open `Demo.pbip` with Power BI Desktop

3. Configure data source paths if needed (update to your local DataSource folder path)

## 📚 Documentation

- [Implementation Plan v1](docs/implementation_plan_v1.md) - Initial data loading and model design plan

## 🔧 Power BI MCP Integration

This project was created using **powerbi-modeling-mcp**, which enables:
- AI-assisted semantic model development
- Programmatic table and measure creation
- TMDL import/export capabilities
- DAX query execution and validation

## 📝 License

This project is for demonstration purposes.

## 🤝 Contributing

Feel free to open issues or submit pull requests for improvements.

---

*Built with ❤️ using Power BI MCP*
