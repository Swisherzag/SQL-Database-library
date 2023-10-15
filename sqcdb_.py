import mysql.connector

# Establish the connection
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Close the connection
connection.close()