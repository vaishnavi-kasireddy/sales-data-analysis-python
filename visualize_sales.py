
import pandas as pd
import matplotlib.pyplot as plt

# Read our CSV data
df = pd.read_csv("sales_data.csv")

# Calculate revenue
df["Revenue"] = df["Price"] * df["Quantity"]

# Group revenue by product
product_sales = df.groupby("Product")["Revenue"].sum()

# Create a bar chart
plt.figure(figsize=(8, 5))

product_sales.plot(kind="bar", color="steelblue")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=0)

plt.tight_layout()

# Save chart as an image
plt.savefig("sales_chart.png")

# Display the chart
plt.show()
