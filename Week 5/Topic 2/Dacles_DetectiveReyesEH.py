# Part 1
class BlankNameError(Exception):
    pass

class BlankLocationError(Exception):
    pass

class DuplicateWitnessError(Exception):
    pass

# Part 2
def investigate_case_v2(statements):
    processed_names = set()
    error_count = 0
    
    valid_rooms = ["Kitchen", "Library", "Garden", "Garage"]

    for person, room in statements.items():
        try:
            if person.strip() == "":
                raise BlankNameError("Error: Name cannot be blank.")
        
            if room.strip() == "":
                raise BlankLocationError("Error: Location cannot be blank.")
        
            if person in processed_names:
                raise DuplicateWitnessError(f"Error: Duplicate witness entry for {person}.")
            
            print(f"🕵 Processing: {person} saw the victim in the {room}.")
            processed_names.add(person)

            if room not in valid_rooms:
                raise Exception(f"Invalid room: {room}.")

        except Exception as e:
            print(f"⚠️ Skipped entry: {e}")
            error_count += 1

    print("✅ Investigation complete.")
    print(f"⛔ Total skipped entries: {error_count}")

try:
    witness_statements = [
        ("Butler" , "Kitchen"),
        (" " , "Garden"),
        ("Chef" , " "),
        ("Maid" , "Library"),
        ("Butler" , "Attic"),
        ("Driver" , "Garage"),
    ]
    investigate_case_v2(witness_statements)

except Exception as e:
    print("ERROR:", e)




