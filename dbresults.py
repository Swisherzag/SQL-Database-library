import sqlite3

# Connect to the SQL database [replace my_database with your own SQL database]
connection = sqlite3.connect("my_database.db")

# Create a cursor object to interact with the database
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Execute SQL query to insert data into the table
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Walter", 55))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Jesse", 25))

# Commit the changes
connection.commit()

# Execute SQL query to retrieve data from the table
cursor.execute("SELECT * FROM users")

# Retrieve the results of the executed query
results = cursor.fetchall()

# Print the results
for row in results:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

# Close the connection to the SQL database
connection.close()
# This is used as a template from a few tutorials I've learned from over the last week. It should run as long as you have mysql and sqlite3