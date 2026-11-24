
import pandas as pd

# STEP 1: Load original dataset
orders = pd.read_csv(
    "data/raw/olist_orders_dataset.csv"
)

# STEP 2: Identify date columns
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

# STEP 3: Convert columns into datetime format
for col in date_columns:
    orders[col] = pd.to_datetime(
        orders[col],
        errors="coerce"
    )

print("UPDATED DATA TYPES")
print(orders[date_columns].dtypes)

# STEP 4: Check missing values
print("\nMISSING VALUES AFTER CONVERSION")
print(orders[date_columns].isnull().sum())

# STEP 5: Calculate delivery time in days
orders["delivery_time_days"] = (
    orders["order_delivered_customer_date"] -
    orders["order_purchase_timestamp"]
).dt.total_seconds() / (24 * 60 * 60)

# STEP 6: Filter delivered orders
delivered_orders = orders[
    (orders["order_status"] == "delivered") &
    (orders["delivery_time_days"].notnull())
]

# STEP 7: Calculate average delivery time
average_delivery = delivered_orders[
    "delivery_time_days"
].mean()

print("\nAVERAGE DELIVERY TIME")
print(round(average_delivery, 2), "days")

# STEP 8: Calculate minimum delivery time
print("\nMINIMUM DELIVERY TIME")
print(round(
    delivered_orders["delivery_time_days"].min(), 2 
),"days")

# STEP 9: Calculate maximum delivery time
print("\nMAXIMUM DELIVERY TIME")
print(round(
    delivered_orders["delivery_time_days"].max(), 2 
),"days")

# STEP 10: Save cleaned dataset
orders.to_csv(
    "data/cleaned/orders_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")


# print("\nFINAL MISSING VALUE REPORT")
# print(orders.isnull().sum())

# print("\nTOTAL MISSING VALUES")
# print(orders.isnull().sum().sum())