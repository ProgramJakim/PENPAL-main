from flask import Flask, request, jsonify
import mysql.connector
from passlib.hash import argon2
import logging
from mysql.connector import errorcode
from argon2 import PasswordHasher


app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# MySQL database connection setup
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="",  # Replace with your MySQL password
    database="penpaldb"
)

db_cursor = db_connection.cursor()

@app.route("/sample", methods=['GET'])
def sample():
    return jsonify({"message":"I AM A SAMPLE GET ENDPOINT"}), 200

ph = PasswordHasher()  # Initialize Argon2 Password Hasher

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    print("Signup route accessed")  # Debug line to check if route is hit
    username = data.get('username')
    password = data.get('password')
    age = data.get('age')
    location = data.get('location')
    gender = data.get('gender')
    social_media_link = data.get('social_media_link', None)
    gmail = data.get('gmail', None)  # New field for Gmail account

    if not username or not password or not age or not location or not gender or not gmail:
        logging.error("Error: Missing required fields.")
        return jsonify({"error": "Missing required fields"}), 400

    if not isinstance(age, int) or age < 13:
        return jsonify({"error": "Age must be a valid number and at least 13"}), 400
    
    if not location or not isinstance(location, str):
        return jsonify({"error": "Location is required and must be a string"}), 400

    password_issue = validate_password(password)
    if password_issue:
        logging.error("Error: Password issue -", password_issue)
        return jsonify({"error": password_issue}), 400

    hashed_password = argon2.hash(password)

    db_cursor.execute("SELECT password FROM users WHERE LOWER(username) = LOWER(%s)", (username.lower(),))
    if db_cursor.fetchone():
        logging.error("Error: Username already exists.")
        return jsonify({"error": "Username already exists"}), 400

    try:
        db_cursor.execute(
            "INSERT INTO users (username, age, location, gender, password, social_media_link, gmail) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (username, age, location, gender, hashed_password, social_media_link, gmail)
        )
        db_connection.commit()
        logging.info("User account created successfully!")
        print(f"Hashed password for {username}: {hashed_password}")
        return jsonify({"message": "Account created successfully!"}), 201
    except mysql.connector.Error as err:
        logging.error(f"Database error: {err}")
        return jsonify({"error": "Database error occurred. Please try again later."}), 500


def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return "Password must include at least one number."
    if not any(char.isupper() for char in password):
        return "Password must include at least one uppercase letter."
    if not any(char in "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|" for char in password):
        return "Password must include at least one special character."
    return None

ph = PasswordHasher()  # Initialize Argon2 Password Hasher


@app.route('/login', methods=['POST'])
def login():
    # Get JSON data from frontend
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    logging.debug(f"Login attempt for username: {username}")

    # Fetch the hashed password for the provided username
    db_cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = db_cursor.fetchone()

    if result:
        stored_hashed_password = result[0]
        logging.debug(f"Stored hash for user {username}: {stored_hashed_password}")

        try:
            # Verify password using Argon2
            ph.verify(stored_hashed_password, password)
            return jsonify({"message": f"Welcome back, {username}!", "username": username, "accessToken": "sample"}), 200
        except Exception as e:
            logging.error(f"Password verification failed: {e}")
            return jsonify({"message": "Invalid password."}), 400
    else:
        logging.error("Username not found")
        return jsonify({"message": "Invalid username."}), 400
    

if __name__ == '__main__':
    app.run(debug=True)

