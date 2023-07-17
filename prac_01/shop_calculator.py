"""
get number_of_item, price_of_item
    while number_of_item < 0
    display error message
    get number_of_item

for i in range(number_of_item)
    total_price += price_of_item

if total_price > 100
    final_price = total_price * 0.9
else
    final_price = total_price
"""
total_price = 0
DISCOUNT_RATE = 0.9

number_of_item = int(input("Number of item:"))
while number_of_item < 0:
    print("Invalid number.")
    number_of_item = int(input("Number of item:"))

for i in range(number_of_item):
    price_of_item = float(input("Price of item:"))
    total_price += price_of_item

if total_price > 100:
    total_price = total_price * DISCOUNT_RATE


print(f"Total price for {number_of_item} items is ${total_price:.2f}")
