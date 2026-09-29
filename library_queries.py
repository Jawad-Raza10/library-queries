import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    price INTEGER,
    stock INTEGER
)
""")

books = [
    (1, "Data Science Basics", "Education", 1450, 10),
    (2, "Clean Code", "Programming", 1200, 8),
    (3, "The Silent Patient", "Fiction", 1350, 2),
    (4, "Python Crash Course", "Programming", 1100, 6),
    (5, "Atomic Habits", "Self Help", 950, 4),
    (6, "The Alchemist", "Fiction", 800, 7),
    (7, "Deep Work", "Self Help", 1050, 3),
    (8, "1984", "Fiction", 700, 2)
]

cur.execute("DELETE FROM books")

cur.executemany("""
INSERT INTO books
VALUES (?, ?, ?, ?, ?)
""", books)

conn.commit()

# (a) Books with price greater than 1000
print("Books above Rs.1000 (sorted):")

cur.execute("""
SELECT title, price
FROM books
WHERE price > 1000
ORDER BY price DESC
""")

for row in cur.fetchall():
    print(row)

# (b) Rename title using AS
print("\nBook titles using AS:")

cur.execute("""
SELECT title AS book_title
FROM books
""")

for row in cur.fetchall():
    print(row)

# (c) Fiction books with stock less than 5
print("\nLow-stock Fiction books:")

cur.execute("""
SELECT title, genre, price, stock
FROM books
WHERE genre = 'Fiction'
AND stock < 5
""")

for row in cur.fetchall():
    print(row)

conn.close()