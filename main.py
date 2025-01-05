#annie
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, QGraphicsOpacityEffect, QMessageBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, QTimer
from PyQt5 import QtCore 
import os
import sys
import requests
import re
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'FRONTEND')))
from SignUpPage import Ui_SignUp
from LogInPage import Ui_LogIn
from ForgotPass import Ui_ForgotPassword_Fullpage
from HomePage import Ui_Homepage
from WelcomePage import Ui_WelcomePage
from InterestPage import Ui_Interest
from MAINPAGE import Ui_Main_Page
from AccountSettings import Ui_AccountSettings
from AboutUsPage import Ui_AboutUs
from ContactUsPage import Ui_ContactUs
from PrivacyPolicy import Ui_PrivacyPolicy
from TermsAndCondition import Ui_TermsAndCondition
from FriendMenu import Ui_FriendMenu
from ChangeProfile import Ui_ChangeProfile 


class SplashScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 850)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


        layout = QVBoxLayout(self)


        # Add a spacer item to push the content upward
        spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)


        # Add logo
        self.logo_label = QLabel(self)
        logo_path = os.path.join(os.path.dirname(__file__), 'resources', 'images', 'Icon.png')
        if os.path.exists(logo_path):
            self.logo_label.setPixmap(QPixmap(logo_path).scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(self.logo_label, alignment=Qt.AlignCenter)


        # Add system name
        self.label = QLabel("Penpal:\nA Social Media\n Friend Recommendation System", self)
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: white;")  # Set text color to white
        layout.addWidget(self.label)


        # Add a spacer item to push the content upward
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)


        # Create opacity effect
        self.opacity_effect = QGraphicsOpacityEffect()
        self.label.setGraphicsEffect(self.opacity_effect)


        # Create animation
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()


        QTimer.singleShot(4000, self.close_splash)


    def close_splash(self):
        self.accept()


class MainApp:
    def __init__(self):
        # Create the application instance
        self.app = QApplication(sys.argv)


        # Create instances for all windows
        self.logInWindow = QMainWindow()
        self.signUpWindow = QMainWindow()
        self.homePageWindow = QWidget()
        self.interestPageWindow = QDialog()
        self.mainPageWindow = QDialog()
        self.accountSettingsWindow = QDialog()
        self.welcomePageWindow = QWidget()
        self.aboutUsWindow = QWidget()
        self.contactUsWindow = QDialog()
        self.privacyPolicyWindow = QDialog()
        self.termsWindow = QDialog()
        self.forgotPasswordWindow = QWidget()
        self.friendMenuWindow = QDialog()
        self.changeProfileWindow = QDialog()
       

        # Setup UI for all windows
        self.setup_ui()

        # Connect buttons to their respective methods
        self.connect_buttons()


    def setup_ui(self):
        # Setup UI for the WelcomePage window
        self.welcomePageUI = Ui_WelcomePage()
        self.welcomePageUI.setupUi(self.welcomePageWindow)


        # Setup UI for the login window
        self.logInUI = Ui_LogIn()
        self.logInUI.setupUi(self.logInWindow)

        # Setup UI for the WelcomePage window
        self.forgotPassUi = Ui_ForgotPassword_Fullpage()
        self.forgotPassUi.setupUi(self.forgotPasswordWindow)


        # Setup UI for the signup window
        self.signUpUI = Ui_SignUp()
        self.signUpUI.setupUi(self.signUpWindow)

         # Define error_message_label for displaying error messages
        self.error_message_label = QLabel(self.signUpWindow)
        self.error_message_label.setStyleSheet("color: red;")
        self.error_message_label.setAlignment(Qt.AlignCenter)
        self.signUpWindow.layout().addWidget(self.error_message_label)


        # Setup UI for the homepage window
        self.homePageUI = Ui_Homepage()
        self.homePageUI.setupUi(self.homePageWindow)


       # Setup UI for the interest page window
        self.interestPageUI = Ui_Interest()
        self.interestPageUI.setupUi(self.interestPageWindow)


        # Setup UI for the main page window
        self.mainPageUI = Ui_Main_Page()
        self.mainPageUI.setupUi(self.mainPageWindow)
        self.mainPageUI.MP_MenuPB.clicked.connect(self.openFriendMenu)
        self.displayed_users = set()  # Keep track of displayed users



        # Setup UI for the account settings window
        self.accountSettingsUI = Ui_AccountSettings()
        self.accountSettingsUI.setupUi(self.accountSettingsWindow)
        
        # Setup UI for the Change Profile window
        self.changeProfileUI = Ui_ChangeProfile()
        self.changeProfileUI.setupUi(self.changeProfileWindow)


        # Setup UI for the AboutUS window
        self.aboutUsUI = Ui_AboutUs()
        self.aboutUsUI.setupUi(self.aboutUsWindow)

        # Setup UI for the Contact U Window
        self.contactUsUi =  Ui_ContactUs()
        self.contactUsUi.setupUi( self.contactUsWindow)

        # Setup Ui for the privacyPolicy
        self.privacyPolicyUI = Ui_PrivacyPolicy()
        self.privacyPolicyUI.setupUi(self.privacyPolicyWindow)

        # Setup Ui for termsConditionsWindow 
        self.termsConditionsUI = Ui_TermsAndCondition()
        self.termsConditionsUI.setupUi(self.termsWindow)

         # Setup UI for the friend menu window 
        self.friendMenuUI = Ui_FriendMenu()
        self.friendMenuUI.setupUi(self.friendMenuWindow)



    def connect_buttons(self):
        # WelcomePage buttons
        self.welcomePageUI.press_to_continue.clicked.connect(self.open_homepagefromwelcome)

        # LogInPage buttons
        self.logInUI.LI_SignUpPB.clicked.connect(self.openSignUpPage)
        self.logInUI.LI_LogInPB.clicked.connect(self.openMAINPage)
        self.logInUI.LIbackButton.clicked.connect(self.openHomePageFromLogin)
        self.logInUI.LI_ForgotPasswordLBL.mousePressEvent = self.handleForgotPasswordClick
        
        # ForgotPass buttons
        self.forgotPassUi.FPbackButton.clicked.connect(self.openLogInFromForgotPass)
       
        # SignUpPage buttons
        self.signUpUI.SU_LogInPB.clicked.connect(self.backtoLogInPage)
        self.signUpUI.SU_InterestPB.clicked.connect(self.openInterestPage)
        self.signUpUI.SU_TermsandPrivacyChB.clicked.connect(self.open_terms_conditions_page_from_signup)
        self.signUpUI.SU_SignUpPB.clicked.connect(self.handle_signup)
        self.signUpUI.SU_SignUpPB.clicked.connect(self.on_sign_up_button_click)

        
        # Terms&Conditions Buttons
        self.termsConditionsUI.TAC_BackPB.clicked.connect(self.backtoSignUpFromTermsCondition)

    
        # HomePage buttons
        self.homePageUI.LogIn_2.clicked.connect(self.openLogInPageFromHomepage)
        self.homePageUI.SignUp.clicked.connect(self.openSignupFromHomepage)
        self.homePageUI.AboutUs.clicked.connect(self.openAboutUsPage)
       

        # Connect the footer buttons to their respective pages
        self.homePageUI.about_us_button.clicked.connect(self.open_about_us_page)
        self.homePageUI.contact_us_button.clicked.connect(self.open_contact_us_page)
        self.homePageUI.privacy_policy_button.clicked.connect(self.open_privacy_policy_page)
        
       

        # About Us Buttons
        self.aboutUsUI.AUbackButton.clicked.connect(self.openHomePageFromAboutUs)

        # Privacy BUttons
        self.privacyPolicyUI.PP_BackPB.clicked.connect(self.backtoHomePagefromPRIVACYPOLICY)

        # InterestPage buttons
        self.interestPageUI.INTpushButton.clicked.connect(self.on_done_clicked)
         # Dictionary to keep track of click counts
        self.click_counts = {
                "pushButton_1": 0,
                "pushButton_2": 0,
                "pushButton_3": 0,
                "pushButton_4": 0,
                "pushButton_5": 0,
                "pushButton_6": 0,
                "pushButton_7": 0,
                "pushButton_8": 0,
                "pushButton_9": 0,
                "pushButton_10": 0,
                "pushButton_11": 0,
                "pushButton_12": 0,
                "pushButton_13": 0,
                "pushButton_14": 0,
                "pushButton_15": 0,
        }

        # Variable to keep track of total clicks
        self.total_clicks = 0

        # Connect buttons to the click handler
        self.interestPageUI.pushButton_1.clicked.connect(lambda: self.handle_button_click_number("pushButton_1"))
        self.interestPageUI.pushButton_2.clicked.connect(lambda: self.handle_button_click_number("pushButton_2"))
        self.interestPageUI.pushButton_3.clicked.connect(lambda: self.handle_button_click_number("pushButton_3"))
        self.interestPageUI.pushButton_4.clicked.connect(lambda: self.handle_button_click_number("pushButton_4"))
        self.interestPageUI.pushButton_5.clicked.connect(lambda: self.handle_button_click_number("pushButton_5"))
        self.interestPageUI.pushButton_6.clicked.connect(lambda: self.handle_button_click_number("pushButton_6"))
        self.interestPageUI.pushButton_7.clicked.connect(lambda: self.handle_button_click_number("pushButton_7"))
        self.interestPageUI.pushButton_8.clicked.connect(lambda: self.handle_button_click_number("pushButton_8"))
        self.interestPageUI.pushButton_9.clicked.connect(lambda: self.handle_button_click_number("pushButton_9"))
        self.interestPageUI.pushButton_10.clicked.connect(lambda: self.handle_button_click_number("pushButton_10"))
        self.interestPageUI.pushButton_11.clicked.connect(lambda: self.handle_button_click_number("pushButton_11"))
        self.interestPageUI.pushButton_12.clicked.connect(lambda: self.handle_button_click_number("pushButton_12"))
        self.interestPageUI.pushButton_13.clicked.connect(lambda: self.handle_button_click_number("pushButton_13"))
        self.interestPageUI.pushButton_14.clicked.connect(lambda: self.handle_button_click_number("pushButton_14"))
        self.interestPageUI.pushButton_15.clicked.connect(lambda: self.handle_button_click_number("pushButton_15"))


        # MainPage buttons
        self.mainPageUI.MP_ProfilePB.clicked.connect(self.openAccountSettings)
        self.mainPageUI.MP_LogoutPB.clicked.connect(self.openHomePageFromMainPage)
        self.mainPageUI.MP_LeftArrow.clicked.connect(self.load_next_user)
        self.mainPageUI.MP_RightArrow.clicked.connect(self.send_friend_request)

         # FriendMenu Buttons
        self.friendMenuUI.FM_HomePB.clicked.connect(self.openMainPageFromFriendMenu)
        self.friendMenuUI.FM_LogOutPB.clicked.connect(self.openHomePageFromFriendMenu)
        self.friendMenuUI.FM_ProfilePB.clicked.connect(self.openAccountSettingsFromFrienMenu)

        # Initialize the list of displayed users
        self.displayed_users = set()

        # AccountSettings Buttons
        self.accountSettingsUI.AS_HomePB.clicked.connect(self.openMAINPAGEfromAccountSettings)
        self.accountSettingsUI.AS_MenuPB.clicked.connect(self.openFriendMenuFromAccountSettings)
        self.accountSettingsUI.AS_LogOutPB.clicked.connect(self.openHomepageFromAccountSettings)
        self.accountSettingsUI.AS_EditAvatarPB.clicked.connect(self.openChangeProfileFromAccountSettings)


        # ChangeProfile BUttons
        self.changeProfileUI.CP_CancelChangesPB.clicked.connect(self.openAccountSettingsFromChangeProfile)
        
    # WelcomePage methods
    def open_homepagefromwelcome(self):
        self.welcomePageWindow.close()
        self.homePageWindow.show()

    # HomePage methods
    def open_about_us_page(self):
        self.homePageWindow.close()
        self.aboutUsWindow.show()
    def open_contact_us_page(self):
        self.homePageWindow.close()
        self.contactUsWindow.show()
    def open_privacy_policy_page(self):
        self.homePageWindow.close()
        self.privacyPolicyWindow.show()
    
   
    def openSignupFromHomepage(self):
        self.homePageWindow.close()
        self.signUpWindow.show()
    def openLogInPageFromHomepage(self):
        self.homePageWindow.close()
        self.logInWindow.show()

    
    
    # PrivacyPolicy methods  
    def backtoHomePagefromPRIVACYPOLICY(self):
        self.privacyPolicyWindow.close()
        self.homePageWindow.show()

    # AboutUsPage methods
    def openAboutUsPage(self):
        self.homePageWindow.close()
        self.aboutUsWindow.show()
    def openHomePageFromAboutUs(self):
        self.aboutUsWindow.close()
        self.homePageWindow.show()


    # LogInPage methods
    def openHomePageFromLogin(self):
        self.logInWindow.close()
        self.homePageWindow.show()
    def openSignUpPage(self):
        self.logInWindow.close()
        self.signUpWindow.show()
    def handleForgotPasswordClick(self, event):
        self.openForgotPassPageFromLogin()
    def openForgotPassPageFromLogin(self):
        self.logInWindow.close()
        self.forgotPasswordWindow.show()

     # ForgotPass methods
    def openLogInFromForgotPass(self):
        self.forgotPasswordWindow.close()
        self.logInWindow.show()

    # SignUpPage methods
    def handle_signup(self):
        username = self.signUpUI.SU_UsernameLE.text()
        password = self.signUpUI.SU_PasswordLE.text()
        gender = self.signUpUI.SU_GenderCB.currentText()
        location = self.signUpUI.SU_LocationLE.text()
        social_media_link = self.signUpUI.SU_SocialLinkLE.text()
        gmail = self.signUpUI.SU_EmailLE.text()  # New field for Gmail account

        # Check if all fields are filled
        if not username or not password or not location or not gender or not gmail:
            self.show_error_message("Please fill in all the required fields.")
            return False  # Indicate that the sign-up process should not continue

        # Validate password
        password_issue = self.validate_password(password)
        if password_issue:
            self.show_error_message(f"Error: {password_issue}. Please re-enter your password.")
            self.signUpUI.SU_PasswordLE.clear()  # Clear the password field to prompt re-entry
            return False  # Indicate that the sign-up process should not continue

        # Validate social media link
        if not self.validate_social_link():
            self.show_error_message("Invalid social media link. Please enter a valid link.")
            self.signUpUI.SU_SocialLinkLE.clear()  # Clear the link field to prompt re-entry
            return False  # Indicate that the sign-up process should not continue

        # Get selected interests
        selected_interests = self.get_selected_interests()

        # Check if interests are selected
        if len(selected_interests) < 5:
            self.show_error_message("Please select at least five interests.")
            return False  # Indicate that the sign-up process should not continue

        # Check if terms and conditions are accepted
        terms_accepted = self.signUpUI.SU_TermsandPrivacyChB.isChecked()
        if not terms_accepted:
            self.show_error_message("You must accept the Terms and Conditions to create an account.")
            return False  # Indicate that the sign-up process should not continue

        dob = self.signUpUI.SU_DOB.date().toPyDate()  # Assuming you have a QDateEdit for date of birth
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        # Check if username already exists
        data = {'username': username}

        try:
            # First, check if the username exists
            response = requests.post('http://127.0.0.1:5000/check_username', json=data)

            if response.status_code == 400:  # Assuming the backend returns 400 if the username exists
                self.show_error_message("Username already exists. Please choose another username.")
                self.signUpUI.SU_UsernameLE.clear()  # Clear the username field to prompt re-entry
                return False  # Indicate that the sign-up process should not continue

            # If the username is available, proceed with the sign-up process
            sign_up_data = {
                'username': username,
                'password': password,
                'age': int(age),
                'gender': gender,
                'location': location,
                'social_media_link': social_media_link,
                'gmail': gmail,  # Include the Gmail field in the sign-up data
                'interests': self.get_selected_interests()  # Include the selected interests
            }

            # Send the data to the backend to create the account
            response = requests.post('http://127.0.0.1:5000/signup', json=sign_up_data)

            if response.status_code == 201:
                self.show_success_message("Account created successfully!")

                # Clear the input fields after sign-up
                self.signUpUI.SU_UsernameLE.clear()
                self.signUpUI.SU_PasswordLE.clear()
                self.signUpUI.SU_DOB.setDate(QtCore.QDate.currentDate())  # Reset to current date
                self.signUpUI.SU_GenderCB.setCurrentIndex(0)  # Reset to first item (if applicable)
                self.signUpUI.SU_LocationLE.clear()
                self.signUpUI.SU_SocialLinkLE.clear()
                self.signUpUI.SU_EmailLE.clear()  # Clear the Gmail field

                self.clear_error_message()  # Clear any existing error messages

                self.show_success_message("You can continue creating another account or stay here.")

                return True  # Indicate that the sign-up process succeeded
            else:
                error_message = response.json().get('error', 'Unknown error occurred')
                self.show_error_message(f"Error: {error_message}")
                return False  # Indicate failure

        except requests.exceptions.RequestException as e:
            self.show_error_message(f"Request failed: {str(e)}")
        return False  # Indicate failure
    def clear_error_message(self):
        # Assuming you have a QLabel named error_message_label for displaying error messages
        self.error_message_label.setText("")

    def show_success_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Success")
        msg.exec_()

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def validate_password(self, password):
        if len(password) < 8:
            return "Password must be at least 8 characters long."
        if not any(char.isdigit() for char in password):
            return "Password must include at least one number."
        if not any(char.isupper() for char in password):
            return "Password must include at least one uppercase letter."
        if not any(char in "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|" for char in password):
            return "Password must include at least one special character."
        return None

    def validate_social_link(self):
        social_link = self.signUpUI.SU_SocialLinkLE.text()
        # Updated pattern to allow periods in the path
        pattern = r"^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(/[\w\-\.]*)*$"
        return bool(re.match(pattern, social_link))
    def on_sign_up_button_click(self):
        if self.handle_signup():  # If sign-up is successful, proceed
           self.backtoLogInPage()
        else:
            # If there's an issue (password, social link, etc.), the user will have to fix it
            pass
    def backtoLogInPage(self):
        self.signUpWindow.close()
        self.logInWindow.show()
    def open_terms_conditions_page_from_signup(self):
        self.signUpWindow.close()
        self.termsWindow.show()
    def openInterestPage(self):
        self.signUpWindow.close()
        self.interestPageWindow.show()

    # Terms&Conditions methods
    def backtoSignUpFromTermsCondition(self):
        self.termsWindow.close()
        self.signUpWindow.show()
       
     # Interests methods
    def handle_button_click_number(self, button_name):
        # Check if the button has already been clicked
        if self.click_counts[button_name] == 0:
            # Increment the total click count only if the button is clicked for the first time
            self.total_clicks += 1

        # Increment the click count for the button
        self.click_counts[button_name] += 1

        # Update the placeholder text with the new total count
        self.interestPageUI.placeholderText.setText(f"{self.total_clicks} selected")


    def get_selected_interests(self):
        interests = {
            "pushButton_1": "SPORTS",
            "pushButton_2": "TECHNOLOGY",
            "pushButton_3": "GAMING",
            "pushButton_4": "ARTS",
            "pushButton_5": "PHOTOGRAPHY",
            "pushButton_6": "MUSIC",
            "pushButton_7": "TRAVEL",
            "pushButton_8": "COOKING",
            "pushButton_9": "FASHION",
            "pushButton_10": "EDUCATION",
            "pushButton_11": "MOVIES",
            "pushButton_12": "BOOKS",
            "pushButton_13": "LIFESTYLE",
            "pushButton_14": "SCIENCE",
            "pushButton_15": "BUSINESS",
        }
        selected_interests = [interest for button, interest in interests.items() if self.click_counts[button] > 0]
        return selected_interests

    def show_selected_interests(self, selected_interests):
        interests_str = "\n".join(selected_interests)
        QMessageBox.information(self.interestPageWindow, "Selected Interests", f"Your selected interests are:\n{interests_str}")

    def on_done_clicked(self):
        selected_interests = self.get_selected_interests()
        self.show_selected_interests(selected_interests)
        self.interestPageWindow.close()
        self.signUpWindow.show()

    
    def openMAINPage(self):
        # Assuming user_id and username are obtained after successful login
        user_id = self.logInUI.user_id  # Replace with actual user_id
        username = self.logInUI.username  # Replace with actual username

        # Set user info in the main page UI
        self.mainPageUI.set_user_info(user_id, username)

        # Show the main page window
        self.logInWindow.close()
        self.mainPageWindow.show()

        # Load the first user immediately
        self.load_next_user()

    #MAINPAGE methods

    def openAccountSettings(self):
        self.accountSettingsUI.set_user_info(self.logInUI.user_id, self.logInUI.username)
        self.mainPageWindow.close()
        self.accountSettingsWindow.show()
    def openFriendMenu(self):
        self.mainPageWindow.close()
        self.friendMenuWindow.show()
        self.fetch_pending_friend_requests()

    def openHomePageFromMainPage(self):
        try:
            response = requests.post('http://127.0.0.1:5000/logout')
            if response.status_code == 200:
                self.show_success_message("Logged out successfully")
                # Reset displayed_users list
                self.displayed_users = set()
            else:
                self.show_error_message("Logout failed", "Failed to log out. Please try again.")
        except requests.exceptions.RequestException as e:
            self.show_error_message("Logout failed", f"An error occurred: {e}")

        # Close the Main Page window and show the Home Page window
        self.mainPageWindow.close()
        self.homePageWindow.show()

    def fetch_and_display_user(self, current_username):
        try:
            response = requests.get('http://127.0.0.1:5000/get_one_user', params={
                'current_username': current_username,
                'logged_in_username': self.logInUI.username  # Pass the logged-in username
            })
            if response.status_code == 200:
                user = response.json().get('user', {})
                self.display_user(user)
            else:
                print(f"Error: Received status code {response.status_code}")
                print(f"Response content: {response.content}")
                self.show_error_message("Failed to fetch user.")
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {str(e)}")
            self.show_error_message(f"Request failed: {str(e)}")
    def display_user(self, user):
        if user:
            self.mainPageUI.MP_Username.setText(user['username'])
            self.mainPageUI.MP_Age.setText(f"Age: {user['age']}")
            self.mainPageUI.MP_Gender.setText(f"Gender: {user['gender']}")
            self.mainPageUI.MP_Location.setText(f"Location: {user['location']}")
            preferences = user.get('preferences', [])
            self.mainPageUI.MP_Preference1.setText(preferences[0] if len(preferences) > 0 else "Pref.1")
            self.mainPageUI.MP_Preference2.setText(preferences[1] if len(preferences) > 1 else "Pref.2")
            self.mainPageUI.MP_Preference3.setText(preferences[2] if len(preferences) > 2 else "Pref.3")
            self.mainPageUI.MP_Preference4.setText(preferences[3] if len(preferences) > 3 else "Pref.4")
            self.mainPageUI.MP_Preference5.setText(preferences[4] if len(preferences) > 4 else "Pref.5")
        else:
            self.show_error_message("No user data available.")

    def load_next_user(self):
        try:
            current_username = self.mainPageUI.MP_Username.text()
            self.displayed_users.add(current_username)  # Add current user to displayed users

            response = requests.get('http://127.0.0.1:5000/get_one_user', params={
                'current_username': current_username,
                'logged_in_username': self.logInUI.username,  # Pass the logged-in username
                'displayed_users': list(self.displayed_users)  # Pass the list of displayed users
            })
            if response.status_code == 200:
                user = response.json().get('user', {})
                self.display_user(user)
            elif response.status_code == 404:
                self.show_error_message("No more users available.")
            else:
                print(f"Error: Received status code {response.status_code}")
                print(f"Response content: {response.content}")
                self.show_error_message("Failed to fetch user.")
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {str(e)}")
            self.show_error_message(f"Request failed: {str(e)}")

    def send_friend_request(self):
        current_username = self.mainPageUI.MP_Username.text()
        logged_in_username = self.logInUI.username

        data = {
            'from_user': logged_in_username,
            'to_user': current_username
        }

        try:
            response = requests.post('http://127.0.0.1:5000/send_friend_request', json=data)
            if response.status_code == 201:
                self.show_success_message("Friend request sent successfully")
            else:
                error_message = response.json().get('error', 'Unknown error occurred')
                self.show_error_message(f"Error: {error_message}")
        except requests.exceptions.RequestException as e:
            self.show_error_message(f"Request failed: {str(e)}")
   
    
    #FRIEND MENU
    def openMainPageFromFriendMenu(self):
        self.friendMenuWindow.close()
        self.mainPageWindow.show()
    def openAccountSettingsFromFrienMenu(self):
        self.friendMenuWindow.close()
        self.accountSettingsWindow.show()
    def openHomePageFromFriendMenu(self):
        self.friendMenuWindow.close()
        self.homePageWindow.show()


    def fetch_pending_friend_requests(self):
        username = self.logInUI.username  # Get the logged-in username

        try:
            response = requests.get('http://127.0.0.1:5000/get_pending_friend_requests', params={'username': username})
            if response.status_code == 200:
                pending_requests = response.json().get('pending_requests', [])
                self.display_pending_friend_requests(pending_requests)
            else:
                print(f"Error: Received status code {response.status_code}")
                print(f"Response content: {response.content}")
                self.show_error_message("Failed to fetch pending friend requests.")
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {str(e)}")
            self.show_error_message(f"Request failed: {str(e)}")

    def display_pending_friend_requests(self, pending_requests):
        _translate = QtCore.QCoreApplication.translate
        friend_request_labels = [
            self.friendMenuUI.FM_FriendRequest1,
            self.friendMenuUI.FM_FriendRequest2,
            self.friendMenuUI.FM_FriendRequest3,
            self.friendMenuUI.FM_FriendRequest4,
            self.friendMenuUI.FM_FriendRequest5,
            self.friendMenuUI.FM_FriendRequest6,
            self.friendMenuUI.FM_FriendRequest7,
            self.friendMenuUI.FM_FriendRequest8,
            self.friendMenuUI.FM_FriendRequest9,
            self.friendMenuUI.FM_FriendRequest10
        ]

        for i, label in enumerate(friend_request_labels):
            if i < len(pending_requests):
                label.setText(_translate("FriendMenu", f"{pending_requests[i]}"))
            else:
                label.setText(_translate("FriendMenu", ""))
    


    # AccountSettings methods
    def openMAINPAGEfromAccountSettings(self):
        self.accountSettingsWindow.close()
        self.mainPageWindow.show()
    def openFriendMenuFromAccountSettings(self):
        self.accountSettingsWindow.close()
        self.friendMenuWindow.show()
    def openHomepageFromAccountSettings(self):
        try:
            response = requests.post('http://127.0.0.1:5000/logout')
            if response.status_code == 200:
                self.show_success_message("Logged out successfully")
                # Reset displayed_users list
                self.displayed_users = set()
            else:
                self.show_error_message("Logout failed", "Failed to log out. Please try again.")
        except requests.exceptions.RequestException as e:
            self.show_error_message("Logout failed", f"An error occurred: {e}")
            
        self.accountSettingsWindow.close()
        self.homePageWindow.show()
    def openChangeProfileFromAccountSettings(self):
        self.changeProfileUI.set_user_info(self.logInUI.user_id, self.logInUI.username)
        self.accountSettingsWindow.close()
        self.changeProfileWindow.show()


    # ChangeProifle methods
    def openAccountSettingsFromChangeProfile(self):
        self.changeProfileWindow.close()
        self.accountSettingsWindow.show()



    def run(self):
        # Show the splash screen
        splash = SplashScreen()
        if splash.exec_() == QDialog.Accepted:
            # Show the welcome page after the splash screen
            self.welcomePageWindow.show()
            sys.exit(self.app.exec_())


# Run the application
if __name__ == "__main__":
    mainApp = MainApp()
    mainApp.run()



