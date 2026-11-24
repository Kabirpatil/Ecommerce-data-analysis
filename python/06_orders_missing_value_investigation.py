
import pandas as pd

orders = pd.read_csv("data/cleaned/orders_cleaned.csv")

# Analyse missing values according to order status

missing_analysis = orders.groupby("order_status").agg(
    total_orders=("order_id", "count"),

    missing_approval=("order_approved_at",
                      lambda x: x.isnull().sum()),

    missing_carrier=("order_delivered_carrier_date",
                     lambda x: x.isnull().sum()),

    missing_delivery=("order_delivered_customer_date",
                      lambda x: x.isnull().sum())
)

print("\nMISSING VALUES BY ORDER STATUS")
print(missing_analysis)

# Investigate delivered orders with missing delivery dates

delivered_missing = orders[
    (orders["order_status"] == "delivered") &
    (orders["order_delivered_customer_date"].isnull())
]

print("\nDELIVERED ORDERS WITH MISSING DELIVERY DATES")
print(delivered_missing)

print("\nTOTAL:")
print(len(delivered_missing))
