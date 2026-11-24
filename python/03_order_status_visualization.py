
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load dataset
# orders = pd.read_csv("data/raw/olist_orders_dataset.csv")

# # Count order statuses
# status_counts = orders["order_status"].value_counts()

# # Display chart
# plt.figure(figsize=(12, 6))

# sns.barplot(
#     x=status_counts.index,
#     y=status_counts.values
# )

# plt.title("E-Commerce Order Status Distribution")
# plt.xlabel("Order Status")
# plt.ylabel("Number of Orders")
# plt.xticks(rotation=45)

# plt.tight_layout()
# plt.savefig("reports/order_status_distribution.png")

# plt.show()



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")

# Count order statuses
status_counts = orders["order_status"].value_counts()

# Calculate percentage
status_percentage = (
    orders["order_status"].value_counts(normalize=True) * 100
)

# Set chart style
sns.set_theme(style="whitegrid")

plt.figure(figsize=(12, 7))

# Create horizontal bar chart
ax = sns.barplot(
    x=status_counts.values,
    y=status_counts.index,
    hue=status_counts.index,
    palette="viridis",
    legend=False
)

# Add count and percentage labels
for i, bar in enumerate(ax.patches):
    count = status_counts.iloc[i]
    percentage = status_percentage.iloc[i]

    ax.text(
        bar.get_width() + 100,
        bar.get_y() + bar.get_height() / 2,
        f"{count:,} ({percentage:.2f}%)",
        va="center",
        fontsize=10
    )

# Titles and labels
plt.title(
    "E-Commerce Order Status Distribution",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.xlabel("Number of Orders", fontsize=12)
plt.ylabel("Order Status", fontsize=12)

plt.xlim(0, status_counts.max() * 1.25)

sns.despine(left=True, bottom=True)

plt.tight_layout()

# Save chart
plt.savefig(
    "reports/order_status_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
