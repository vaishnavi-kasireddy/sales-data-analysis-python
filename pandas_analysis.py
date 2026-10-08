
import pandas as pd

# Read our sales data
df = pd.read_csv("sales_data.csv")

# Display the data
print(df)

# Calculate revenue
df["Revenue"] = df["Price"] * df["Quantity"]

# Calculate total revenue
total_revenue = df["Revenue"].sum()

# Revenue by product
product_sales = df.groupby("Product")["Revenue"].sum()

# Find highest-revenue product
best_product = product_sales.idxmax()
highest_revenue = product_sales.max()

# Display report
print("===== SALES ANALYSIS REPORT =====")
print(df)

print("\nTotal Revenue: $", total_revenue)

print("\nRevenue by Product:")
print(product_sales)

print("\nBest Product:", best_product)
print("Highest Product Revenue: $", highest_revenue)