import time

def choose_label():
    while True:
        label = input("What label color do you want? (red/blue/green): ").lower()
        match label:
            case "red"| "blue" | "green":
                time.sleep(2)
                print(f"Label color set to {label.capitalize()}.")
                time.sleep(1)
                print(f"� Applying {label.capitalize()} label...")
                break
            case _:
                time.sleep(.5)
                print("❌ Invalid color. Please choose red, blue, or green.")
                continue

def apply_label():
    choose_label()
    time.sleep(1) 
    print("⌛ Sealing bottle...")
    time.sleep(1) 
    print("✅ Jessitol bottle labeled and sealed successfully!")

def main():
    apply_label()

if __name__ == "__main__":
    main()