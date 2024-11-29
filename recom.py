import mysql.connector  
import networkx as nx
import random

# Connect to MySQL database
#cute ko par
#TINGINTININITNIGN
#BAGO TO
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
            return "Generation Z (Gen Z) - 12 to 27 years old"
        elif 28 <= age <= 43:
            return "Millennials (Gen Y) - 28 to 43 years old"
        elif 44 <= age <= 59:
            return "Generation X (Gen X) - 44 to 59 years old"
        elif 60 <= age <= 78:
            return "Baby Boomers - 60 to 78 years old"
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

        # Randomly select up to `count` users
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

# Account creation and login functions
def create_account(username, age, location, gender, password):
    # Ensure that age is between 18 and 100 inclusive
    if age < 18 or age > 100:
        print("Sorry, you must be between 18 and 100 years old to create an account.")
        return

    sm_graph = SocialMediaGraph()
    user_data = {
        "age": age,
        "location": location,
        "gender": gender,
        "password": password
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

def login(username, password):
    db_cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = db_cursor.fetchone()
    if result and result[0] == password:
        print(f"Welcome back, {username}!")

        db_cursor.execute("SELECT interest FROM user_interests WHERE username = %s", (username,))
        interests = db_cursor.fetchall()
        if not interests:
            print("You haven't selected your interests yet. Let's do that now!")
            choose_interests(username)

        return username
    else:
        print("Invalid username or password.")
        return None

# Interactive menu for user actions
def main():
    logged_in_user = None
    sm_graph = SocialMediaGraph()

    while True:
        print("\n--- Social Media Friend Recommendation System ---")
        if not logged_in_user:
            print("1. Create Account")
            print("2. Log In")
            print("3. View All Registered Users")
            print("4. Exit")
        else:
            print("1. View Friend Recommendations")
            print("2. Add Friend Menu")
            print("3. Log Out")
        
        choice = input("Enter your choice: ")

        if choice == "1" and not logged_in_user:
            username = input("Enter username: ")
            password = input("Enter password: ")
            age = int(input("Enter age: "))
            location = input("Enter location: ")
            gender = input("Enter gender (Male/Female): ")
            create_account(username, age, location, gender, password)
        
        elif choice == "2" and not logged_in_user:
            username = input("Enter username: ")
            password = input("Enter password: ")
            logged_in_user = login(username, password)

        elif choice == "3" and not logged_in_user:
            sm_graph.view_all_users()

        elif choice == "1" and logged_in_user:
            while True:
                print("\n --View Friend Recommendations--")
                print("1. Based on Mutual Friends")
                print("2. Based on Shared Location")
                print("3. Based on Shared Interests")
                print("4. Find People")
                print("5. Based on Age")
                print("6. Back to Main Menu")
                fr_choice = input("Enter your choice: ")

                if fr_choice == "1":
                    recommendations = sm_graph.recommend_friends(logged_in_user)
                    if recommendations:
                        print(f"Friend recommendations for {logged_in_user} based on Mutual Friends:")
                    for user, mutual_count in recommendations.items():
                        print(f"Recommended friend: {user}, Mutual friends: {mutual_count}")
                    else:
                        print("No friend recommendations found.")

                elif fr_choice == "2":
                    recommendations = sm_graph.recommend_friends_by_location(logged_in_user)
                    if recommendations:
                        print(f"friend recommendations for {logged_in_user} based on location: ")
                        for user in recommendations:
                            print(f"- {user}")
                    else:
                        print("No recommendations found based on location")

                elif fr_choice == "3":
                    print("Based on Shared Interests")

                elif fr_choice == "4":
                    print("\n-- Find People --")
                    gender_filter = input("Which gender do you want to find? (male/female/both gender): ").lower()
                    sm_graph.find_people(logged_in_user, gender_filter=gender_filter)
                
                elif fr_choice == "5":
                    sm_graph.view_friend_recommendations_based_on_age(logged_in_user)

                elif fr_choice == "6":
                    break

        elif choice == "2" and logged_in_user:
            while True:
                print("\n--- Friend Menu ---")
                print("1. View Friend Requests")
                print("2. Send Friend Request")
                print("3. Accept Friend Request")
                print("4. Decline Friend Request")
                print("5. View your friends")
                print("6. Back to Main Menu")
                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    friend_requests = sm_graph.get_friend_requests(logged_in_user)
                    print(f"Friend requests for {logged_in_user}: {friend_requests}")
                
                elif sub_choice == "2":
                    friend_username = input("Enter the username of the friend you want to add: ")
                    sm_graph.send_friend_request(logged_in_user, friend_username)

                elif sub_choice == "3":
                    friend_username = input("Enter the username of the friend to accept: ")
                    sm_graph.accept_friend_request(logged_in_user, friend_username)

                elif sub_choice == "4":
                    friend_username = input("Enter the username of the friend to decline: ")
                    sm_graph.decline_friend_request(logged_in_user, friend_username)

                elif sub_choice == "5":
                    sm_graph.view_all_friends(logged_in_user)
                    break

                elif sub_choice == "6":
                    break

        elif choice == "3" and logged_in_user:
            logged_in_user = None
            print("Logged out successfully.")


        elif choice == "4" and not logged_in_user:
            print(f"Exiting the system. Goodbye, {username}")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
