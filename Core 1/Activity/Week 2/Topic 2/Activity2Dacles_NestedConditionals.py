while True:
    print("----------Grade Remark Identifier:---------- ")
    try:
        grades = int(input("      Enter your grade(1-100): "))
    
        print("---------------Remark---------------")
        match grades:
            case a if grades == 100:
                result = "Perfect Score!"
            case b if grades >= 90 and grades <= 99:
                result = "Excellent Work"
            case c if grades >= 80 and grades <= 89:
                result = "Great Job"
            case d if grades >= 70 and grades <= 79:
                result = "Good Effort"
            case e if grades >= 60 and grades <= 69:
                result = "Needs Improvement"
            case f if grades >= 0 and grades <= 60:
                result = "Try Again"
                
        print(f"              Grade: {grades} \n        Remark: {result}")
        print("-" * 35)        
        break
    except:
        print("         Invalid! Please Try again")
