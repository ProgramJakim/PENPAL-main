import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from loginpage import Ui_LogIn  # Import the Login UI class

def main():
    app = QApplication(sys.argv)
    
    # Initialize the login window
    logInWindow = QMainWindow()
    ui = Ui_LogIn()
    ui.setupUi(logInWindow)
    
    # Show the login window
    logInWindow.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()