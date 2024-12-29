#annie
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, QGraphicsOpacityEffect
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, QTimer
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'FRONTEND')))
from SignUpPage import Ui_SignUp
from LogInPage import Ui_LogIn
from HomePage import Ui_Homepage
from WelcomePage import Ui_WelcomePage
from InterestPage import Ui_Dialog as Ui_InterestPage
from MAINPAGE import Ui_Main_Page
from AccountSettings import Ui_AccountSettings
from FriendMenu import Ui_FriendMenu

class SplashScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 600)
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

        # Setup UI for the WelcomePage window
        self.welcomePageUI = Ui_WelcomePage()
        self.welcomePageUI.setupUi(self.welcomePageWindow)


        # Setup UI for the login window
        self.logInUI = Ui_LogIn()
        self.logInUI.setupUi(self.logInWindow)


        # Setup UI for the signup window
        self.signUpUI = Ui_SignUp()
        self.signUpUI.setupUi(self.signUpWindow)


        # Setup UI for the homepage window
        self.homePageUI = Ui_Homepage()
        self.homePageUI.setupUi(self.homePageWindow)


        # Setup UI for the interest page window
        self.interestPageUI = Ui_InterestPage()
        self.interestPageUI.setupUi(self.interestPageWindow)


        # Setup UI for the main page window
        self.mainPageUI = Ui_Main_Page()
        self.mainPageUI.setupUi(self.mainPageWindow)


        # Setup UI for the account settings window
        self.accountSettingsUI = Ui_AccountSettings()
        self.accountSettingsUI.setupUi(self.accountSettingsWindow)

        # Setup UI for the friend menu window 
        self.friendMenuUI = Ui_FriendMenu()
        self.friendMenuUI.setupUi(self.friendMenuWindow)

        # Connect the "Sign Up" button to open the signup window
        self.logInUI.LI_SignUpPB.clicked.connect(self.openSignUpPage)


        # Connect the "Back to Login" button to go back to the login window
        self.signUpUI.SU_LogInPB.clicked.connect(self.backtoLogInPage)


        # Connect the "Log In" button on the homepage to open the login window
        self.homePageUI.LogIn_2.clicked.connect(self.openLogInPageFromHomepage)


        # Connect the "Log In" button on the login page to open the interest page
        self.logInUI.LI_LogInPB.clicked.connect(self.openInterestPage)


        # Connect the "Sign Up" button on the homepage to open the signup window
        self.homePageUI.SignUp.clicked.connect(self.openSignupFromHomepage)


        # Connect the button to the method to open the homepage
        self.welcomePageUI.press_to_continue.clicked.connect(self.open_homepagefromwelcome)


        # Connect the "CONTINUE" button in the interest page to open the main page
        self.interestPageUI.INTpushButton.clicked.connect(self.openMainPage)


        # Connect the "Home" button in Account Settings to go back to the Home Page
        self.accountSettingsUI.AS_HomePB.clicked.connect(self.openHomePageFromAccountSettings)


        # Connect the "PROFILE" button in the main page to open the account settings page
        self.mainPageUI.MP_ProfilePB.clicked.connect(self.openAccountSettingsFromFriendMenu)


        # Connect the "Menu" button in the Account Settings window to go to the friend menu
        self.accountSettingsUI.AS_HomePB.clicked.connect(self.openAccountSettingsFromFriendMenu)

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

    def on_profile_button_click(self):
        self.mainPageWindow.close()
        self.accountSettingsWindow.show()

    def on_continue_clicked(self):
        self.interestPageWindow.close()
        self.mainPageWindow.show()


    def open_homepagefromwelcome(self):
        self.welcomePageWindow.close()
        self.homePageWindow.show()


    def openSignupFromHomepage(self):
        self.homePageWindow.close()
        self.signUpWindow.show()


    def openLogInPageFromHomepage(self):
        # Close the homepage window and show the login window
        self.homePageWindow.close()
        self.logInWindow.show()


    def openSignUpPage(self):
        # Hide the login window and show the signup window
        self.logInWindow.close()
        self.signUpWindow.show()

    def backtoLogInPage(self):
        # Close the signup window and show the login window
        self.signUpWindow.close()
        self.logInWindow.show()
   
    def openInterestPage(self):
        # Close the login window and show the interest page window
        self.logInWindow.close()
        self.interestPageWindow.show()


    def openMainPage(self):
        # Close the interest page window and show the main page window
        self.interestPageWindow.close()
        self.mainPageWindow.show()


    def openAccountSettings(self):
        # Close the main page window and show the account settings window
        self.mainPageWindow.close()
        self.accountSettingsWindow.show()
    
    def openHomePageFromAccountSettings(self):
        # Close the Account Settings window and open the Home Page
        self.accountSettingsWindow.close()
        self.mainPageWindow.show()

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

