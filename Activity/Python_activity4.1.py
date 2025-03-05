# Ask the user for the Original Price
price = int(input("Enter The Original Price Of The Product: "))
dis = int(input("Enter The Discount Amount: "))
dis_price = price - dis
tax = dis_price * .12
final = dis_price + tax

#Print
print(f"Final Amount: {final:.2f} ")