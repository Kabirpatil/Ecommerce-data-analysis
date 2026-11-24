
import pandas as pd

# Load dataset
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")

# 1. Count orders by status
print("\nORDER STATUS DISTRIBUTION")
print(orders["order_status"].value_counts())

# 2. Check missing values by order status
print("\nMISSING VALUES BY ORDER STATUS")

missing_analysis = orders.groupby("order_status").agg(
    total_orders=("order_id", "count"),
    missing_approval=("order_approved_at",
                      lambda x: x.isnull().sum()),
    missing_carrier=("order_delivered_carrier_date",
                     lambda x: x.isnull().sum()),
    missing_delivery=("order_delivered_customer_date",
                      lambda x: x.isnull().sum())
)

print(missing_analysis)

# 3. Check duplicate order IDs
print("\nDUPLICATE ORDER IDS")
print(orders["order_id"].duplicated().sum())

# 4. Check unique order statuses
print("\nUNIQUE ORDER STATUSES")
print(orders["order_status"].unique())
