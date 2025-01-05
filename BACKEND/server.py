from flask import Flask, request, jsonify, session
from flask_session import Session
import mysql.connector
from passlib.hash import argon2
import logging
from mysql.connector import errorcode
from argon2 import PasswordHasher

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# Session configuration
app.config['SECRET_KEY'] = 'PenpalApp'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False  # Ensure sessions are not permanent
Session(app)

# MySQL database connection setup
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="",  # Replace with your MySQL password
    database="penpaldb"
)

db_cursor = db_connection.cursor()

ph = PasswordHasher()  # Initialize Argon2 Password Hasher

@app.route("/sample", methods=['GET'])
def sample():
    return jsonify({"message": "I AM A SAMPLE GET ENDPOINT"}), 200

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
    interests = data.get('interests', [])  # Get the interests from the request

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

         # Save interests in the user_interests table
        for interest in interests:
            db_cursor.execute(
                "INSERT INTO user_interests (username, interest) VALUES (%s, %s)",
                (username, interest)
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

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    logging.debug(f"Login attempt for username: {username}")

    db_cursor.execute("SELECT id, password FROM users WHERE username = %s", (username,))
    result = db_cursor.fetchone()

    if result:
        user_id, stored_hashed_password = result
        logging.debug(f"Stored hash for user {username}: {stored_hashed_password}")

        try:
            ph.verify(stored_hashed_password, password)
            session['user_id'] = user_id
            session['username'] = username
            session.modified = True
            logging.debug(f"Session data after login: {dict(session)}")
            return jsonify({"message": f"Welcome back, {username}!", "user_id": user_id, "username": username}), 200
        except Exception as e:
            logging.error(f"Password verification failed: {e}")
            return jsonify({"message": "Invalid password."}), 400
    else:
        logging.error("Username not found")
        return jsonify({"message": "Invalid username."}), 400
    
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200

#USERNAME DISPLAY

@app.route('/get_username', methods=['GET'])
def get_username():
    logging.debug("Retrieving username from session")
    logging.debug(f"Session contents: {dict(session)}")
    username = session.get('username')
    
    if not username:
        app.logger.error("Username not found in session")
        return jsonify({"error": "Username not found in session"}), 401

    app.logger.debug(f"Username retrieved from session: {username}")
    return jsonify({"username": username}), 200

#AGE DISPLAY

@app.route('/get_user_age', methods=['GET'])
def get_user_age():
    username = request.args.get('username')
    
    if not username:
        return jsonify({"error": "Username is required"}), 400

    db_cursor.execute("SELECT age FROM users WHERE username = %s", (username,))
    result = db_cursor.fetchone()

    if result:
        age = result[0]
        return jsonify({"age": age}), 200
    else:
        return jsonify({"error": "User not found"}), 404
    
#GENDER DISPLAY

@app.route('/get_user_gender', methods=['GET'])
def get_user_gender():
    username = request.args.get('username')
    
    if not username:
        return jsonify({"error": "Username is required"}), 400

    db_cursor.execute("SELECT gender FROM users WHERE username = %s", (username,))
    result = db_cursor.fetchone()

    if result:
        gender = result[0]
        return jsonify({"gender": gender}), 200
    else:
        return jsonify({"error": "User not found"}), 404
    
#LOCATION DISPLAY

@app.route('/get_user_location', methods=['GET'])
def get_user_location():
    username = request.args.get('username')
    
    if not username:
        return jsonify({"error": "Username is required"}), 400

    db_cursor.execute("SELECT location FROM users WHERE username = %s", (username,))
    result = db_cursor.fetchone()

    if result:
        location = result[0]
        return jsonify({"location": location}), 200
    else:
        return jsonify({"error": "User not found"}), 404
    
# SOCIAL LINK DISPLAY

@app.route('/get_user_social_link', methods=['GET'])
def get_user_social_link():
    username = request.args.get('username')
    
    if not username:
        return jsonify({"error": "Username is required"}), 400

    db_cursor.execute("SELECT social_media_link FROM users WHERE username = %s", (username,))
    result = db_cursor.fetchone()

    if result:
        social_link = result[0]
        return jsonify({"social_link": social_link}), 200
    else:
        return jsonify({"error": "User not found"}), 404

#PREFERENCES DISPLAY

@app.route('/get_user_interests', methods=['GET'])
def get_user_interests():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    try:
        db_cursor.execute("SELECT interest FROM user_interests WHERE username = %s", (username,))
        interests = [row[0] for row in db_cursor.fetchall()]
        return jsonify({"interests": interests}), 200
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"error": "Database error"}), 500
    
#EMAIL DISPLAY

@app.route('/get_user_email', methods=['GET'])
def get_user_email():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    try:
        db_cursor.execute("SELECT gmail FROM users WHERE username = %s", (username,))
        result = db_cursor.fetchone()
        if result:
            return jsonify({"email": result[0]}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"error": "Database error"}), 

# DISPLAY ALL USERS 
@app.route('/get_all_users', methods=['GET'])
def get_all_users():
    try:
        db_cursor.execute("SELECT username, age, gender, location FROM users")
        users = db_cursor.fetchall()
        user_list = [{"username": user[0], "age": user[1], "gender": user[2], "location": user[3]} for user in users]
        return jsonify({"users": user_list}), 200
    except mysql.connector.Error as err:
        logging.error(f"Database error: {err}")
        return jsonify({"error": "Database error occurred. Please try again later."}), 500

@app.route('/get_one_user', methods=['GET'])
def get_one_user():
    current_username = request.args.get('current_username')
    logged_in_username = request.args.get('logged_in_username')
    displayed_users = request.args.getlist('displayed_users')  # Get the list of displayed users

    try:
        # Exclude the current user, logged-in user, and already displayed users
        placeholders = ', '.join(['%s'] * (len(displayed_users) + 2))
        query = f"SELECT username, age, gender, location FROM users WHERE username NOT IN ({placeholders}) LIMIT 1"
        params = [current_username, logged_in_username] + displayed_users
        db_cursor.execute(query, params)
        user = db_cursor.fetchone()
        if user:
            user_data = {"username": user[0], "age": user[1], "gender": user[2], "location": user[3]}
            
            # Fetch user preferences
            db_cursor.execute("SELECT interest FROM user_interests WHERE username = %s", (user[0],))
            preferences = [row[0] for row in db_cursor.fetchall()]
            user_data['preferences'] = preferences
            
            return jsonify({"user": user_data}), 200
        else:
            return jsonify({"error": "No user found"}), 404
    except mysql.connector.Error as err:
        logging.error(f"Database error: {err}")
        return jsonify({"error": "Database error occurred. Please try again later."}), 500

@app.route('/send_friend_request', methods=['POST'])
def send_friend_request():
    data = request.get_json()
    from_user = data.get('from_user')
    to_user = data.get('to_user')

    if not from_user or not to_user:
        return jsonify({"error": "Both from_user and to_user are required"}), 400

    try:
        db_cursor.execute(
            "INSERT INTO friend_requests (from_user, to_user, status) VALUES (%s, %s, 'pending')",
            (from_user, to_user)
        )
        db_connection.commit()
        return jsonify({"message": "Friend request sent successfully"}), 201
    except mysql.connector.Error as err:
        logging.error(f"Database error: {err}")
        return jsonify({"error": "Database error occurred. Please try again later."}), 500
    
@app.route('/get_pending_friend_requests', methods=['GET'])
def get_pending_friend_requests():
    username = request.args.get('username')
    
    if not username:
        return jsonify({"error": "Username is required"}), 400

    try:
        db_cursor.execute("SELECT from_user FROM friend_requests WHERE to_user = %s AND status = 'pending'", (username,))
        pending_requests = [row[0] for row in db_cursor.fetchall()]
        return jsonify({"pending_requests": pending_requests}), 200
    except mysql.connector.Error as err:
        logging.error(f"Database error: {err}")
        return jsonify({"error": "Database error occurred. Please try again later."}), 500

@app.route('/accept_friend_request', methods=['POST'])
def accept_friend_request():
    data = request.get_json()
    from_user = data.get('from_user')
    to_user = data.get('to_user')

    if not from_user or not to_user:
        return jsonify({"error": "Both from_user and to_user are required"}), 400

    try:
        db_cursor.execute(
            "UPDATE friend_requests SET status = 'accepted' WHERE from_user = %s AND to_user = %s",
            (from_user, to_user)
        )
        db_connection.commit()
        return jsonify({"message": "Friend request accepted successfully"}), 200
    except mysql.connector.Error as err:
        logging.error(f"Database error: {err}")
        return jsonify({"error": "Database error occurred. Please try again later."}), 500
    
@app.route('/get_accepted_friends', methods=['GET'])
def get_accepted_friends():
    username = request.args.get('username')
    
    if not username:
        return jsonify({"error": "Username is required"}), 400

    try:
        db_cursor.execute("SELECT from_user FROM friend_requests WHERE to_user = %s AND status = 'accepted'", (username,))
        accepted_friends = [row[0] for row in db_cursor.fetchall()]
        return jsonify({"accepted_friends": accepted_friends}), 200
    except mysql.connector.Error as err:
        logging.error(f"Database error: {err}")
        return jsonify({"error": "Database error occurred. Please try again later."}), 500

if __name__ == '__main__':
    app.run(debug=True)