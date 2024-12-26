import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QPushButton, QVBoxLayout, QLabel, QScrollArea
from PyQt5.QtGui import QPixmap, QFont, QCursor
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QRect
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'FRONTEND')))
from SignUpPage import Ui_SignUp
from LogInPage import Ui_LogIn
from HomePage import Ui_Homepage
from WelcomePage import Ui_WelcomePage
from InterestPage import Ui_Dialog as Ui_InterestPage

class MainApp:
    def __init__(self):
        # Create the application instance
        self.app = QApplication(sys.argv)

        # Create instances for all windows
        self.logInWindow = QMainWindow()
        self.signUpWindow = QMainWindow()
        self.homePageWindow = QWidget()
        self.interestPageWindow = QDialog()
        self.welcomePageWindow = QWidget()

        # Setup UI for the WelcomePage window
        self.welcomePageWindow = QWidget()
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

        # Connect the "Sign Up" button to open the signup window
        self.logInUI.LI_SignUpPB.clicked.connect(self.openSignUpPage)

        # Connect the "Back to Login" button to go back to the login window
        self.signUpUI.SU_LogInPB.clicked.connect(self.backtoLogInPage)

        # Connect the "Log In" button on the homepage to open the login window
        self.homePageUI.LogIn_2.clicked.connect(self.openLogInPageFromHomepage)

        # Connect the "Log In" button on the login page to open the interest page
        self.logInUI.LI_LogInPB.clicked.connect(self.openInterestPage)

        # Connect the "Sign Up" button on the homepage to open the signup window
        self.homePageUI.SignUp.clicked.connect(self.openSignupHomepage)

        # Connect the button to the method to open the homepage
        self.welcomePageUI.press_to_continue.clicked.connect(self.open_homepagefromwelcome)


    def open_homepagefromwelcome(self):
        self.welcomePageWindow.close()
        self.homePageWindow.show()


    def openSignupHomepage(self):
        self.homePageWindow.close()
        self.signUpWindow.show()


    def openSignUpPage(self):
        # Hide the login window and show the signup window
        self.logInWindow.close()
        self.signUpWindow.show()

    def backtoLogInPage(self):
        # Close the signup window and show the login window
        self.signUpWindow.close()
        self.logInWindow.show()

    def openLogInPageFromHomepage(self):
        # Close the homepage window and show the login window
        self.homePageWindow.close()
        self.logInWindow.show()

    def openInterestPage(self):
        # Close the login window and show the interest page window
        self.logInWindow.close()
        self.interestPageWindow.show()

    def run(self):
        # Show the homepage window initially
        self.welcomePageWindow.show()
        
        

        # Execute the app
        sys.exit(self.app.exec_())

# Run the application
if __name__ == "__main__":
    mainApp = MainApp()
    mainApp.run()