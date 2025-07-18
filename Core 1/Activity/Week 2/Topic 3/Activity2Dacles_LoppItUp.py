# Activity A: While Loop ‒ "Number Counter"
print("📘 Activity A: Number Counter")
num = int(input("Enter a number: "))

count = 1
while count <= num:
    print(count)
    count += 1

print("\n-------------------------")

# Activity B: While Loop ‒ "Password Retry"
print(" Activity B: Password Retry")
correct_password = "admin123"
password = input("Enter password: ")

while password != correct_password:
    print("Wrong password. Try again.")
    password = input("Enter password: ")

print("Access granted!")

print("\n-------------------------")

# Activity C: For Loop ‒ "List Summer"
print("Activity C: List Summer")
# You can hardcode or take user input. Here's using input:
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

total = 0
for n in numbers:
    total += n

print(f"Numbers: {numbers}")
print(f"Sum = {total}")
