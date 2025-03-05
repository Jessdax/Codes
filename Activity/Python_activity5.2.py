# Ask the user for the Price
price = int(input(" What is the Snack Price? "))
discount = int(input(" Discount Amount: "))
discount_price = price - discount 
tax = discount_price * .12
f_price = discount_price + tax 

# Conditional Statement
if f_price < 3 :
    print(f"The Final Price is {f_price:.2f} Cheap Snack!")