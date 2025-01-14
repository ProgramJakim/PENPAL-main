
import os
import sys
import traceback
import requests
import re
from datetime import datetime
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, QGraphicsOpacityEffect, QMessageBox, QListWidget, QMessageBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, QTimer
from PyQt5 import QtCore 



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
from NotificationPage import NotificationWindow

class SplashScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 850)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


        layout = QVBoxLayout(self)


        spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)


      
        self.logo_label = QLabel(self)
        logo_path = os.path.join(os.path.dirname(__file__), 'resources', 'images', 'Icon.png')
        if os.path.exists(logo_path):
            self.logo_label.setPixmap(QPixmap(logo_path).scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(self.logo_label, alignment=Qt.AlignCenter)


      
        self.label = QLabel("Penpal:\nA Social Media\n Friend Recommendation System", self)
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: white;")  
        layout.addWidget(self.label)


        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)


      
        self.opacity_effect = QGraphicsOpacityEffect()
        self.label.setGraphicsEffect(self.opacity_effect)


     
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()


        QTimer.singleShot(1000, self.close_splash)


    def close_splash(self):
        self.accept()


class MainApp:
    def __init__(self):
      
        self.app = QApplication(sys.argv)


       
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
     
        self.notificationWindow = NotificationWindow()
       

     
        self.setup_ui()

       
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
        self.selected_interests = []


        # Setup UI for the main page window
        self.mainPageUI = Ui_Main_Page()
        self.mainPageUI.setupUi(self.mainPageWindow)
        self.mainPageUI.MP_MenuPB.clicked.connect(self.openFriendMenu)
        self.displayed_users = set()  # Keep track of displayed users
        self.first_user = None 
        # Setup UI for NOtification
        self.notificationWindow = NotificationWindow()

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
         # Connect buttons to their respective methods
        



    def connect_buttons(self):
        # WelcomePage buttons
        self.welcomePageUI.press_to_continue.clicked.connect(self.open_homepagefromwelcome)

        # LogInPage buttons
        self.logInUI.LI_SignUpPB.clicked.connect(self.openSignUpPage)
        self.logInUI.LI_LogInPB.clicked.connect(self.openMAINPage)
        self.logInUI.LIbackButton.clicked.connect(self.openHomePageFromLogin)
       
        
        # ForgotPass buttons
        self.forgotPassUi.FPbackButton.clicked.connect(self.openLogInFromForgotPass)
       
        # SignUpPage buttons neww
        self.signUpUI.SU_InterestPB.clicked.connect(self.openInterestPage)
        self.signUpUI.SU_TermsandPrivacyChB.clicked.connect(self.open_terms_conditions_page_from_signup)
        
        if hasattr(self.signUpUI.SU_SignUpPB, 'clicked'):
            try:
                self.signUpUI.SU_SignUpPB.clicked.disconnect()
            except TypeError:
                pass
        self.signUpUI.SU_SignUpPB.clicked.connect(self.handle_signup_origin)
        
        self.signUpUI.SU_LogInPB.clicked.connect(self.on_sign_up_button_click)

        
        # Terms&Conditions Buttons
        self.termsConditionsUI.TAC_BackPB.clicked.connect(self.backtoSignUpFromTermsCondition)

        # Contact Us Buttons
        self.contactUsUi.CUbackButton.clicked.connect(self.backtoHomePagefromContactUs)
       
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
        
        # Connect the notification button to open the notification window
        self.mainPageUI.MP_NotificationPB.clicked.connect(self.open_notification_window)

         # FriendMenu Buttons
        self.friendMenuUI.FM_HomePB.clicked.connect(self.openMainPageFromFriendMenu)
        self.friendMenuUI.FM_LogOutPB.clicked.connect(self.openHomePageFromFriendMenu)
        self.friendMenuUI.FM_ProfilePB.clicked.connect(self.openAccountSettingsFromFrienMenu)

        # Initialize the list of displayed users
        self.displayed_users = set()

        # FriendMenu buttons
        self.friendMenuUI.FM_Accept1PB.clicked.connect(lambda: self.accept_friend_request(self.friendMenuUI.FM_FriendRequest1.text()))
        self.friendMenuUI.FM_Accept2PB.clicked.connect(lambda: self.accept_friend_request(self.friendMenuUI.FM_FriendRequest2.text()))
        self.friendMenuUI.FM_Accept3PB.clicked.connect(lambda: self.accept_friend_request(self.friendMenuUI.FM_FriendRequest3.text()))
        self.friendMenuUI.FM_Accept4PB.clicked.connect(lambda: self.accept_friend_request(self.friendMenuUI.FM_FriendRequest4.text()))
        self.friendMenuUI.FM_Accept5PB.clicked.connect(lambda: self.accept_friend_request(self.friendMenuUI.FM_FriendRequest5.text()))
        self.friendMenuUI.FM_Accept6PB.clicked.connect(lambda: self.accept_friend_request(self.friendMenuUI.FM_FriendRequest6.text()))
        self.friendMenuUI.FM_Accept7PB.clicked.connect(lambda: self.accept_friend_request(self.friendMenuUI.FM_FriendRequest7.text()))
        self.friendMenuUI.FM_Accept8PB.clicked.connect(lambda: self.accept_friend_request(self.friendMenuUI.FM_FriendRequest8.text()))
        self.friendMenuUI.FM_Accept9PB.clicked.connect(lambda: self.accept_friend_request(self.friendMenuUI.FM_FriendRequest9.text()))
        self.friendMenuUI.FM_Accept10PB.clicked.connect(lambda: self.accept_friend_request(self.friendMenuUI.FM_FriendRequest10.text()))


        self.friendMenuUI.FM_Decline1PB.clicked.connect(lambda: self.decline_friend_request(self.friendMenuUI.FM_FriendRequest1.text()))
        self.friendMenuUI.FM_Decline2PB.clicked.connect(lambda: self.decline_friend_request(self.friendMenuUI.FM_FriendRequest2.text()))
        self.friendMenuUI.FM_Decline3PB.clicked.connect(lambda: self.decline_friend_request(self.friendMenuUI.FM_FriendRequest3.text()))
        self.friendMenuUI.FM_Decline4PB.clicked.connect(lambda: self.decline_friend_request(self.friendMenuUI.FM_FriendRequest4.text()))
        self.friendMenuUI.FM_Decline5PB.clicked.connect(lambda: self.decline_friend_request(self.friendMenuUI.FM_FriendRequest5.text()))
        self.friendMenuUI.FM_Decline6PB.clicked.connect(lambda: self.decline_friend_request(self.friendMenuUI.FM_FriendRequest6.text()))
        self.friendMenuUI.FM_Decline7PB.clicked.connect(lambda: self.decline_friend_request(self.friendMenuUI.FM_FriendRequest7.text()))
        self.friendMenuUI.FM_Decline8PB.clicked.connect(lambda: self.decline_friend_request(self.friendMenuUI.FM_FriendRequest8.text()))
        self.friendMenuUI.FM_Decline9PB.clicked.connect(lambda: self.decline_friend_request(self.friendMenuUI.FM_FriendRequest9.text()))
        self.friendMenuUI.FM_Decline10PB.clicked.connect(lambda: self.decline_friend_request(self.friendMenuUI.FM_FriendRequest10.text()))



       # AccountSettings Buttons
        self.accountSettingsUI.AS_HomePB.clicked.connect(self.openMAINPAGEfromAccountSettings)
        self.accountSettingsUI.AS_MenuPB.clicked.connect(self.openFriendMenuFromAccountSettings)
        self.accountSettingsUI.AS_LogOutPB.clicked.connect(self.openHomepageFromAccountSettings)
        self.accountSettingsUI.AS_EditAvatarPB.clicked.connect(self.openChangeProfileFromAccountSettings)
        # Connect the save changes button to the change_social_link method
        self.accountSettingsUI.AS_SaveChangesPB.clicked.connect(self.save_changes)
        



        # ChangeProfile BUttons
        self.changeProfileUI.CP_CancelChangesPB.clicked.connect(self.openAccountSettingsFromChangeProfile)
        
        #RECOMMENDATIONS Buttons
        self.mainPageUI.MP_ViewMutualFriendsButton.clicked.connect(self.show_mutual_friends_list)
    
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

    def handle_signup_origin(self):
        print("handle_signup called") 
        username = self.signUpUI.SU_UsernameLE.text()
        password = self.signUpUI.SU_PasswordLE.text()
        gender = self.signUpUI.SU_GenderCB.currentText()
        location = self.signUpUI.SU_LocationLE.text()
        social_media_link = self.signUpUI.SU_SocialLinkLE.text()
        gmail = self.signUpUI.SU_EmailLE.text()  
        selected_interests = self.selected_interests  

        if not username or not password or not location or not gender or not gmail:
            self.show_error_message("Please fill in all the required fields.")
            return False  

      
        password_issue = self.validate_password(password)
        if password_issue:
            self.show_error_message(f"Error: {password_issue}. Please re-enter your password.")
            self.signUpUI.SU_PasswordLE.clear()  
            return False 

     
        if not self.validate_social_link():
            self.show_error_message("Invalid social media link. Please enter a valid link.")
            self.signUpUI.SU_SocialLinkLE.clear()  
            return False 


        selected_interests = self.get_selected_interests()

    
        if len(selected_interests) < 5:
            self.show_error_message("Please select at least five interests.")
            return False 

        if len(selected_interests) < 5:
            self.show_error_message("Please select at least five interests.")
            return False  

        terms_accepted = self.signUpUI.SU_TermsandPrivacyChB.isChecked()
        if not terms_accepted:
            self.show_error_message("You must accept the Terms and Conditions to create an account.")
            return False  

        dob = self.signUpUI.SU_DOB.date().toPyDate()
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


        data = {'username': username}

        try:
         
            response = requests.post('http://127.0.0.1:5000/check_username', json=data)
            print(f"Response status code: {response.status_code}")  

            if response.status_code == 400:  
                self.show_error_message("Username already exists. Please choose another username.")
                self.signUpUI.SU_UsernameLE.clear()  
                return False  


            sign_up_data = {
                'username': username,
                'password': password,
                'age': int(age),
                'gender': gender,
                'location': location,
                'social_media_link': social_media_link,
                'gmail': gmail,  
                'interests': selected_interests 
            }

            
            response = requests.post('http://127.0.0.1:5000/signup', json=sign_up_data)

            
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.content}")

            if response.status_code == 201:
                self.clear_error_message() 
                self.show_success_message("Account created successfully!")

               
                self.signUpUI.SU_UsernameLE.clear()
                self.signUpUI.SU_PasswordLE.clear()
                self.signUpUI.SU_DOB.setDate(QtCore.QDate.currentDate())  
                self.signUpUI.SU_GenderCB.setCurrentIndex(0)  
                self.signUpUI.SU_LocationLE.clear()
                self.signUpUI.SU_SocialLinkLE.clear()
                self.signUpUI.SU_EmailLE.clear()  
                self.signUpUI.SU_EmailLE.clear() 

                self.total_clicks = 0
                self.click_counts = {button_name: 0 for button_name in self.click_counts}
                self.interestPageUI.placeholderText.setText("0 selected")  
                self.show_success_message("You can continue creating another account or stay here.")
                self.clear_error_message()
                return True 
            else:
                error_message = response.json().get('error', 'Unknown error occurred')
                self.show_error_message(f"Error: {error_message}")
                return False 

        except requests.exceptions.RequestException as e:
            self.show_error_message(f"Request failed: {str(e)}")
        return False 

    def clear_error_message(self):
       
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
        
        pattern = r"^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(/[\w\-\.]*)*$"
        return bool(re.match(pattern, social_link))
    
    def on_sign_up_button_click(self):
        if self.handle_signup_origin():  
            self.backtoLogInPage()
        else:
           
            reply = QMessageBox.question(
                self.signUpWindow,
                'Continue Sign Up?',
                'Are you sure you want to stop the sign-up process?',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                self.backtoLogInPage()
            else:
               
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

  
    def backtoSignUpFromTermsCondition(self):
        self.termsWindow.close()
        self.signUpWindow.show()

    def backtoHomePagefromContactUs(self):
        self.contactUsWindow.close()
        self.homePageWindow.show()
       
   
    def handle_button_click_number(self, button_name):
        
        if self.click_counts[button_name] == 0:
           
            self.total_clicks += 1

  
        self.click_counts[button_name] += 1

        
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
        
        if len(selected_interests) < 5:
            self.show_error_message("Please select at least five interests.")
            return
        
        self.show_selected_interests(selected_interests)
        self.interestPageWindow.close()
        self.signUpWindow.show()
        

    
    

    #MAINPAGE methods

    def openAccountSettings(self):
        self.accountSettingsUI.set_user_info(self.logInUI.user_id, self.logInUI.username)
        self.mainPageWindow.close()
        self.accountSettingsWindow.show()
    def openFriendMenu(self):
        self.mainPageWindow.close()
        self.friendMenuWindow.show()
        self.fetch_pending_friend_requests()
        self.fetch_accepted_friends()

    def openHomePageFromMainPage(self):
        try:
            response = requests.post('http://127.0.0.1:5000/logout')
            if response.status_code == 200:
                self.show_success_message("Logged out successfully")
              
                self.displayed_users = set()
            else:
                self.show_error_message("Logout failed", "Failed to log out. Please try again.")
        except requests.exceptions.RequestException as e:
            self.show_error_message("Logout failed", f"An error occurred: {e}")

       
        self.mainPageWindow.close()
        self.homePageWindow.show()
    
    def openMAINPage(self):
        username = self.logInUI.LI_UsernameLE.text()
        password = self.logInUI.LI_PasswordLE.text()

        data = {
            'username': username,
            'password': password
        }

        try:
            response = requests.post('http://127.0.0.1:5000/login', json=data)
            if response.status_code == 200:
                user_data = response.json()
                self.logInUI.user_id = user_data['user_id']
                self.logInUI.username = user_data['username']
                self.logged_in_username = user_data['username'] 


                self.mainPageUI.set_user_info(self.logInUI.user_id, self.logInUI.username)

              
                self.logInWindow.close()
                self.mainPageWindow.show()

                self.load_next_user()
            else:
                error_message = response.json().get('error', '')
                if error_message:
                    self.show_error_message(f"Error: {error_message}")
        except requests.exceptions.RequestException as e:
            self.show_error_message(f"Request failed: {str(e)}")

    def fetch_and_display_user(self, current_username):
        try:
            response = requests.get('http://127.0.0.1:5000/get_one_user', params={
                'current_username': current_username,
                'logged_in_username': self.logInUI.username
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

    def handle_left_button_click(self):
      
        self.mainPageUI.MP_LeftArrow += 1

     
        if self.mainPageUI.MP_LeftArrow >= 2:
            self.show_error_message("No more users available after multiple attempts.")
            self.clear_user_display()
          
            self.mainPageUI.MP_LeftArrow = 0
        else:
            self.load_next_user()


    def load_next_user(self):
        current_username = self.mainPageUI.MP_UPusername.text()
        if not current_username:
            return

        try:
            response = requests.get('http://localhost:5000/get_one_user', params={
                'current_username': current_username,
                'logged_in_username': self.logInUI.username,
                'displayed_users': list(self.displayed_users)
            })
            if response.status_code == 200:
                user = response.json().get('user')
                if user:
                    if not self.first_user:
                        self.first_user = user['username'] 
                    self.display_user(user)
                    self.displayed_users.add(user['username'])

                 
                    mutual_response = requests.get('http://localhost:5000/get_mutual_friends_count', params={
                        'username': self.logInUI.username,
                        'other_user': user['username']
                    })
                    if mutual_response.status_code == 200:
                        mutual_data = mutual_response.json()
                        mutual_count = mutual_data.get('mutual_count', 0)
                        mutual_friends = mutual_data.get('mutual_friends', [])
                        if mutual_count > 0:
                            self.mainPageUI.MP_MutualFriends.setText(f"Mutual Friend{'s' if mutual_count > 1 else ''}: {mutual_count}")
                            self.mainPageUI.MP_MutualFriendsList.setText(", ".join(mutual_friends))
                            self.mainPageUI.MP_MutualFriends.show()
                            self.mainPageUI.MP_ViewMutualFriendsButton.setText(f"View Mutual Friend{'s' if mutual_count > 1 else ''}")
                            self.mainPageUI.MP_ViewMutualFriendsButton.show()
                        else:
                            self.mainPageUI.MP_MutualFriends.hide()
                            self.mainPageUI.MP_ViewMutualFriendsButton.hide()
                            self.mainPageUI.MP_MutualFriendsList.setText("")
                    else:
                        self.mainPageUI.MP_MutualFriends.hide()
                        self.mainPageUI.MP_ViewMutualFriendsButton.hide()
                        self.mainPageUI.MP_MutualFriendsList.setText("")

           
                    self.highlight_common_interests(user['username'])

              
                    self.highlight_location(user['username'])
                else:
                    self.prompt_browse_again()
                    self.clear_user_display()
            else:
                self.prompt_browse_again()
                self.clear_user_display()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            self.clear_user_display()

    def show_mutual_friends_list(self):
        mutual_friends_list = self.mainPageUI.MP_MutualFriendsList.text().split(", ")
        mutual_friends_str = "\n".join(mutual_friends_list)
        mutual_friends_count = len(mutual_friends_list)
        title = "Mutual Friend" if mutual_friends_count == 1 else "Mutual Friends"
        QMessageBox.information(self.mainPageWindow, title, mutual_friends_str)
    
    def highlight_common_interests(self, other_username):
        try:
            response = requests.get('http://localhost:5000/get_user_interests', params={
                'username': self.logInUI.username
            })
            if response.status_code == 200:
                logged_in_user_interests = set(response.json().get('interests', []))

                response = requests.get('http://localhost:5000/get_user_interests', params={
                    'username': other_username
                })
                if response.status_code == 200:
                    other_user_interests = set(response.json().get('interests', []))
                    common_interests = logged_in_user_interests.intersection(other_user_interests)

               
                    for label in self.mainPageUI.interest_labels:
                        label.setStyleSheet("color: rgb(122, 12, 12);\n"
                                            "border: none;\n"
                                            "font: 700 12pt \"Rockwell\";\n"
                                            "background: none;\n")

                    for interest in common_interests:
                        for label in self.mainPageUI.interest_labels:
                            if label.text() == interest:
                                label.setStyleSheet("background-color: yellow;")
                                if label == self.mainPageUI.MP_Preference1:
                                        label.setGeometry(QtCore.QRect(30, 360, 190, 30))
                                elif label == self.mainPageUI.MP_Preference2:
                                        label.setGeometry(QtCore.QRect(300, 360, 190, 30))
                                elif label == self.mainPageUI.MP_Preference3:
                                        label.setGeometry(QtCore.QRect(30, 400, 190, 30))
                                elif label == self.mainPageUI.MP_Preference4:
                                        label.setGeometry(QtCore.QRect(300, 400, 190, 30))
                                elif label == self.mainPageUI.MP_Preference5:
                                        label.setGeometry(QtCore.QRect(190, 440, 190, 30))


       
                    common_interests_count = len(common_interests)
                    self.mainPageUI.MP_Preference.setText(f"Preferences: {common_interests_count} same interest{'s' if common_interests_count > 1 else ''}!")
                else:
                    print(f"Error: Received status code {response.status_code} for other user's interests")
                    self.mainPageUI.MP_Preference.setText("Preferences: 0 same interests!")
            else:
                print(f"Error: Received status code {response.status_code} for logged-in user's interests")
                self.mainPageUI.MP_Preference.setText("Preferences: 0 same interests!")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            self.mainPageUI.MP_Preference.setText("Preferences: 0 same interests!")
    
    def highlight_location(self, other_username):
        try:
            response = requests.get('http://localhost:5000/get_user_location', params={
                'username': self.logInUI.username
            })
            if response.status_code == 200:
                logged_in_user_location = response.json().get('location', '')

                response = requests.get('http://localhost:5000/get_user_location', params={
                    'username': other_username
                })
                if response.status_code == 200:
                    other_user_location = response.json().get('location', '')

                    if logged_in_user_location == other_user_location:
                        self.mainPageUI.MP_Location.setStyleSheet("background-color: yellow; border:  2px solid rgb(122, 12, 12); color: rgb(122, 12, 12);")
                        self.mainPageUI.MP_Location.setGeometry(QtCore.QRect(30, 270, 470, 30))
                    else:
                        self.mainPageUI.MP_Location.setStyleSheet("border: none; color: rgb(122, 12, 12);")
                        self.mainPageUI.MP_Location.setGeometry(QtCore.QRect(30, 270, 470, 30))
                else:
                    print(f"Error: Received status code {response.status_code} for other user's location")
                    self.mainPageUI.MP_Location.setStyleSheet("border: none;")
                    self.mainPageUI.MP_Location.setGeometry(QtCore.QRect(30, 270, 470, 30))
            else:
                print(f"Error: Received status code {response.status_code} for logged-in user's location")
                self.mainPageUI.MP_Location.setStyleSheet("border: none;")
                self.mainPageUI.MP_Location.setGeometry(QtCore.QRect(30, 270, 470, 30))
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            self.mainPageUI.MP_Location.setStyleSheet("border: none;")
            self.mainPageUI.MP_Location.setGeometry(QtCore.QRect(30, 270, 470, 30))
   
    def prompt_browse_again(self):
        if len(self.displayed_users) == 1:
            QMessageBox.information(
                self.mainPageWindow,
                'Last User',
                'This is the last user available.'
            )
            return

        reply = QMessageBox.question(
            self.mainPageWindow,
            'No more users',
            'Do you want to browse again?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.displayed_users.clear()
            self.load_first_user()
        else:
            self.clear_user_display()

    def load_first_user(self):
        if self.first_user:
            self.displayed_users.add(self.first_user)
            self.load_next_user()
        

    def clear_user_display(self):
        self.mainPageUI.MP_Username.setText("")
        self.mainPageUI.MP_Age.setText("")
        self.mainPageUI.MP_Gender.setText("")
        self.mainPageUI.MP_Location.setText("")
        self.mainPageUI.MP_Preference1.setText("")
        self.mainPageUI.MP_Preference2.setText("")
        self.mainPageUI.MP_Preference3.setText("")
        self.mainPageUI.MP_Preference4.setText("")
        self.mainPageUI.MP_Preference5.setText("")
        self.mainPageUI.MP_Preference.setText("")

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
                response_data = response.json()
                added_user = response_data.get("added_user")
                self.show_success_message(f"{added_user} added!")
                self.displayed_users.add(added_user)  
                self.load_next_user()
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
        self.accountSettingsUI.set_user_info(self.logInUI.user_id, self.logInUI.username)
        self.friendMenuWindow.close()
        self.accountSettingsWindow.show()
    
    def openHomePageFromFriendMenu(self):
        try:
            response = requests.post('http://127.0.0.1:5000/logout')
            if response.status_code == 200:
                self.show_success_message("Logged out successfully")
              
                self.displayed_users = set()
            else:
                self.show_error_message("Logout failed", "Failed to log out. Please try again.")
        except requests.exceptions.RequestException as e:
            self.show_error_message("Logout failed", f"An error occurred: {e}")

        self.friendMenuWindow.close()
        self.homePageWindow.show()


    def fetch_pending_friend_requests(self):
        username = self.logInUI.username  

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
        accept_buttons = [
            self.friendMenuUI.FM_Accept1PB,
            self.friendMenuUI.FM_Accept2PB,
            self.friendMenuUI.FM_Accept3PB,
            self.friendMenuUI.FM_Accept4PB,
            self.friendMenuUI.FM_Accept5PB,
            self.friendMenuUI.FM_Accept6PB,
            self.friendMenuUI.FM_Accept7PB,
            self.friendMenuUI.FM_Accept8PB,
            self.friendMenuUI.FM_Accept9PB,
            self.friendMenuUI.FM_Accept10PB
        ]
        decline_buttons = [
            self.friendMenuUI.FM_Decline1PB,
            self.friendMenuUI.FM_Decline2PB,
            self.friendMenuUI.FM_Decline3PB,
            self.friendMenuUI.FM_Decline4PB,
            self.friendMenuUI.FM_Decline5PB,
            self.friendMenuUI.FM_Decline6PB,
            self.friendMenuUI.FM_Decline7PB,
            self.friendMenuUI.FM_Decline8PB,
            self.friendMenuUI.FM_Decline9PB,
            self.friendMenuUI.FM_Decline10PB
        ]

        for i, label in enumerate(friend_request_labels):
            if i < len(pending_requests):
                label.setText(_translate("FriendMenu", f"{pending_requests[i]}"))
                accept_buttons[i].setVisible(True)
                decline_buttons[i].setVisible(True)
            else:
                label.setText(_translate("FriendMenu", ""))
                accept_buttons[i].setVisible(False)
                decline_buttons[i].setVisible(False)
    

    def accept_friend_request(self, from_user):
        to_user = self.logInUI.username

        data = {
            'from_user': from_user,
            'to_user': to_user
        }

        try:
            response = requests.post('http://127.0.0.1:5000/accept_friend_request', json=data)
            if response.status_code == 200:
                self.show_success_message("Friend request accepted successfully")
                self.update_accepted_friends(from_user)
                self.remove_friend_request(from_user)
            else:
                error_message = response.json().get('error', 'Unknown error occurred')
                self.show_error_message(f"Error: {error_message}")
        except requests.exceptions.RequestException as e:
            self.show_error_message(f"Request failed: {str(e)}")

    def update_accepted_friends(self, accepted_friend):
        accepted_friends_labels = [
            self.friendMenuUI.FM_AcceptedFriend1,
            self.friendMenuUI.FM_AcceptedFriend2,
            self.friendMenuUI.FM_AcceptedFriend3,
            self.friendMenuUI.FM_AcceptedFriend4,
            self.friendMenuUI.FM_AcceptedFriend5,
            self.friendMenuUI.FM_AcceptedFriend6,
            self.friendMenuUI.FM_AcceptedFriend7,
            self.friendMenuUI.FM_AcceptedFriend8,
            self.friendMenuUI.FM_AcceptedFriend9,
            self.friendMenuUI.FM_AcceptedFriend10,
            self.friendMenuUI.FM_AcceptedFriend11,
            self.friendMenuUI.FM_AcceptedFriend12
        ]

        for label in accepted_friends_labels:
            if label.text() == "":
                label.setText(accepted_friend)
                break

    def decline_friend_request(self, from_user):
            to_user = self.logInUI.username


            data = {
                'from_user': from_user,
                'to_user': to_user
            }


            try:
                response = requests.post('http://127.0.0.1:5000/decline_friend_request', json=data)
                if response.status_code == 200:
                    self.show_success_message("Friend request declined successfully")
                    self.remove_friend_request(from_user)
                else:
                    error_message = response.json().get('error', 'Unknown error occurred')
                    self.show_error_message(f"Error: {error_message}")
            except requests.exceptions.RequestException as e:
                self.show_error_message(f"Request failed: {str(e)}")

    def decline_friend_request(self, from_user):
        to_user = self.logInUI.username

        data = {
            'from_user': from_user,
            'to_user': to_user
        }

        try:
            response = requests.post('http://127.0.0.1:5000/decline_friend_request', json=data)
            if response.status_code == 200:
                self.show_success_message("Friend request declined successfully")
                self.remove_friend_request(from_user)
            else:
                error_message = response.json().get('error', 'Unknown error occurred')
                self.show_error_message(f"Error: {error_message}")
        except requests.exceptions.RequestException as e:
            self.show_error_message(f"Request failed: {str(e)}")

    def remove_friend_request(self, from_user):
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
        accept_buttons = [
            self.friendMenuUI.FM_Accept1PB,
            self.friendMenuUI.FM_Accept2PB,
            self.friendMenuUI.FM_Accept3PB,
            self.friendMenuUI.FM_Accept4PB,
            self.friendMenuUI.FM_Accept5PB,
            self.friendMenuUI.FM_Accept6PB,
            self.friendMenuUI.FM_Accept7PB,
            self.friendMenuUI.FM_Accept8PB,
            self.friendMenuUI.FM_Accept9PB,
            self.friendMenuUI.FM_Accept10PB
        ]
        decline_buttons = [
            self.friendMenuUI.FM_Decline1PB,
            self.friendMenuUI.FM_Decline2PB,
            self.friendMenuUI.FM_Decline3PB,
            self.friendMenuUI.FM_Decline4PB,
            self.friendMenuUI.FM_Decline5PB,
            self.friendMenuUI.FM_Decline6PB,
            self.friendMenuUI.FM_Decline7PB,
            self.friendMenuUI.FM_Decline8PB,
            self.friendMenuUI.FM_Decline9PB,
            self.friendMenuUI.FM_Decline10PB
        ]
        for i, label in enumerate(friend_request_labels):
            if label.text() == from_user:
                label.setText("")
                accept_buttons[i].setVisible(False)
                decline_buttons[i].setVisible(False)
                break


    
    #NOTIFICATION WINDOW
    def open_notification_window(self):
      
        username = self.logInUI.username 
        users_added = self.fetch_users_added_notification()
        accepted_requests = self.fetch_accepted_friends()  
        pending_requests = self.fetch_pending_friend_requests_notification() 

        # Set the data in the notification window
        self.notificationWindow.set_users_added_notification(users_added)
        self.notificationWindow.set_accepted_requests_notification(accepted_requests)
        self.notificationWindow.set_pending_requests_notification(pending_requests or [])

        # Show the notification window
        self.notificationWindow.exec_()



    def fetch_users_added_notification(self):
        username = self.logInUI.username  

        try:
            response = requests.get('http://127.0.0.1:5000/get_users_added_notification', params={'username': username})
            if response.status_code == 200:
                return response.json().get('users_added', [])
            else:
                print(f"Error: Received status code {response.status_code}")
                print(f"Response content: {response.content}")
                self.show_error_message("Failed to fetch users added.")
                return []
        except requests.exceptions.RequestException as e:
            self.show_error_message(f"Request failed: {str(e)}")
            return []
        
    def fetch_accepted_friends(self):
        username = self.logInUI.username

        try:
            response = requests.get('http://127.0.0.1:5000/get_accepted_friends', params={'username': username})
            if response.status_code == 200:
                accepted_friends = response.json().get('accepted_friends', [])
                self.display_accepted_friends(accepted_friends)  
                return accepted_friends  
            else:
                print(f"Error: Received status code {response.status_code}")
                print(f"Response content: {response.content}")
                self.show_error_message("Failed to fetch accepted friends.")
                return []
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {str(e)}")
            self.show_error_message(f"Request failed: {str(e)}")
            return []
        

    def display_accepted_friends(self, accepted_friends):
        accepted_friends_labels = [
            self.friendMenuUI.FM_AcceptedFriend1,
            self.friendMenuUI.FM_AcceptedFriend2,
            self.friendMenuUI.FM_AcceptedFriend3,
            self.friendMenuUI.FM_AcceptedFriend4,
            self.friendMenuUI.FM_AcceptedFriend5,
            self.friendMenuUI.FM_AcceptedFriend6,
            self.friendMenuUI.FM_AcceptedFriend7,
            self.friendMenuUI.FM_AcceptedFriend8,
            self.friendMenuUI.FM_AcceptedFriend9,
            self.friendMenuUI.FM_AcceptedFriend10,
            self.friendMenuUI.FM_AcceptedFriend11,
            self.friendMenuUI.FM_AcceptedFriend12
        ]

        for i, label in enumerate(accepted_friends_labels):
            if i < len(accepted_friends):
                label.setText(accepted_friends[i])
            else:
                label.setText("")
    
    def remove_friend_request(self, from_user):
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
        for label in friend_request_labels:
            if label.text() == from_user:
                label.setText("")
                break
    
    def fetch_pending_friend_requests_notification(self):
        username = self.logInUI.username  

        try:
            response = requests.get('http://127.0.0.1:5000/get_pending_friend_requests_notification', params={'username': username})
            if response.status_code == 200:
                pending_requests = response.json().get('pending_requests', [])
                self.notificationWindow.set_pending_requests_notification(pending_requests)
                return pending_requests
            else:
                print(f"Error: Received status code {response.status_code}")
                print(f"Response content: {response.content}")
                self.show_error_message("Failed to fetch pending friend requests.")
                return []
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {str(e)}")
            self.show_error_message(f"Request failed: {str(e)}")
            return []
        

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

    def save_changes(self):
        new_email = self.accountSettingsUI.AS_EnterNewEmLE.text()
        confirm_email = self.accountSettingsUI.AS_ConfirmNewEmLE_.text()
        if new_email == confirm_email:
            print(f"New email: {new_email}, Confirm email: {confirm_email}")
            self.accountSettingsUI.change_email(new_email, confirm_email)
        else:
            print("email do not match. Please try again.")

        new_social_link = self.accountSettingsUI.AS_EnterNewSocialLinkLE.text()
        confirm_social_link = self.accountSettingsUI.AS_ConfirmNewSocialLinkLE.text()
        if new_social_link == confirm_social_link:
            print(f"New social link: {new_social_link}, Confirm social link: {confirm_social_link}")
            self.accountSettingsUI.change_social_link(new_social_link, confirm_social_link)
        else:
            print("Social links do not match. Please try again.")


    def go_to_home_page(self):
        if self.accountSettingsWindow:
            self.accountSettingsWindow.close()
        if self.homePageWindow:
            self.homePageWindow.show()



    # ChangeProifle methods
    def openAccountSettingsFromChangeProfile(self):
        self.changeProfileWindow.close()
        self.accountSettingsWindow.show()

    
   
    def run(self):
      
        splash = SplashScreen()
        if splash.exec_() == QDialog.Accepted:
            
            self.welcomePageWindow.show()
            sys.exit(self.app.exec_())

    def main():
        try:
            mainApp = MainApp()
        except Exception as e:
            print(f"Unhandled exception: {e}")
            traceback.print_exc()
            sys.exit(1)

def start_server():
    server_path = os.path.join(os.path.dirname(__file__), 'BACKEND', 'server.py')
    subprocess.Popen(['python', server_path])

if __name__ == "__main__":
    start_server()
    app = QApplication(sys.argv)
    mainApp = MainApp()
    mainApp.run()
    mainApp.run()



