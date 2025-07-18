#Step 1: Get user input to create outfit tuples
tops = tuple(input("Enter 3 tops separated by commas: ").split(","))
bottoms = tuple(input("Enter 3 bottoms separated by commas: ").split(","))
shoes = tuple(input("Enter 3 types of shoes separated by commas: ").split(","))

# Step 2: Display one item from each category using index
print("\nYour selected outfit pieces:")
print("Top of choice:", tops[0])
print("Bottom of choice:", bottoms[1])
print("Shoe of choice:", shoes[2])

# Step 3: Concatenate all outfit elements into one tuple

complete_outfit = tops + bottoms + shoes
print(f"\nTops: {tops[0]}|{tops[1]}|{tops[2]}\nBottoms: {bottoms[0]}|{bottoms[1]}|{bottoms[2]}\nShoes: {shoes[0]}|{shoes[1]}|{shoes[2]}")
print("\nComplete Outfit Tuple:", complete_outfit)

# Step 4: Display a slice of the first 5 items
print("Preview of outfit plan (first 5 items):", complete_outfit[:5])

# Implementing tops[0] = "Tank Top" produces "TypeError: 'tuple' object does not support item assignment"