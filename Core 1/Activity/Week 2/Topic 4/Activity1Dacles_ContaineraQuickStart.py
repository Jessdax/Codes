print( "---------- Container Quick-Start ----------")
fruits = ["cherry", "banana", "apple"] # LIST: ordered, mutable
colors = ("red", "green", "blue") # TUPLE: ordered, immutable
profile = {"name": "Ana", "age": 21} # DICT: key-value, mutable
unique_ids = {101, 102, 103, 101} # SET: unordered, no

print("------Given Output-----")
print("List ", (fruits))
print("Tuple ", colors )
print("Dictionary ", profile)
print("Set ", unique_ids)

print("-----Updated Output-----")
# Adding new character in the list using .append
fruits.append("durian")
# Sorting the list using .sort
fruits.sort()
print("List 2.0 ", (fruits))

# Adding new color to the tuple using +
new_color = ("cyan",)
print("Tuple 2.0 ", colors + new_color )

# Adding course key and IT value in the dict using .update
profile.update({"course" : "IT"})
print("Dictionary 2.0 ", profile)

# Adding new values to sets (104 and 102) using .add
unique_ids.add(102)
unique_ids.add(104)
print("Set 2.0 ", unique_ids)
print(" ------------------------------------------- ")

print("----- Trip -----")
elements = ["fire", "water", "earth", "wind"]
balls = ("basketball", "baseball", "volleyball")
anime = {
    "Dragon Ball" : "Goku",
    "Naruto" : "Sasuke",
    "One Piece" : "Mugiwara"
}
set1 = {111, 222, 333, 444}

print("--------------- LIST ---------------")
print("Original Elements",elements)
elements.append("lightning")
elements.remove("fire")
print(f"Jessie's List: {elements}")

print("--------------- TUPLE ---------------")
print(f"Tuple: {balls}")
ball = tuple([input("Enter another ball: ")])
combined_balls = balls + ball
print(f"Jessie's Tuple but added another ball: {balls + ball}")
print(f"Tuple contains {len(combined_balls)} values" )

print("--------------- DICTIONARY ---------------")
print(f"Dictionary: {anime}")
new_key = input("Enter new anime title: ")
new_value = input("Enter anime character: ")
anime[new_key] = new_value
print(f"Jessie's Dictionary added one anime: {anime}" )
delete = input("What anime to delete: ")
if delete in anime:
    anime.pop(delete)
    print(f"{delete} has been deleted!")
else:
    print(f"No Anime Found!")
print(f"Jessie's Dictionary Deleted an anime: {anime}" )

print("--------------- SET ---------------")
print(f"Set: {set1}")
set2 = set()
for i in range(3):
    num = int(input("Enter another set: "))
    set2.add(num)
print(f"Set 2: {set2}")

onion = set1.union(set2)
print(f"Jessie's Set Intersection: {onion}")







