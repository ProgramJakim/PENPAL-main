import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QWidget

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'FRONTEND')))
from SignUpPage import Ui_SignUp
from LogInPage import Ui_LogIn
from HomePage import Ui_Homepage

class MainApp:
    def __init__(self):
        # Create the application instance
        self.app = QApplication(sys.argv)

        # Create instances for all windows
        self.logInWindow = QMainWindow()
        self.signUpWindow = QMainWindow()
        self.homePageWindow = QWidget()

        # Setup UI for the login window
        self.logInUI = Ui_LogIn()
        self.logInUI.setupUi(self.logInWindow)

        # Setup UI for the signup window
        self.signUpUI = Ui_SignUp()
        self.signUpUI.setupUi(self.signUpWindow)

        # Setup UI for the homepage window
        self.homePageUI = Ui_Homepage()
        self.homePageUI.setupUi(self.homePageWindow)

        # Connect the "Sign Up" button to open the signup window
        self.logInUI.LI_SignUpPB.clicked.connect(self.openSignUpPage)

        # Connect the "Back to Login" button to go back to the login window
        self.signUpUI.SU_LogInPB.clicked.connect(self.backtoLogInPage)

    def openSignUpPage(self):
        # Hide the login window and show the signup window
        self.logInWindow.close()
        self.signUpWindow.show()

    def backtoLogInPage(self):
        # Close the signup window and show the login window
        self.signUpWindow.close()
        self.logInWindow.show()

    def run(self):
        # Show the homepage window initially
        self.homePageWindow.show()

        # Execute the app
        sys.exit(self.app.exec_())

# Run the application
if __name__ == "__main__":
    mainApp = MainApp()
    mainApp.run()