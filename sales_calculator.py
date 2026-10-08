laptop_price = 800
phone_price = 500
tablet_price = 300 

laptop_quantity = 10
phone_quantity = 8
tablet_quantity = 4

# calculate revenue

laptop_sales = laptop_price  * laptop_quantity
phone_sales = phone_price * phone_quantity
tablet_sales = tablet_price * tablet_quantity

#total revenue

total_revenue = laptop_sales+phone_sales+tablet_sales

print("----Sales Report-----")

print ("laptop_sales:$", laptop_sales)
print ("phone_sales:$", phone_sales)
print ("tablet_sales: $", tablet_sales)
print("-----------------")
print("total_revenue:$", total_revenue)