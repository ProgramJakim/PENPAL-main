import mysql.connector  
import networkx as nx
import bcrypt
import sys
import msvcrt 
import random

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="",  # Replace with your MySQL password
    database="interests"
)

db_cursor = db_connection.cursor()

# Graph for users and friendships
class SocialMediaGraph: 
    def __init__(self):
        self.graph = nx.Graph()
        self._initialize_graph()

    def _initialize_graph(self):
        """Initialize graph nodes and edges from MySQL database."""
        db_cursor.execute("SELECT username FROM users")
        users = db_cursor.fetchall()
        for user in users:
            self.graph.add_node(user[0])

        db_cursor.execute("SELECT user1, user2 FROM friendships")
        friendships = db_cursor.fetchall()
        for user1, user2 in friendships:
            self.graph.add_edge(user1, user2)

    def classify_user_generation(self, age):
        """Classify user into a generation based on age."""
        if 12 <= age <= 27:
            return "Generation Z (Gen Z)"
        elif 28 <= age <= 43:
            return "Millennials (Gen Y)"
        elif 44 <= age <= 59:
            return "Generation X (Gen X)"
        elif 60 <= age <= 78:
            return "Baby Boomers"
        else:
            return "Age out of range"

    def view_friend_recommendations_based_on_age(self, username):
        """Find and recommend friends based on the user's generation."""
        db_cursor.execute("SELECT age FROM users WHERE username = %s", (username,))
        result = db_cursor.fetchone()
        if not result:
            print(f"User {username} does not exist.")
            return []
        
        age = result[0]
        generation = self.classify_user_generation(age)
        print(f"\nREGISTERED USER is: {generation}")

        # Find friends of the same generation
        db_cursor.execute("SELECT username, age FROM users WHERE username != %s", (username,))
        users = db_cursor.fetchall()

        same_generation_friends = []
        for user in users:
            user_username, user_age = user
            if self.classify_user_generation(user_age) == generation:
                same_generation_friends.append(user_username)

        # Output friend recommendations
        print(f"Friend recommendations for {username} based on {generation}: {', '.join(same_generation_friends)}")
        return same_generation_friends

    def find_people(self, username, count=5, gender_filter=None):
        """
        Find random registered users who are not friends with the logged-in user,
        with an optional gender filter.
        """
        # Check if the user exists
        db_cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
        if not db_cursor.fetchone():
            print(f"User {username} does not exist.")
            return []

        # Get friends of the user
        db_cursor.execute(""" 
            SELECT user2 FROM friendships WHERE user1 = %s
            UNION 
            SELECT user1 FROM friendships WHERE user2 = %s
        """, (username, username))
        friends = {row[0] for row in db_cursor.fetchall()}
        friends.add(username)  # Include the user themselves to exclude them

        # Get all registered users
        db_cursor.execute("SELECT username, gender, age FROM users")
        all_users = db_cursor.fetchall()

        # Filter users based on gender
        if gender_filter:
            all_users = [user for user in all_users if user[1].lower() == gender_filter.lower()]
        else:
            all_users = [user for user in all_users]

        # Exclude friends and the user themselves
        non_friends = list(set(all_users) - friends)

        # Randomly select up to count users
        random_users = random.sample(non_friends, min(count, len(non_friends)))
        print(f"\nRecommended people to connect with: {', '.join([user[0] for user in random_users])}")

        return [user[0] for user in random_users]

    def add_user(self, username, user_data):
        """Add a new user to the system."""
        db_cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
        if db_cursor.fetchone():
            print("Username already exists.")
            return False

        db_cursor.execute(
            "INSERT INTO users (username, age, location, gender, password, social_media_link) VALUES (%s, %s, %s, %s, %s, %s)",
            (username, user_data["age"], user_data["location"], user_data["gender"], user_data["password"], user_data["social_media_link"] )
        )
        db_connection.commit()
        self.graph.add_node(username)
        return True

    def send_friend_request(self, from_user, to_user):
        db_cursor.execute("SELECT username FROM users WHERE username = %s", (to_user,))
        if not db_cursor.fetchone():
            print(f"User {to_user} does not exist.")
            return
        if from_user == to_user:
            print("You cannot send a friend request to yourself.")
            return

        db_cursor.execute("SELECT * FROM friend_requests WHERE from_user = %s AND to_user = %s", (from_user, to_user))
        if db_cursor.fetchone():
            print(f"Friend request already s  to {to_user}.")
            return

        db_cursor.execute(
            "INSERT INTO friend_requests (from_user, to_user, status) VALUES (%s, %s, 'pending')",
            (from_user, to_user)
        )
        db_connection.commit()
        print(f"{from_user} sent a friend request to {to_user}")

    def accept_friend_request(self, user, from_user):
        db_cursor.execute("SELECT * FROM friend_requests WHERE from_user = %s AND to_user = %s", (from_user, user))
        if not db_cursor.fetchone():
            print("No friend request found from this user.")
            return

        db_cursor.execute("UPDATE friend_requests SET status = 'accepted' WHERE from_user = %s AND to_user = %s", (from_user, user))
        db_cursor.execute(
            "INSERT INTO friendships (user1, user2) VALUES (%s, %s), (%s, %s)",
            (user, from_user, from_user, user)
        )
        db_connection.commit()
        print(f"{user} accepted the friend request from {from_user}")

    def decline_friend_request(self, user, from_user):
        db_cursor.execute("SELECT * FROM friend_requests WHERE from_user = %s AND to_user = %s", (from_user, user))
        if not db_cursor.fetchone():
            print("No friend request found from this user.")
            return

        db_cursor.execute("UPDATE friend_requests SET status = 'rejected' WHERE from_user = %s AND to_user = %s", (from_user, user))
        db_connection.commit()
        print(f"{user} declined the friend request from {from_user}")

    def get_friend_requests(self, user):
        db_cursor.execute("SELECT from_user, status FROM friend_requests WHERE to_user = %s", (user,))
        requests = db_cursor.fetchall()
        return [{"from_user": row[0], "status": row[1]} for row in requests]

    def recommend_friends(self, username):
        if username not in self.graph:
            print(f"User {username} is not in the system.")
            return {}

        friends = set(self.graph.neighbors(username))
        recommendations = {}

        for friend in friends:
            for fof in self.graph.neighbors(friend):
                if fof != username and fof not in friends:
                    if fof not in recommendations:
                        mutual_count = len(set(self.graph.neighbors(fof)).intersection(friends))
                        recommendations[fof] = mutual_count

        sorted_recommendations = dict(sorted(recommendations.items(), key=lambda item: item[1], reverse=True))

        return sorted_recommendations
    
    def recommend_friends_by_location(self, username):
        # Check if the user exists in the database
        db_cursor.execute("SELECT location FROM users WHERE username = %s", (username,))
        result = db_cursor.fetchone()
        if not result:
            print(f"User {username} does not exist.")
            return []

        user_location = result[0]

        # Fetch users in the same location but not already friends
        db_cursor.execute("""
            SELECT username FROM users
            WHERE location = %s AND username != %s
            AND username NOT IN (
                SELECT user2 FROM friendships WHERE user1 = %s
                UNION
                SELECT user1 FROM friendships WHERE user2 = %s
            )
        """, (user_location, username, username, username))
        
        potential_friends = [row[0] for row in db_cursor.fetchall()]
        
        if potential_friends:
            print(f"Recommended friends based on location ({user_location}): {', '.join(potential_friends)}")
        else:
            print(f"No friend recommendations found for {username} based on location.")
        
        return potential_friends
    
    def recommend_friends_by_interests(self, username):
        # Fetch the user's interests
        db_cursor.execute("SELECT interest FROM user_interests WHERE username = %s", (username,))
        user_interests = {row[0] for row in db_cursor.fetchall()}
    
        if not user_interests:
            print("No interests found for the user. Encourage the user to select interests.")
            return []
    
        # Fetch all other users' interests and exclude current friends
        db_cursor.execute("""
            SELECT u.username, ui.interest 
            FROM users u
            JOIN user_interests ui ON u.username = ui.username
            WHERE u.username != %s 
            AND u.username NOT IN (
                SELECT user2 FROM friendships WHERE user1 = %s
                UNION
                SELECT user1 FROM friendships WHERE user2 = %s
            )
        """, (username, username, username))
    
        potential_friends = {}
        for other_user, interest in db_cursor.fetchall():
            if other_user not in potential_friends:
                potential_friends[other_user] = set()
            potential_friends[other_user].add(interest)
    
        # Calculate shared interests
        recommendations = {
            user: user_interests.intersection(interests)
            for user, interests in potential_friends.items()
        }
    
        # Filter out users with no shared interests and sort by the number of shared interests
        sorted_recommendations = {
        user: shared_interests
        for user, shared_interests in sorted(recommendations.items(), key=lambda item: len(item[1]), reverse=True)
        if shared_interests
        }
    
        if sorted_recommendations:
            print(f"Friend recommendations for {username} based on shared interests:")
            for user, shared_interests in sorted_recommendations.items():
                print(f"User: {user}, Shared Interests: {', '.join(shared_interests)}")
        else:
            print("No friend recommendations found based on shared interests.")
    
        return sorted_recommendations


    
    def view_all_friends(self, username):
        """View all friends of a user from the database."""
        # Check if the user exists in the database
        db_cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
        if not db_cursor.fetchone():
            print(f"User {username} does not exist.")
            return []

        # Retrieve friends from the friendships table
        db_cursor.execute("""
            SELECT user2 FROM friendships WHERE user1 = %s
            UNION
            SELECT user1 FROM friendships WHERE user2 = %s
        """, (username, username))
        
        friends = [row[0] for row in db_cursor.fetchall()]

        if friends:
            print(f"Friends of {username}: {', '.join(friends)}")
        else:
            print(f"{username} has no friends yet.")
        
        return friends
    
    def view_all_users(self):
        """Display all registered usernames."""
        try:
            db_cursor.execute("SELECT username FROM users")
            users = db_cursor.fetchall()
            print("\nAll Registered Users:")
            for user in users:
                print(user[0])
        except mysql.connector.Error as err:
            print(f"Error fetching users: {err}")

def validate_password(password):
    """Check if the password is strong enough."""
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return "Password must include at least one number."
    if not any(char.isupper() for char in password):
        return "Password must include at least one uppercase letter."
    if not any(char in "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|" for char in password):
        return "Password must include at least one special character."
    return None

# Account creation and login functions
def create_account():
    """Create a new account with user inputs and validations."""
    
    username = input("Enter username: ").strip()

    # Loop until a strong password is provided
    while True:
        password = input("Enter password: ").strip()

        # Validate password strength
        password_issue = validate_password(password)
        if password_issue:
            print(f"Password issue: {password_issue}")
            print("Please try again with a stronger password.")
        else:
            break  # Exit loop if the password is valid

    
    #age requirement
    while True:
        try:
            # Get and process the age input
            age = int(input("Enter age: ").strip())  # Convert to int and strip any extra spaces
        except ValueError:
            # Handle non-numeric inputs
            print("Invalid input! Please enter a valid number for your age.")
            continue  # Re-prompt if the input is invalid

        # Validate ages
        if age < 18:
            print("You must be at least 18 years old to create an account.")
        elif age >= 100:
            print("The age you entered is not valid. Please enter a valid age less than 100 years.")
        else:
            break  # Exit the loop when the age is valid

    location = input("Enter location: ").strip()
    
    while True:
        gender = input("Enter gender (Male/Female): ").strip()

        # Check if the gender is valid
        if gender.lower() not in ["male", "female"]:
            print("Invalid choice! Please enter 'Male' or 'Female'.")
        else:
            break  # Exit loop if valid choice

    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')  # Decode to str

    sm_graph = SocialMediaGraph()
    user_data = {
        "age": age,
        "location": location,
        "gender": gender,
        "password": hashed_password  # Store hashed password
    }

    social_media_link = input("Enter your social media account link (optional): ").strip()
    user_data["social_media_link"] = social_media_link

    terms = input("Do you agree to the Terms and Conditions? (yes/no): ").lower()
    if terms != "yes":
        print("You must agree to the Terms and Conditions to create an account.")
        return

    if sm_graph.add_user(username, user_data):
        print(f"Account for {username} created successfully.")
        print("Let's set up your interests!")
        choose_interests(username)
    else:
        print("Account creation failed.")

def choose_interests(username):
    predefined_interests = [
        "Sports", "Music", "Movies", "Technology", "Travel", 
        "Books", "Gaming", "Cooking", "Fitness", "Art", 
        "Fashion", "Science", "Photography", "Education", "Business"
    ]
    
    print("\n--- Choose Your Interests ---")
    print("Select at least 5 interests from the list below:")
    for i, interest in enumerate(predefined_interests, 1):
        print(f"{i}. {interest}")
    
    selected_interests = []
    while len(selected_interests) < 5:
        try:
            choice = int(input(f"Select interest ({len(selected_interests)+1}/5): "))
            if choice < 1 or choice > len(predefined_interests):
                print("Invalid choice. Please select a valid number.")
            elif predefined_interests[choice - 1] in selected_interests:
                print("You have already selected this interest.")
            else:
                selected_interests.append(predefined_interests[choice - 1])
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Add selected interests to the database
    for interest in selected_interests:
        db_cursor.execute(
            "INSERT INTO user_interests (username, interest) VALUES (%s, %s)", 
            (username, interest)
        )

    db_connection.commit()
    print(f"Your interests have been saved: {', '.join(selected_interests)}")

def masked_input(prompt=""):
    """
    Custom function to accept input while showing '*' for each character typed.
    Works on Windows (using msvcrt).
    """
    print(prompt, end="", flush=True)
    
    password = []
    while True:
        char = msvcrt.getch()  # Get a single character from the user
        if char == b'\r':  # Enter key pressed (Carriage return)
            break
        elif char == b'\x08':  # Backspace key pressed
            if password:
                password.pop()
                sys.stdout.write("\b \b")  # Erase the last '*' on the screen
                sys.stdout.flush()
        else:
            password.append(char.decode())  # Append the character to the password list
            sys.stdout.write('')  # Mask the character with ''
            sys.stdout.flush()
    
    print()  # Move to the next line after password input
    return ''.join(password)

# login function with custom masked password
def login(username, password):
    # Fetch the hashed password for the provided username
    db_cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = db_cursor.fetchone()

    if result:
        stored_hashed_password = result[0].encode('utf-8')  # Convert str back to bytes

        # Compare the entered password with the stored hashed password
        if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
            print(f"Welcome back, {username}!")

            # Check for user interests after successful login
            db_cursor.execute("SELECT interest FROM user_interests WHERE username = %s", (username,))
            interests = db_cursor.fetchall()

            if not interests:
                print("You haven't selected your interests yet. Let's do that now!")
                choose_interests(username)

            return username  
        else:
            print("Invalid password.")  
    else:
        print("Invalid username.")  

    return None  


# FOR SETTING OPTION
def edit_username(current_username):
    new_username = input("Enter your new username: ").strip()

    # Check if the new username is already taken
    db_cursor.execute("SELECT username FROM users WHERE username = %s", (new_username,))
    if db_cursor.fetchone():
        print("This username is already taken. Please try a different one.")
        return current_username

    try:
        # Ensure there is no pending transaction
        print("Resetting transaction state...")
        db_connection.commit()  # Commit any previous transaction, if active

        print("Starting new transaction...")
        db_connection.start_transaction()

        # Update the username in the users table
        print("Updating users table...")
        db_cursor.execute("UPDATE users SET username = %s WHERE username = %s", (new_username, current_username))

        # Update the username in dependent tables
        print("Updating user_interests table...")
        db_cursor.execute("UPDATE user_interests SET username = %s WHERE username = %s", (new_username, current_username))

        print("Updating friendships table...")
        db_cursor.execute("UPDATE friendships SET user1 = %s WHERE user1 = %s", (new_username, current_username))
        db_cursor.execute("UPDATE friendships SET user2 = %s WHERE user2 = %s", (new_username, current_username))

        # Commit the transaction
        print("Committing transaction...")
        db_connection.commit()
        print("Username updated successfully.")
        return new_username
    except mysql.connector.Error as e:
        # Rollback if any part of the transaction fails
        db_connection.rollback()
        print(f"An error occurred while updating the username: {e}")
        return current_username

# FOR SETTING OPTION
def edit_password(username):
    while True:
        new_password = input("Enter your new password: ").strip()
        password_issue = validate_password(new_password)
        if password_issue:
            print(f"Password issue: {password_issue}")
        else:
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            db_cursor.execute("UPDATE users SET password = %s WHERE username = %s", (hashed_password, username))
            db_connection.commit()
            print("Password updated successfully.")
            break
# FOR SETTING OPTION
def edit_social_media_link(username):
    new_link = input("Enter your new social media link: ").strip()
    db_cursor.execute("UPDATE users SET social_media_link = %s WHERE username = %s", (new_link, username))
    db_connection.commit()
    print("Social media link updated successfully.")

# FOR SETTING OPTION
def delete_account(username):
    confirm = input("Are you sure you want to delete your account? This action cannot be undone. (yes/no): ").lower()
    if confirm == "yes":
        try:
            print("Deleting related data in dependent tables...")

            # Delete from user_interests
            db_cursor.execute("DELETE FROM user_interests WHERE username = %s", (username,))

            # Delete from friendships
            db_cursor.execute("DELETE FROM friendships WHERE user1 = %s", (username,))
            db_cursor.execute("DELETE FROM friendships WHERE user2 = %s", (username,))

            # Finally, delete the user
            print("Deleting user account...")
            db_cursor.execute("DELETE FROM users WHERE username = %s", (username,))

            # Commit the transaction
            db_connection.commit()
            print("Account deleted successfully.")
            return True
        except mysql.connector.Error as e:
            # Rollback in case of any errors
            db_connection.rollback()
            print(f"An error occurred while deleting the account: {e}")
            return False
    else:
        print("Account deletion canceled.")
        return False






# Interactive menu for user actions
def main():
    logged_in_user = None
    sm_graph = SocialMediaGraph()

    while True:
        print("\n--- PENPAL: Social Media Friend Recommendation System ---")
        if not logged_in_user:
            print("1. Create Account")
            print("2. Log In")
            print("3. Exit")
        else:
            print(f"Currently logged in Penpal: {logged_in_user}")
            print("1. View Friend Recommendations")
            print("2. Add Friend Menu")
            print("3. Account Settings")
            print("4. Log Out")
        
        choice = input("Enter your choice: ")

        if choice == "1" and not logged_in_user:
           create_account()
        
        elif choice == "2" and not logged_in_user:
                
                username = input("Enter username: ").strip() 
                password = masked_input("Enter password: ") 
                logged_in_user = login(username, password)
              
                if logged_in_user:
                    print(f"Logged in as {logged_in_user}")
                else:
                    print("Login failed. Please try again.")

        elif choice == "1" and logged_in_user:
            while True:
                print("\n --View Friend Recommendations--")
                print(f"Currently logged in Penpal: {logged_in_user}")
                print("1. Based on Mutual Friends")
                print("2. Based on Shared Location")
                print("3. Based on Shared Interests")
                print("4. Based on Age")
                print("5. Back to Main Menu")
                fr_choice = input("Enter your choice: ")

                if fr_choice == "1":
                    recommendations = sm_graph.recommend_friends(logged_in_user)
                    if recommendations:
                        print(f"Friend recommendations for {logged_in_user} based on Mutual Friends:")
                        for user, mutual_count in recommendations.items():
                            print(f"- {user}, Mutual friends: {mutual_count}")
                    else:
                        print("No friend recommendations found based on mutual friends.")

                elif fr_choice == "2":
                     sm_graph.recommend_friends_by_location(logged_in_user)

                elif fr_choice == "3":
                     sm_graph.recommend_friends_by_interests(logged_in_user)                      

                elif fr_choice == "4":
                    sm_graph.view_friend_recommendations_based_on_age(logged_in_user)

                elif fr_choice == "5":
                    break

                elif choice == "2" and logged_in_user:
                 while True:
                    print("\n--- Friend Menu ---")
                    print("1. Manage Friend Requests (accept, decline, view)")
                    print("2. Send Friend Request")
                    print("3. View Your Friends")
                    print("4. Back to Main Menu")
                    sub_choice = input("Enter your choice: ")

               
                if sub_choice == "1":
                    while True:
                        print("\n--- Manage Friend Requests ---")
                        print("1. View Friend Requests")
                        print("2. Accept Friend Request")
                        print("3. Decline Friend Request")
                        print("4. Back to Friend Menu")
                        manage_choice = input("Enter your choice: ")

                        if manage_choice == "1":
                            friend_requests = sm_graph.get_friend_requests(logged_in_user)
                            print(f"Friend requests for {logged_in_user}: {friend_requests}")
                        elif manage_choice == "2":
                            friend_username = input("Enter the username of the friend to accept: ")
                            sm_graph.accept_friend_request(logged_in_user, friend_username)
                        elif manage_choice == "3":
                            friend_username = input("Enter the username of the friend to decline: ")
                            sm_graph.decline_friend_request(logged_in_user, friend_username)
                        elif manage_choice == "4":
                            break
                        else:
                            print("Invalid choice. Please try again.")

                elif sub_choice == "2":
                    friend_username = input("Enter the username of the friend you want to add: ")
                    sm_graph.send_friend_request(logged_in_user, friend_username)

                elif sub_choice == "3":
                    sm_graph.view_all_friends(logged_in_user)

                elif sub_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "3" and logged_in_user:
            while True:
                print("\n--- Account Settings ---")
                print("1. Edit Username")
                print("2. Edit Password")
                print("3. Edit Social Media Link")
                print("4. Delete Account")
                print("5. Back to Main Menu")
                settings_choice = input("Enter your choice: ")

                if settings_choice == "1":
                    logged_in_user = edit_username(logged_in_user)
                elif settings_choice == "2":
                    edit_password(logged_in_user)
                elif settings_choice == "3":
                    edit_social_media_link(logged_in_user)
                elif settings_choice == "4":
                    if delete_account(logged_in_user):
                        logged_in_user = None
                        break
                elif settings_choice == "5":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "4" and logged_in_user:
            logged_in_user = None
            print("Logged out successfully.")


        elif choice == "3" and not logged_in_user:
            print(f"Exiting the system. Goodbye! Thank you for using Penpal")
            break

        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()