# Problem 1: User Profile
print("-" * 70)
print("Your Profile")

# Input user information
_name = input("Enter your name: ")
_age = input("Enter your age: ")
_hobby = input("Enter your hobby: ")

# Display user profile
print("-" * 70)
print(f"Hi, I'm {_name}, I'm {_age} years old and I enjoy {_hobby}.")
print("-" * 70)
print("\n")

# Problem 2: Simple Budget Tracker
print("-" * 70)
print("Simple Budget Tracker")

# Input allowance and spending
_allowance = int(input("Enter your allowance: "))
_spending = int(input("Enter your spent allowance: "))
_remaining = _allowance - _spending
_75 = _remaining * .75
_50 = _remaining * .5

# Solving of remaining allowance
print("\n")
print("-" * 70)
if _remaining >= 0:
    print(f"{_name}, You have {_remaining} pesos left from your weekly allowance.")
elif _remaining < 0:
    print(f"{_name}, You have no allowance left!")

# Warning for overspending allowance
print("-" * 70)
if _spending == _allowance:
    print(f"{_name}, You have spent your allowance!")
elif _spending > _allowance:
    print("Warning!")
    print(f"{_name}, You have spent more than your allowance!")

# Warning for remaining allowance
if _remaining >= _50 :
    print(f"Please Be mindful of spending {_name}!")

elif _remaining == _50 :
    print("Warning!")
    print(f"{_name}, You have spent half of your allowance!")

elif _remaining >= _50 :
    print("Warning!")
    print(f"{_name}, You have spent more than half of your allowance!")

elif _remaining >= _75:
    print("Warning!")
    print(f"{_name}, You have spent 75% of your allowance!")
print("-" * 70)


