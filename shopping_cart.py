customer_name = input("Enter customer name: ")

product1 = input("Enter product 1 name: ")
price1 = float(input(f"Enter the price of {product1}: "))

product2 = input("Enter product 2 name: ")
price2 = float(input(f"Enter the price of {product2}: "))

product3 = input("Enter product 3 name: ")
price3 = float(input(f"Enter the price of {product3}: "))

subtotal = price1 + price2 + price3

if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0

discount = subtotal * discount_rate
final_total = subtotal - discount

print(f"\nCustomer Name: {customer_name}")
print(f"Product 1: {product1} | Price: {price1:g}")
print(f"Product 2: {product2} | Price: {price2:g}")
print(f"Product 3: {product3} | Price: {price3:g}")
print(f"Subtotal: {subtotal:g}")
print(f"Discount: {discount:g}")
print(f"Final Total: {final_total:g}")