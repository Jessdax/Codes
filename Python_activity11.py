# Functions, Parameters and Scope
greetings = "Konbanwa!"
def greet(name):
    print(f"\n{greetings}{name}!")
greet("Jessie")

def calculate(d):        
    quantity = 10
    price = 5
    total_price = 10 * 5
    return total_price - (total_price * d)

result = calculate(.20)
print("\nThe Discounted Price is",result)

global_total = 10
def time(h, s):
    global global_total
    total = h / s + global_total
    return total

hour = 10
subject = 6
total = time(hour, subject)
rounded = round(total)
print(f"\nStudy Time: {total:.2f}")
print(f"\nStudy Time: {rounded} Hours/Subject(Rounded)\n")

    




