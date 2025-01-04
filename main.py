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
from FriendMenu import Ui_FriendMenu

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
        self.friendMenuWindow = QDialog()

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



        # Setup UI for the account settings window
        self.accountSettingsUI = Ui_AccountSettings()
        self.accountSettingsUI.setupUi(self.accountSettingsWindow)
        
        # Setup UI for the Change Profile window
        self.changeProfileUI = Ui_ChangeProfile()
        self.changeProfileUI.setupUi(self.changeProfileWindow)

        # Setup UI for the friend menu window 
        self.friendMenuUI = Ui_FriendMenu()
        self.friendMenuUI.setupUi(self.friendMenuWindow)

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


        # Connect the "Home" button in Account Settings to go back to the Home Page
        self.accountSettingsUI.AS_HomePB.clicked.connect(self.openHomePageFromAccountSettings)


        # Connect the "PROFILE" button in the main page to open the account settings page
        self.mainPageUI.MP_ProfilePB.clicked.connect(self.openAccountSettingsFromFriendMenu)


        # Connect the "Profile" button in the FriendMenu window to go to the AccountSettings window
        self.friendMenuUI.FM_ProfilePB.clicked.connect(self.openAccountSettingsFromFriendMenu)


        #CLICKABLE BUTTON FOR CONTINUE
        self.interestPageUI.INTpushButton.clicked.connect(self.on_continue_clicked)

        #CLICKABLE PROFILE BUTTON
        self.mainPageUI.MP_ProfilePB.clicked.connect(self.on_profile_button_click)

        # Connect the "Menu" button in the main page to open the friend menu window
        self.mainPageUI.MP_MenuPB.clicked.connect(self.openFriendMenu)

        # Connect the "Home" button in the FriendMenu window to go back to the MainPage
        self.friendMenuUI.FM_HomePB.clicked.connect(self.openMainPageFromFriendMenu)

        #connect the "MENU" button on the account settings window to go back to the friend menu window
        self.accountSettingsUI.AS_MenuPB.clicked.connect(self.openFriendMenuFromAccountSettings)

        # Connect the "Log Out" button in the main page to go back to the home page
        self.mainPageUI.MP_LogoutPB.clicked.connect(self.openHomePageFromMainPage)

        # account settings log out
        self.accountSettingsUI.AS_LogOutPB.clicked.connect(self.openHomepageFromAccountSettings)

        # friend menu log out 
        self.friendMenuUI.FM_LogOutPB.clicked.connect(self.openHomePageFromFriendMenu)

    def on_profile_button_click(self):
        self.mainPageWindow.close()
        self.accountSettingsWindow.show()

        # FriendMenu Buttons
        self.friendMenuUI.FM_HomePB.clicked.connect(self.openMainPageFromFriendMenu)
        self.friendMenuUI.FM_LogOutPB.clicked.connect(self.openHomePageFromFriendMenu)
        self.friendMenuUI.FM_ProfilePB.clicked.connect(self.openAccountSettingsFromFrienMenu)

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
    def openMAINPage(self):
        # Assuming user_id and username are obtained after successful login
        user_id = self.logInUI.user_id  # Replace with actual user_id
        username = self.logInUI.username  # Replace with actual username

        # Set user info in the main page UI
        self.mainPageUI.set_user_info(user_id, username)

        # Show the main page window
        self.logInWindow.close()
        self.mainPageWindow.show()
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

    
    def openMainPage(self):
        self.interestPageWindow.close()
        self.mainPageWindow.show()

    #MAINPAGE methods

    def openAccountSettings(self):
        self.accountSettingsUI.set_user_info(self.logInUI.user_id, self.logInUI.username)
        self.mainPageWindow.close()
        self.accountSettingsWindow.show()
    def openFriendMenu(self):
        self.mainPageWindow.close()
        self.friendMenuWindow.show()
    def openHomePageFromMainPage(self):
        # Close the Main Page window and show the Home Page window
        self.mainPageWindow.close()
        self.homePageWindow.show()


    # AccountSettings methods
    def openMAINPAGEfromAccountSettings(self):
        self.accountSettingsWindow.close()
        self.mainPageWindow.show()
    def openFriendMenuFromAccountSettings(self):
        self.accountSettingsWindow.close()
        self.friendMenuWindow.show()
    def openHomepageFromAccountSettings(self):
        self.accountSettingsWindow.close()
        self.homePageWindow.show()
    def openChangeProfileFromAccountSettings(self):
        self.accountSettingsWindow.close()
        self.changeProfileWindow.show()

    # FriendMenu methods
    def openMainPageFromFriendMenu(self):
        self.friendMenuWindow.close()
        self.mainPageWindow.show()
    def openAccountSettingsFromFrienMenu(self):
        self.friendMenuWindow.close()
        self.accountSettingsWindow.show()
    def openHomePageFromFriendMenu(self):
        self.friendMenuWindow.close()
        self.homePageWindow.show()

    # ChangeProifle methods
    def openAccountSettingsFromChangeProfile(self):
        self.changeProfileWindow.close()
        self.accountSettingsWindow.show()

    def openFriendMenu(self):
    # Close the main page window and show the friend menu window
        self.mainPageWindow.close()
        self.friendMenuWindow.show()

    def openMainPageFromFriendMenu(self):
        # Close the Friend Menu window and show the Main Page window
        self.friendMenuWindow.close()
        self.mainPageWindow.show()

    def openAccountSettingsFromFriendMenu(self):
        # Close the Friend Menu window and show the Account Settings windoww
        self.friendMenuWindow.close()
        self.accountSettingsWindow.show()

    def openFriendMenuFromAccountSettings(self):
        # Close the Account Settings window and show the Friend Menu window
        self.accountSettingsWindow.close()
        self.friendMenuWindow.show()

    def openHomePageFromMainPage(self):
        # Close the Main Page window and show the Home Page window
        self.mainPageWindow.close()
        self.homePageWindow.show()

    def openHomepageFromAccountSettings(self):
        self.accountSettingsWindow.close()
        self.homePageWindow.show()

    def openHomePageFromFriendMenu(self):
        self.friendMenuWindow.close()
        self.homePageWindow.show()
    
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



