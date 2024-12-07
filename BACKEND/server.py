from flask import Flask, request, jsonify
import bcrypt
import mysql.connector

app = Flask(__name__)

# MySQL database connection setup
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="",  # Replace with your MySQL password
    database="interests"
)

db_cursor = db_connection.cursor()

@app.route('/login', methods=['POST'])
def login():
    # Get JSON data from frontend
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Fetch the hashed password for the provided username
    db_cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = db_cursor.fetchone()

    if result:
        stored_hashed_password = result[0].encode('utf-8')  # Convert str back to bytes

        # Compare the entered password with the stored hashed password
        if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
            # Check for user interests after successful login
            db_cursor.execute("SELECT interest FROM user_interests WHERE username = %s", (username,))
            interests = db_cursor.fetchall()

            if not interests:
                return jsonify({"message": "You haven't selected your interests yet."}), 200

            return jsonify({"message": f"Welcome back, {username}!", "username": username}), 200
        else:
            return jsonify({"message": "Invalid password."}), 400
    else:
        return jsonify({"message": "Invalid username."}), 400

if __name__ == '__main__':
    app.run(debug=True)