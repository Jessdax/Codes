print("----------Part 1----------------------")
print("Even Numbers in 1 - 50 \n")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")

print("----------Part 2---------------------")
print("Skip the digits divisible by 3 and 5 \n")
for i in range(1, 51):
    if i % 2 == 0:        
        if i % 3 == 0 and i % 5 == 0 :
            continue
        print(i,end=" ")
print("\n")

print("----------Part 3--------------------")
print("Adding all odd number from 1 to 100 and summing their value up to 1000 \n")
total_sum = 0
num = 1

while num <= 100:
    if num % 2 == 1:
        total_sum += num
        if total_sum + num > 1000:           
            break

    num += 1

print(f"The sum of numbers from 1 to 100 is: {total_sum} and broke on No.{num} \n")

print("----------Part 4------------------")
print("        Multiplication Table")
for row in range(1,6):
    for col in range(1,6):
        product = row * col
        print(f"{product}", end="\t") 

    print()  
print("----------------------------------")



