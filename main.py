import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'FRONTEND')))
from SignUpPage import Ui_SignUp
from LogInPage import Ui_LogIn
from HomePagetry import Ui_Homepage

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

    def openMainAppWindow(self):
        # Close the login window after login
        self.logInWindow.close()

        # Create a QWidget for the Homepage
        self.mainAppWindow = QtWidgets.QWidget()  # Create a QWidget (not just the UI layout)
        self.ui = Ui_Homepage()  # Create the Ui_Homepage object
        self.ui.setupUi(self.mainAppWindow)  # Set up the UI layout for the QWidget
        self.mainAppWindow.show()  # Show the QWidget containing the UI layout

       

    def run(self):
        # Show the login window
        self.logInWindow.show()

        # Execute the app
        sys.exit(self.app.exec_())



# Run the application
if __name__ == "__main__":
    mainApp = MainApp()
    mainApp.run()