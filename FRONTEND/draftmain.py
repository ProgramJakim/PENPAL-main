import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from SignUpPage import Ui_SignUp
from LogInPage import Ui_LogIn

class MainApp:
    def __init__(self):
        # Create the application instance
        self.app = QApplication(sys.argv)

        # Create instances for both windows
        self.logInWindow = QMainWindow()
        self.signUpWindow = QMainWindow()

        # Setup UI for the login window
        self.logInUI = Ui_LogIn()
        self.logInUI.setupUi(self.logInWindow)

        # Setup UI for the signup window
        self.signUpUI = Ui_SignUp()
        self.signUpUI.setupUi(self.signUpWindow)

        # Connect the "Sign Up" button to open the signup window
        self.logInUI.LI_SignUpPB.clicked.connect(self.openSignUpPage)

    def openSignUpPage(self):
        # Hide the login window and show the signup window
        self.logInWindow.hide()
        self.signUpWindow.show()

    def run(self):
        # Show the login window
        self.logInWindow.show()

        # Execute the app
        sys.exit(self.app.exec_())

# Run the application
if __name__ == "__main__":
    mainApp = MainApp()
    mainApp.run()