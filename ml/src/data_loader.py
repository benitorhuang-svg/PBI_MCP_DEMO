"""
Data Loader Module
==================
Utilities for loading CSV data from the DataSource folder.
"""

import pandas as pd
from pathlib import Path


def get_data_path() -> Path:
    """Get the path to the DataSource folder."""
    return Path(__file__).parent.parent.parent / "DataSource"


def load_candy_sales() -> pd.DataFrame:
    """Load Candy Sales data."""
    return pd.read_csv(get_data_path() / "Candy_Sales.csv")


def load_candy_products() -> pd.DataFrame:
    """Load Candy Products data."""
    return pd.read_csv(get_data_path() / "Candy_Products.csv")


def load_candy_factories() -> pd.DataFrame:
    """Load Candy Factories data."""
    return pd.read_csv(get_data_path() / "Candy_Factories.csv")


def load_candy_targets() -> pd.DataFrame:
    """Load Candy Targets data."""
    return pd.read_csv(get_data_path() / "Candy_Targets.csv")


def load_uszips() -> pd.DataFrame:
    """Load US ZIP codes data."""
    return pd.read_csv(get_data_path() / "uszips.csv")


def load_all_data() -> dict[str, pd.DataFrame]:
    """Load all datasets and return as a dictionary."""
    return {
        "sales": load_candy_sales(),
        "products": load_candy_products(),
        "factories": load_candy_factories(),
        "targets": load_candy_targets(),
        "uszips": load_uszips(),
    }


if __name__ == "__main__":
    # Quick test
    data = load_all_data()
    for name, df in data.items():
        print(f"{name}: {len(df)} rows, {len(df.columns)} columns")
