# Users Grade 
grade = int(input(" What is your Test Score?: "))
# Users Bonus
bonus = int(input(" Bonus: "))
fscore = grade + bonus

# Print The Final Score
print("Final Score:", fscore)

# Conditional Statement
if fscore <= 100:

    if grade <=100 and bonus <= 10:
       
        if fscore >= 90:
            print("Grade A")

        elif fscore >= 80: 
            print("Grade B")

        elif fscore >= 70:
            print("Grade C")

        elif fscore >= 60:
            print("Grade D")

        else:
            print("Grade E")    
    else:
        print(" Invalid Score ")

else: 
    print(" Invalid Score")