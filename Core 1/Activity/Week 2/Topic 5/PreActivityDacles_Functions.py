print("---------- Part 1 ----------")
def greet_user(name):
    message = f"Hello, {name}!"
    return message
users = ["Ana", "Ben", "Carlos"]
for user in users:print(greet_user(user))

print("---------- Part 2 ----------")
# 1. Define a function that calculates the total price after tax
def calculate_total(price, tax_rate):
    total = price + (price * tax_rate)
    return total

# 2. Use a dictionary to store items and their prices
products = {"notebook": 25,"pen": 10,"eraser": 5
}
products["pencil"] = 10
products["Crayons"] = 25

# 3. Loop through the dictionary and calculate total for each item
for item, price in products.items():
    final_price = calculate_total(price, 0.25)
    print(f"{item.capitalize()} -Final Price: {final_price}")

print("---------- Part 3 ----------")
x = 10

def multiply(num):
    x = 5
    return num * x
result = multiply(3)
print(result)
print(x)

print("---------- Part 4 ----------")
print("---------- A ----------")
def custom_greeting(name, day):
    return f"Good Day, {name}! Happy {day}!"

print(custom_greeting("Jessie", "Thursday"))

print("---------- B ----------")
def count_evens(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count

# Sample run
nums = [2, 5, 8, 11, 4]
print(count_evens(nums))  # Output: 3

