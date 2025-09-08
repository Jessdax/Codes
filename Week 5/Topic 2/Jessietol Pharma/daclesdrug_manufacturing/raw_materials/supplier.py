import time

def get_ingredients():
    time.sleep(1)
    return ["Jessitol Base", "Caffeine Extract", "Stabilizer"]

def check_inventory():
    time.sleep(1)
    available = input("Are all ingredients available? (yes/no): ").strip().lower()
    time.sleep(2)
    if available == "no":
        print("❌ Missing ingredients. Production halted.")
        return False
    else:
        print("✅ All ingredients available. Ready to proceed.")
        return True

def list_missing_items():
    time.sleep(1)
    missing = input("\nEnter missing ingredients (comma-separated), or press Enter if none: ").strip()
    time.sleep(2)
    if missing:
        missing_list = [item.strip() for item in missing.split(",") if item.strip()]
    else:
        missing_list = []
    print(f"Missing ingredients: {', '.join(missing_list)}")
    return missing_list

def inventory_report():
    time.sleep(1)
    print("\n--- Inventory Report ---")
    ingredients = get_ingredients()
    time.sleep(1)
    print(f"Ingredients: {', '.join(ingredients)}")
    all_available = check_inventory()
    time.sleep(2)
    if not all_available:
        missing_items = list_missing_items()
        if missing_items:
            time.sleep(1)
            print("Status: Missing items detected!")
            print(f"Missing: {','.join(missing_items)}")
            print("Production cannot continue.")
        else:
            time.sleep(1)
            print("Warning: No missing items listed despite 'no' availability.")
    else:
        time.sleep(1)
        print("Status: All ingredients available.")
        print("Production can proceed.")

if __name__ == "__main__":
    inventory_report()
