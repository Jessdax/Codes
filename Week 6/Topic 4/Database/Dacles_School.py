import sqlite3

try:
    conn = sqlite3.connect('school.db')  # Open or create the database file
    cur = conn.cursor() 

    cur.execute("PRAGMA foreign_keys = ON")  # Enable foreign key constraints

    cur.execute("DROP TABLE IF EXISTS Students")  # Drop Students table if it exists
    cur.execute("DROP TABLE IF EXISTS Grades")  # Drop Grades table if it exists

    cur.execute(''' CREATE TABLE IF NOT EXISTS Students (
StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
StudentName TEXT NOT NULL,
BirthYear INTEGER CHECK (BirthYear BETWEEN 2000 and 2025)
    )   
                ''')

    cur.execute(''' CREATE TABLE IF NOT EXISTS Grades (
GradeID INTEGER PRIMARY KEY AUTOINCREMENT,
StudentID INTEGER,
Subject TEXT,
Grade INTEGER CHECK (Grade BETWEEN 0 and 100),
FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE
    )   
                ''')
    
    cur.execute("INSERT INTO Students (StudentName, BirthYear) VALUES ('Jessie', 2003)")
    cur.execute("INSERT INTO Students (StudentName, BirthYear) VALUES ('Asta', 2004)")
    cur.execute("INSERT INTO Students (StudentName, BirthYear) VALUES ('Conan', 2005)")
    cur.execute("INSERT INTO Students (StudentName, BirthYear) VALUES ('Sun', 2023)")

    cur.execute("INSERT INTO Grades (StudentID, Subject, Grade) VALUES (1,'Math', 85)")
    cur.execute("INSERT INTO Grades (StudentID, Subject, Grade) VALUES (2,'Science', 90)")
    cur.execute("INSERT INTO Grades (StudentID, Subject, Grade) VALUES (3,'PE', 91)")
    cur.execute("INSERT INTO Grades (StudentID, Subject, Grade) VALUES (4,'English', 100)")

    cur.execute("CREATE INDEX IF NOT EXISTS StudentID ON Grades (StudentID)")

    cur.execute('''
SELECT Students.StudentName, Grades.Subject, Grades.Grade
FROM Students
JOIN Grades ON Students.StudentID = Grades.StudentID
    ''')

    print("---------------------------------------------------")
    print("|Name    Subject  Grade                            |")
    print("---------------------------------------------------")

    for row in cur.fetchall():
        print("|",' : '.join(str(item) for item in row))


    conn.commit()  # Save all changes permanently
    conn.close()  # Close the database connection
    print("|==================================================")
    print("|School database created with Students and Grades!|")

    print("---------------------------------------------------")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")