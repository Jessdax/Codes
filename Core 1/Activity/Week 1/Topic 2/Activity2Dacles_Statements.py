# Basic and Net Pay Computation
hours_work = 6
hourly_rate = 100
deduction = 80
basic_pay = hours_work * hourly_rate
net_pay = basic_pay - deduction

# Output
print("=" * 35)
print("      Employee's Net Pay")
print("-" * 35)
print(f"       Net Pay: {net_pay} ")

#checks if net pay is greater than 500 or not
def checkNet_pay():
    if net_pay >= 500:
        print("       Net Pay is Sufficient")
    else:
        print("       Net Pay is too low")
    print("=" * 35)
checkNet_pay()

# Loop without for or while
# def count(n):
#     if n > 20:           # Base case: stop if n > 5
#         return
#     print(n)
#     count(n + 1)        # Recursive call: count the next number

# count(2)  # Output: 1 2 3 4 5

# While loop
# print("\nUsing while loop:")

# words = ["apple", "banana", "kiwi", "orange"]
# total_length = 0
# i = 0

# while i < len(words):
#     total_length += len(words[i])
#     i += 1

# average_length = total_length / len(words)
# print("Average word length is:", average_length)

# for loop
# print("Using for loop:")

# words = ["apple", "banana", "kiwi", "orange"]
# total_length = 0

# for word in words:
#     total_length += len(word)

# average_length = total_length / len(words)
# print("Average word length is:", average_length)