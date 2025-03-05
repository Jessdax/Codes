# Ask the user for its temperature (in celsius)
cls = float(input("Enter Your Temperature (In Celsius):"))
cls_new = int(cls)
far = (cls_new * 1.8) + 32

# Displaying The Celsius and Fahrenheit
print(f" Your Temperature in Celsius: {cls}" )
print(f" Your Temperature in Fahrenheit: {far}")
