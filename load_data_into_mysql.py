import mysql.connector
import json

# Connect to the MySQL server
db = mysql.connector.connect(
    host="localhost",
    user="", # username
    password="", #password
)

# Create a cursor object
cursor = db.cursor()

# Create the database
database_name = "covidGhana"
query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
cursor.execute(query)

# Use the database
db.database = database_name

# Create the table
table_name = "covid"
query = f"CREATE TABLE IF NOT EXISTS {table_name} (`key` VARCHAR(255) PRIMARY KEY, `value` VARCHAR(255))"
cursor.execute(query)

# Read the contents of the JSON file
with open('cleaned_data.json', 'r') as f:
    data = json.load(f)

# Loop through the data and insert each record into the database
for key, value in data.items():
    query = f"INSERT INTO {table_name} (`key`, `value`) VALUES ('{key}', '{value}') ON DUPLICATE KEY UPDATE `value`='{value}'"
    cursor.execute(query)

# Loading contents of your database
query2 = "SELECT * FROM covid"
cursor.execute(query2)

# Fetch all rows and display the content
rows = cursor.fetchall()
for row in rows:
    print(row)
# Commit the transaction
db.commit()

# Close the cursor and connection
cursor.close()
db.close()