from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QApplication, QSizePolicy
from PyQt5.QtGui import QPixmap, QFont, QCursor
from PyQt5.QtCore import Qt, QRect
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'FRONTEND')))
from HomePage import Ui_Homepage

class Ui_WelcomePage(object):
    def setupUi(self, WelcomePage):
        # Set the fixed size of the main window
        WelcomePage.setFixedSize(1440, 850)
        WelcomePage.setObjectName("WelcomePage")

        # Create a widget to hold the content
        content_widget = QWidget(WelcomePage)
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)

       # Create a label to hold the background image
        self.background_label = QLabel(content_widget)
        self.background_label.setFixedSize(1700, 900)

        # Set the background image
        current_directory = os.path.dirname(os.path.abspath(__file__))
        background_image_path = os.path.join(current_directory, '..', 'resources', 'images', 'WELCOMEPAGE.png')
        if os.path.exists(background_image_path):
            self.background_label.setPixmap(QPixmap(background_image_path).scaled(1700, 900))
        else:
            print(f"Background image not found: {background_image_path}")

        # Add the background label to the content layout
        content_layout.addWidget(self.background_label)

        # Add the background label to the content layout
        content_layout.addWidget(self.background_label)

        # Create the Press To Continue button
        self.press_to_continue = QPushButton("PRESS TO CONTINUE", content_widget)
        self.press_to_continue.setGeometry(QRect(959, 613, 230, 60))
        font = QFont()
        font.setPointSize(30)
        self.press_to_continue.setFont(font)
        self.press_to_continue.setCursor(QCursor(Qt.PointingHandCursor))
        self.press_to_continue.setStyleSheet("""
            QPushButton {
                font:20px;
                color: #9E2932;
                border: 3px solid #9E2932; 
                background: transparent;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #9E2932;
                color: #FFFFFF;
            }
        """)
        self.press_to_continue.setObjectName("PressToContinue")

        # Connect the button to the method to open the homepage
        self.press_to_continue.clicked.connect(self.open_homepage)

        # Set the layout of the main window
        main_layout = QVBoxLayout(WelcomePage)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(content_widget)
        WelcomePage.setLayout(main_layout)


    def open_page(self, page_name):
        welcome_page = QDialog()
        welcome_page.setWindowTitle(page_name)
        welcome_page.setFixedSize(400, 300)
        label = QLabel(f"Welcome to {page_name}", welcome_page)
        label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout(welcome_page)
        layout.addWidget(label)
        welcome_page.exec_()

    def open_homepage(self):
        self.homepage_window = QDialog()
        self.ui = Ui_Homepage()
        self.ui.setupUi(self.homepage_window)
        self.homepage_window.hide()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    WelcomePage = QWidget()
    ui = Ui_WelcomePage()
    ui.setupUi(WelcomePage)
    WelcomePage.show()
    sys.exit(app.exec_())