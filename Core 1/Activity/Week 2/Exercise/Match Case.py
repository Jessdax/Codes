print("-" * 40)
print("     Transportation System")
print("-" * 40)
transportation = str(input("Enter the mode of transportation: ")).strip().lower()
if transportation not in ("jeep", "bus", "bus aircon", "taxi", "train", "motorcycle", "motor"):
    print("Transportation not registered!")
    exit()

try:
    student_senior = int(input("How many are students: "))
    regular = int(input("How many are regulars: "))
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()
    
passenger = student_senior + regular

match transportation:
    case "jeep":
        fare = 12
    case "bus":
        fare = 20
    case "bus aircon":
        fare = 25   
    case "taxi":
        if passenger >= 5:
            print("Warning! Taxi can only occupied by 4 passengers!.")
            exit()
        else:
            fare = 45
    case "train":
        fare = 30
    case "motorcycle" | "motor":
        if passenger >= 2:
            print("Warning! Motor/Motorcycle can only occupied by 1 passengers!.")
            exit()
        else:
            fare = 10

rate = regular * fare
discount = fare * .85
dis_total = discount * student_senior
total_rate = rate + dis_total

print("-----------------Rate-----------------")
print(f"Student's Fare: {discount:.2f}")
print(f"Regular's Fare: {fare}")
print("---------------Summary---------------")
print(f"Total Passenger: {passenger}\nStudent / Seniors: {student_senior}\nRegular: {regular}")
print(f"Transportation: {transportation}\nTotal Fare: {total_rate:.2f}")
print("-" * 40)