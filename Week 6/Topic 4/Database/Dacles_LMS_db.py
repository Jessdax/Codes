import sqlite3

conn = sqlite3.connect('school_lms.db')  # Open or create the database file
cursor = conn.cursor()  # Create a controller to manage commands

conn.execute("DROP TABLE IF EXISTS Students")  # Drop Students table if it exists
conn.execute("DROP TABLE IF EXISTS Subjects")  # Drop Subjects table if it exists
conn.execute("DROP TABLE IF EXISTS Teachers")  # Drop Teachers table if it exists

# Create Students table
cursor.execute(''' Create Table IF NOT EXISTS Students (
    StudentID VARCHAR PRIMARY KEY,
    StudentName VARCHAR NOT NULL,
    StudentContactNumber INTEGER UNIQUE NOT NULL,
    SubjectCode VARCHAR,
    FOREIGN KEY (SubjectCode) REFERENCES Subjects(SubjectCode)
)''')

cursor.execute("INSERT INTO Students VALUES ('SSJ1', 'Naruto', 916545647, 'CS 002')")
cursor.execute("INSERT INTO Students VALUES ('SSJ2', 'Sasuke', 949887465, 'PE 900')")
cursor.execute("INSERT INTO Students VALUES ('SSJ3', 'Sakura', 974897647, 'THESIS 100')")

cursor.execute(''' Create Table IF NOT EXISTS Subjects (
    SubjectCode VARCHAR PRIMARY KEY,
    SubjectName VARCHAR NOT NULL,
    TeacherID VARCHAR,
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID)
)''')

cursor.execute("INSERT INTO Subjects VALUES ('CS 002', 'Introduction to Hacking', 'SENSEI 001')")
cursor.execute("INSERT INTO Subjects VALUES ('PE 900', 'Taijutsu Training', 'SENSEI 002')")
cursor.execute("INSERT INTO Subjects VALUES ('THESIS 100', 'Reality or Dream', 'SENSEI 003')")

cursor.execute(''' Create Table IF NOT EXISTS Teachers (
        TeacherID VARCHAR PRIMARY KEY,
        TeacherName VARCHAR NOT NULL,
        SubjectCode VARCHAR NOT NULL,
        FOREIGN KEY (SubjectCode) REFERENCES Subjects(SubjectCode)
)''')

cursor.execute("INSERT INTO Teachers VALUES ('SENSEI 001', 'Gojo Satoru', 'CS 002')")
cursor.execute("INSERT INTO Teachers VALUES ('SENSEI 002', 'Hatake Kakashi', 'PE 900')")
cursor.execute("INSERT INTO Teachers VALUES ('SENSEI 003', 'Rayleigh', 'THESIS 100')")


conn.commit()  # Save all changes permanently
conn.close()  # Close the database connection

print("School LMS database created with Students, Subjects, and Teachers!")