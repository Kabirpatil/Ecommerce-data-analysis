import pandas as pd
import os

# Dataset location
data_path = "data/raw"

# Load orders dataset
orders = pd.read_csv(
    os.path.join(data_path, "olist_orders_dataset.csv")
)

# 1. Display first 5 records
print("\nFIRST FIVE RECORDS")
print(orders.head())

# 2. Check total rows and columns
print("\nDATASET SHAPE")
print(orders.shape)

# 3. Check column names
print("\nCOLUMN NAMES")
print(orders.columns.tolist())

# 4. Check data types
print("\nDATA TYPES")
print(orders.dtypes)

# 5. Check missing values
print("\nMISSING VALUES")
print(orders.isnull().sum())

# 6. Check duplicate records
print("\nDUPLICATE ROWS")
print(orders.duplicated().sum())

# 7. Statistical summary
print("\nDATA SUMMARY")
print(orders.describe(include="all"))
