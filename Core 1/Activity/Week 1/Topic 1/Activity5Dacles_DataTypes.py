# Student Profile
# Prompt the user
print("=" * 35)
print("Enter your information")
print("=" * 35)
f_name = str(input("Enter your Full Name: "))
age = int(input("Enter your Age: "))
course = str(input("Enter your Course: "))
enrollment = input("Are you currently Enrolled?(yes or no): ")
if enrollment == "yes":
    result = True
elif enrollment == "no":
    result = False
else:
    result ="Invalid Answer!"
# Another trick for boolean, is_enrolled = enrollment.lower() == "yes"
ave_grade = float(input("Enter your Average Grade: "))
proj = int(input("Completed Project: "))
print("=" * 35)
print("\n")

# Output
print("=" * 35)
print("Student Profile Summary:")
print("=" * 35)
print(f"Fullname: {f_name}")
print(f"Age: {age}")
print(f"Course: {course}")
print(f"Enrolled: {result}")
print(f"Average Grade: {ave_grade}")
print(f"Completed Project: {proj}")
print("=" * 35)

# The system records the students information
# prints the output base on his/her given data