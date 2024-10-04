import sqlite3

# Connect to the database (creates it if it doesn't exist)
connection = sqlite3.connect('Knowledge.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create the knowledge table
cursor.execute('''
CREATE TABLE IF NOT EXISTS knowledge (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    query TEXT NOT NULL,
    response TEXT NOT NULL
)
''')

# Insert sample data
cursor.execute("INSERT INTO knowledge (query, response) VALUES (?, ?)", ("What is Eros?", "Eros is a travel assistant."))
cursor.execute("INSERT INTO knowledge (query, response) VALUES (?, ?)", ("How can Eros help me?", "Eros can provide travel suggestions and answer questions."))

# Commit changes and close the connection
connection.commit()
connection.close()

print("Database created and sample data inserted!")
