# Basic and Net Pay Computation
hours_work = 6
hourly_rate = 100
deduction = 80
basic_pay = hours_work * hourly_rate
net_pay = basic_pay - deduction
bonus = 5
net_pay += bonus

# Checking of final pay if 500 and even
if net_pay >= 500 and net_pay % 2 == 0 :
    result = True
else:
    result = False

# Output
print("=" * 35)
print("        Employee's Net Pay")
print("-" * 35)
print(f"     Final Pay after bonus: {net_pay} ")
print(f"    Is above 500 and Even: {result}" )
print("=" * 35)

# loops the net pay plus bonus
for i in range(90):
    print(i +1,"             ",net_pay)
print("=" * 35)