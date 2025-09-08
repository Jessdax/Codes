import sqlite3

try:
    conn = sqlite3.connect('schooleme.db')
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON")

    # Create tables if they don't exist
    cur.execute("CREATE TABLE IF NOT EXISTS Students (StudentID INTEGER PRIMARY KEY AUTOINCREMENT, StudentName TEXT NOT NULL, BirthYear INTEGER CHECK (BirthYear BETWEEN 2000 AND 2025))")
    cur.execute("CREATE TABLE IF NOT EXISTS Grades (GradeID INTEGER PRIMARY KEY AUTOINCREMENT, StudentID INTEGER, Subject TEXT, Grade INTEGER CHECK (Grade BETWEEN 0 AND 100), FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE)")

    # Get user input
    while True:
        name = input("Enter student's name: ")
        birth_year = int(input("Enter student's birth year (2000-2025): "))
        subject = input("Enter subject: ")
        grade = int(input("Enter grade (0-100): "))
        choose = input("Do you want to insert a new student and grade? (yes/no): ").strip().lower()


        # Insert student
        cur.execute("INSERT INTO Students (StudentName, BirthYear) VALUES (?, ?)", (name, birth_year))
        student_id = cur.lastrowid  # get the auto-generated StudentID

        # Insert grade for this student
        cur.execute("INSERT INTO Grades (StudentID, Subject, Grade) VALUES (?, ?, ?)", (student_id, subject, grade))

        conn.commit()
        print(f"Inserted {name} with grade {grade} in {subject}.")
    
        if choose == "yes":
            continue
        else:
            break

except sqlite3.Error as e:
    print("An error occurred:", e)

conn.close()

        
