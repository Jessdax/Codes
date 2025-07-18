# Loop
while True:
    try:
        grade = 80
        
        if grade < 1 or grade > 100:
            print("Error! Please input 1-100 only.")
            continue  # ask again
        
        elif grade < 50:
            result = "Fail"
        elif grade < 70:
            result = "Pass"
        elif grade < 90:
            result = "Good"
        else:
            result = "Excellent"
        
        print(f"Grade: {result}")
        break  # valid grade entered, break loop

    except (ValueError,TypeError):
        print("Invalid input! Please enter a numeric grade.")
# continue looping automatically
