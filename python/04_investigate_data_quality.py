
import pandas as pd

orders = pd.read_csv("data/raw/olist_orders_dataset.csv")

# Find delivered orders with missing delivery dates
delivered_missing = orders[
    (orders["order_status"] == "delivered") &
    (orders["order_delivered_customer_date"].isnull())
]

print("DELIVERED ORDERS WITH MISSING DELIVERY DATES")
print(delivered_missing[
    [
        "order_id",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]
])

print("\nTOTAL ANOMALOUS RECORDS:")
print(len(delivered_missing))

# Check missing approval dates in delivered orders
print("\nMISSING APPROVAL DATES:")
print(
    orders[
        (orders["order_status"] == "delivered") &
        (orders["order_approved_at"].isnull())
    ][["order_id", "order_approved_at"]]
)


#Date and Time Conversion. 
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(
        orders[col],
        errors="coerce"
    )

print(orders[date_columns].dtypes)