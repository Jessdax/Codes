import sqlite3

# Connect or create database
conn = sqlite3.connect("moviehub.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")  # Enable foreign key constraints

# Drop existing tables if they exist
cursor.execute("DROP TABLE IF EXISTS Ratings")
cursor.execute("DROP TABLE IF EXISTS Movies")
cursor.execute("DROP TABLE IF EXISTS Genres")

# Create Genres Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Genres(
GenreID INTEGER PRIMARY KEY AUTOINCREMENT,
GenreName TEXT NOT NULL UNIQUE
)
''')

# Create Movies Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Movies(
MovieID INTEGER PRIMARY KEY AUTOINCREMENT,
Title TEXT NOT NULL,
Year INTEGER CHECK(Year >= 1900),
GenreID INTEGER,
FOREIGN KEY (GenreID) REFERENCES Genres(GenreID) ON DELETE CASCADE
)
''')

# Create Ratings Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Ratings(
RatingID INTEGER PRIMARY KEY AUTOINCREMENT,
MovieID INTEGER NOT NULL,
Score REAL CHECK(Score BETWEEN 0 AND 10),
FOREIGN KEY (MovieID) REFERENCES Movies(MovieID) ON DELETE CASCADE
)
''')

# Insert genres
cursor.executemany('INSERT INTO Genres(GenreName) VALUES(?)',
                [
                ("Action",),
                ("Comedy",),
                ("Drama",),
                ("Sci-Fi",),
                ("Mystery",),
                ("Cartoon",)
                ]
                )

# Insert movies
cursor.executemany(
    'INSERT INTO Movies(Title, Year, GenreID) VALUES(?, ?, ?)',
                [
                ("Inception", 2010, 4),
                ("The Dark Knight", 2008, 1),
                ("Forrest Gump", 1994, 3),
                ("The Hangover", 2009, 2),
                ("Chucky", 2010, 5),
                ("Dora", 2008, 6),
                ("FNAF 3", 2023, 5)
                
                ]
                )

# Insert ratings
cursor.executemany(
    'INSERT INTO Ratings(MovieID, Score) VALUES(?, ?)',
                [
                    (1, 8.8),
                    (2, 9.0),
                    (3, 8.8),
                    (4, 7.7),
                    (5, 6.5),
                    (6, 9.0),
                    (7, 8.0)
                ]
                )

cursor.execute('''
SELECT Movies.Title, Genres.GenreName, Ratings.Score
FROM Movies
JOIN Genres ON Movies.GenreID = Genres.GenreID
JOIN Ratings ON Movies.MovieID = Ratings.MovieID
ORDER BY Ratings.Score DESC
''')
print("---------------------------------------------------")
print("Movies with their genres and ratings")
print("---------------------------------------------------")
for row in cursor.fetchall():
        print("|",' : '.join(str(item) for item in row))
print("---------------------------------------------------")

cursor.execute('''
SELECT Movies.Title, Genres.GenreName, Ratings.Score
FROM Movies
JOIN Genres ON Movies.GenreID = Genres.GenreID
JOIN Ratings ON Movies.MovieID = Ratings.MovieID
WHERE Score > 8.0
ORDER BY Ratings.Score DESC
''')

print("---------------------------------------------------")
print("Movies with ratings of 8.0 and above")
print("---------------------------------------------------")
for row in cursor.fetchall():
    print("|",' : '.join(str(item) for item in row))
print("---------------------------------------------------")

cursor.execute('''
SELECT Movies.Title, Genres.GenreName, Ratings.Score
FROM Movies
JOIN Genres ON Movies.GenreID = Genres.GenreID
JOIN Ratings ON Movies.MovieID = Ratings.MovieID
WHERE Genres .GenreName = 'Action'
ORDER BY Ratings.Score DESC
''')

print("---------------------------------------------------")
print("Movies with Action Genre")
print("---------------------------------------------------")
for row in cursor.fetchall():
    print("|",' : '.join(str(item) for item in row))
print("---------------------------------------------------")

cursor.execute('CREATE INDEX IF NOT EXISTS idx_movie_title ON Movies(Title)')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_ratings_score ON Ratings(Score)')

conn.commit()
conn.close()
