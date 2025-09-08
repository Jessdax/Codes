print("🔍 INTERROGATION LOG: Suspect #7 – Digital Transcript")
# Suspect's basic info
name = input("🧑 Enter suspect's name: ")
# 1. ValueError: Convert input to age
try:
    age = int(input("🧑 Enter suspect's age: "))
except ValueError:
    print("⚠️  Invalid age input. Setting the default age to 0.")
    age = 0

# 2. TypeError: Combine string and number
try:
    statement = "Suspect " + name + " has a record count of " + 3
except TypeError:
    print("⚠️  Type error... \n🔧 Fixing... \n📺 Output has the record count of 3.")

# 3. KeyError: Accessing missing profile data
try:
    profile = {"name": name, "age": age}
    print("Suspect name:", profile["name"])
except KeyError:
    print("⚠️  Occupation data missing in profile.")

# 4. IndexError: Accessing past aliases
try:
    aliases = ["🟥🐍 Red Viper", "⬛🐍 Black Mamba"]
    print("Previous alias used:", aliases[3])
except IndexError:
    print(f"⚠️  No alias found... Showing Available aliases: {aliases}")

# 5. ZeroDivisionError: Time calculations
try:
    interrogation_minutes = int(input("How many minutes did the interrogation last? "))
    questions_asked = int(input("How many questions were asked? "))
    print("Average time per question:", interrogation_minutes / questions_asked)

except ZeroDivisionError:
    print("⚠️  Error: Cannot divide by zero. Questions asked must be greater than zero.")


print("🗃 Interview logged successfully.")
