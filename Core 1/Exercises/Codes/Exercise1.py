name = input("Omai no namae wa?: ")

gender = input(str("Are you a Male or Female?(m/f):"))
if gender == "m":
    print("Konichiwa!",name+"-kun\n")
if gender == "f":
    print("Konichiwa!",name+"-chan\n")

food = input("What is your favorite food?: ") 
print("Eating",food,"is your stress reliever!\n")

age = int(input("How old are you?: "))
print("You are",age,"years old")
if age >= 20:
    print("Mag Asawa kana",name+"!\n")
else:
    print("Bagets ka pa pala",name+"!\n")

fav_color = input("Favorite Color?: ")
print("So your favorite color is",fav_color,"\n")

leisure = input("What do you do in your free time?: ")
print("Oh! so you like doing/playing",leisure,"when bored\n")






