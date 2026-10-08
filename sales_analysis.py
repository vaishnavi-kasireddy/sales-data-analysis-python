
# Sales data
products = ["Laptop", "Phone", "Tablet"]
prices = [800, 500, 300]
quantities = [5, 12, 4]

total_revenue = 0

print("===== SALES REPORT =====")

for i in range(len(products)):
    sales = prices[i] * quantities[i]

    print(products[i], "Revenue: $", sales)

    total_revenue = total_revenue + sales

print("------------------------")
print("Total Revenue: $", total_revenue)


# Find the product with the highest revenue
highest_sales = 0
best_product = ""

for i in range(len(products)):
    sales = prices[i] * quantities[i]

    if sales > highest_sales:
        highest_sales = sales
        best_product = products[i]

print("Best Product:", best_product)
print("Highest Product Revenue: $", highest_sales)

