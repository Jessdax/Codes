import time

def mix_ingredients(ingredients):
    print("Mixing Ingredients...")

    # Check if required ingredients are present
    if "Jessitol Base" not in ingredients:
        print("Mixing Failed... Jessitol Base not found.")
        return False

    if "Stabilizer" not in ingredients:
        print("Mixing Failed... Stabilizer not found.")
        return False

    # Simulate mixing Jessitol Base
    print("🧪 Jessitol Base Found.")
    time.sleep(2)

    # Simulate mixing Stabilizer
    print("🧪 Mixing Stabilizer.")
    time.sleep(1)

    print("🧪 Ingredients mixed and heated at 60°C.")
    return True

def adjust_temperature():
    while True:
        try:
            temp = float(input("🌡️ Enter the temperature to adjust (°C): "))
            time.sleep(1)
            print(f"🌡️ Temperature set to {temp}°C. Processing Updated.")
            break
        except ValueError:
            print("❌ Invalid temperature input. Please enter a valid number.")

def process_formula(ingredients):
    success = mix_ingredients(ingredients)
    if not success:
        return "Processing Failed"

    adjust_temperature()
    time.sleep(3)
    return "Processing Complete"

