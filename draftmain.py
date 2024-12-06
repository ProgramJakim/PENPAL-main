import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from LogInPage import Ui_LogIn  # Import the LogIn UI from the LogInPage.py file


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create an instance of the Ui_LogIn class
        self.ui = Ui_LogIn()
        self.ui.setupUi(self)  # Setup the UI of the LogInPage in the main window

        # Set window properties
        self.setWindowTitle("PenPal - Log In")
        self.setGeometry(100, 100, 1440, 780)  # Set window size and position


def run_app():
    app = QApplication(sys.argv)  # Initialize the application
    window = MainWindow()  # Create an instance of MainWindow
    window.show()  # Show the window
    sys.exit(app.exec_())  # Start the application event loop


if __name__ == "__main__":
    run_app()