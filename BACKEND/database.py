import mysql.connector
import bcrypt

# Database connection setup
def create_connection():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="",  # Replace with your MySQL password
        database="interests"
    )
    return db_connection

# Function to validate the login credentials
def validate_user(username, password):
    db_connection = create_connection()
    db_cursor = db_connection.cursor()

    # Query to fetch the user by username
    query = "SELECT password FROM users WHERE username = %s"
    db_cursor.execute(query, (username,))
    result = db_cursor.fetchone()  # Fetch one row

    db_cursor.close()
    db_connection.close()

    if result:
        # The hashed password stored in the database
        stored_hashed_password = result[0]

        # Compare the entered password with the stored hashed password
        if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
            return True
        else:
            return False
    else:
        return False