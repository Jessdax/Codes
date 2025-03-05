n= (input("Enter A List:"))
lst = [int(num) for num in n.split()] 
large = lst[0]
for val in lst:
    if val > large:
        large = val
print("The Largest Number in the list is: " , large)