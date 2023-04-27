print("Hello, my name is Alex your virtual assistant. I will help you order a pizza!")
print("I would like to ask you a few questions. After typing your answer please press enter.")
userName = input("\nEnter your name:  ")
if userName. lower() == "michael dupuis":
    print(f"\nMy creator, {userName}. Pleasure to serve you!")
else:
    print(f"\nHello, {userName}. Nice to meet you !")
size = input("\nWhat size pizza would you like? Enter Small, Medium, or Large:  ")
flavor = input("\nEnter the flavor of pizza:  ")
crustType = input("\nWhat type of crust do you like:  ")
quantity = input("\nHow many pizza's would you like to order? Please Enter a numeric value:  ")
quantity =int(quantity)
method = input ("\nWill this be carry out or delivery:  ")
if method. lower() == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0
salesTax = 1.1
if size. lower() == "small":
    pizzaCost = 8.99
elif size. lower() == "medium":
    pizzaCost = 14.99
elif size. lower() == "large":
    pizzaCost = 17.99
total = (pizzaCost * quantity) * salesTax + deliveryFee
print("-" * 10)
print(f"Thank you, {userName}, for your order.")
print(f"your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.")
if total >= 50:
    print("\nCongratulations! You've been awarded a $10 off coupon on your next order.")
else:
    print("\nOrders over $50 will receive a free $10 off coupon!")
print("-" * 10)

