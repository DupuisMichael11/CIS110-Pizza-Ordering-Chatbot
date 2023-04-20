print("Hello, my name is Alex your virtual assistant. I will help you order a pizza!")
print("I would like to ask you a few questions. After typing your answer please press enter.")
userName = input("\nEnter your name:  ")
print(f"\nHello, {userName}. Nice to meet you!")
size = input("\nWhat size pizza would you like? Enter Small, Medium, or Large:  ")
flavor = input("\nEnter the flavor of pizza:  ")
crustType = input("\nWhat  type of crust do you like:  ")
quantity = input("\nHow many pizza's would you like to order? Please Enter a numeric value:  ")
quantity =int(quantity)
mmethod = input ("\nWill this be carry out or delivery:  ")
salesTax = 1.1
pizzaCost = 14.99
total = (pizzaCost * quantity) * salesTax
print("-" * 10)
print(f"Thank you, {userName}, for your order.")
print(f"your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.")
print("-" * 10)

