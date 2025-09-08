import sqlite3 # Load SQLite library for database operations
conn = sqlite3.connect('school.db') # Open or create the database file
cursor = conn.cursor() # Create a controller to manage commands

# Create Students table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
StudentID TEXT PRIMARY KEY,
StudentName TEXT
)
''')

# Create Subjects table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Subjects (
SubjectCode TEXT PRIMARY KEY,
SubjectName TEXT
)
''')

# Insert sample students
cursor.execute("INSERT INTO Students VALUES ('S001', 'Anna Reyes')")
cursor.execute("INSERT INTO Students VALUES ('S002', 'Ben Castillo')")
cursor.execute("INSERT INTO Students VALUES ('S003', 'Carla Dominguez')")

# Insert sample subjects
cursor.execute("INSERT INTO Subjects VALUES ('MATH101', 'Basic Mathematics')")
cursor.execute("INSERT INTO Subjects VALUES ('ENG101', 'English Grammar')")

conn.commit() # Save all changes permanently
conn.close() # Close the database connection
print("School database created with Students and Subjects!")
