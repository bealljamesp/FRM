import sys

import numpy as np
import pandas as pd


def check_environment():
    print("--- Risk Quant Environment Check ---")

    # Check Math Libraries
    print(f"Pandas version: {pd.__version__}")
    print(f"NumPy version: {np.__version__}")

    # Check Database Driver
    try:
        import psycopg2

        print("PostgreSQL driver (psycopg2): INSTALLED")
    except ImportError:
        print("PostgreSQL driver (psycopg2): MISSING")
        print("Action: Run 'pip install psycopg2-binary' in your terminal.")

    # Check Python Version
    print(f"Python version: {sys.version.split()[0]}")


if __name__ == "__main__":
    check_environment()
