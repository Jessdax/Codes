# Checking temperature level
print("-" * 40)
temp = float(input("Enter your temperature: "))
print("-" * 40)
if temp > 37 :
    if temp >= 41:
        result = "Critical Fever! Seek Emergency"
    elif temp >= 39:
        result = "High Fever Alert!"
    else:
        result = "Mild Fever"

else:
    if temp == 36.5:
        result = "Perfect Normal Temperature"        
    elif temp < 36:
        if temp <= 0:
            result = f"Temperature is {temp} EMERGENCY!"
        elif temp <= 10:
            result = "Low Temperature! Seek Emergency"
        else:
            result = "Below Normal! Monitor"            
    else:
        result = "Normal"

# Output
print(f"Temperature: {temp}C\nHealth Status: {result}")
print("-" * 40)
