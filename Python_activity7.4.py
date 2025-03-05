user = str(input("Enter A String: "))
r_string = ""
for i in range(len(user) -1, 0, -1):
    r_string += user[i]
print("Reversed String: ", r_string)