phone_price = int(input(" What is your Phone Plan Price?($): "))
coupon = int(input(" Coupon Value Available($): "))
c_price = phone_price - coupon
tax = c_price * .12
f_price = c_price + tax
f_price_new = "{:.2f}".format(f_price)

if f_price < 50:
    print(" Good Plan! Total: ", f_price_new)
else :
    print(" Too Much! Total: ", f_price_new)
