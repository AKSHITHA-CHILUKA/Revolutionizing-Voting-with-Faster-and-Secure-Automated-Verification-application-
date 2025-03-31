import sqlite3

# Connect to SQLite database (it will create a new file if it doesn’t exist)
conn = sqlite3.connect('votes.db')
cursor = conn.cursor()

# Create a table for votes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS votes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        encrypted_vote TEXT
    )
''')

# Save (commit) the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")
