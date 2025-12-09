# Machine Learning Module

ML components for Power BI Candy Distributor Demo project.

## Setup

1. Install [Astral UV](https://docs.astral.sh/uv/)
2. Sync dependencies:
   ```bash
   uv sync
   ```
3. For forecasting features:
   ```bash
   uv sync --extra forecasting
   ```

## Project Structure

```
ml/
├── pyproject.toml          # Project dependencies
├── .python-version         # Python version lock
├── notebooks/              # Jupyter notebooks
├── src/
│   ├── data_loader.py      # Data loading utilities
│   └── models/             # ML models
└── outputs/                # Predictions and exports
```

## Usage

```bash
# Start Jupyter
uv run jupyter notebook

# Run scripts
uv run python src/data_loader.py
```
