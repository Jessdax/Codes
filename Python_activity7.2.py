vowels = "aeiouAEIOU"  # Define vowels
count = 0  # Initialize count
found_vowels = []  # List to store found vowels

# Get user input
input_string = input("Enter a string: ")

# Iterate through each character in the string
for char in input_string:
    print(char)
    if char in vowels:  # Check if character is a vowel
        count += 1  # Increment count
        found_vowels.append(char)  # Store the vowel

# Print the total count and found vowels
print("Vowels found:", " ".join(found_vowels))
print("Number of vowels in the string:", count)
