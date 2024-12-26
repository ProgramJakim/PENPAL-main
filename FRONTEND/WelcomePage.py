from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QApplication, QSizePolicy, QGraphicsOpacityEffect, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap, QFont, QCursor
from PyQt5.QtCore import Qt, QRect, QPropertyAnimation, QTimer
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
        background_image_path = os.path.join(current_directory, '..', 'resources', 'images', 'POPUP.png')
        if os.path.exists(background_image_path):
            self.background_label.setPixmap(QPixmap(background_image_path).scaled(1450, 900))
        else:
            print(f"Background image not found: {background_image_path}")

        # Add the background label to the content layout
        content_layout.addWidget(self.background_label)

        # Add the background label to the content layout
        content_layout.addWidget(self.background_label)

      
        # Create the Press To Continue button
        self.press_to_continue = QPushButton("PRESS TO CONTINUE", content_widget)
        self.press_to_continue.setGeometry(QRect(613, 613, 290, 100))
        font = QFont()
        font.setPointSize(50)
        self.press_to_continue.setFont(font)
        self.press_to_continue.setCursor(QCursor(Qt.PointingHandCursor))
        self.press_to_continue.setStyleSheet("""
            QPushButton {
                font:28px;
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
        self.homepage_window.show()

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
        logo_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'images', 'Icon.png')
        if os.path.exists(logo_path):
            self.logo_label.setPixmap(QPixmap(logo_path).scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(self.logo_label, alignment=Qt.AlignCenter)

        # Add system name
        self.label = QLabel("Penpal:\nA Social Media\n Friend Recommendation System", self)
        self.label.setGeometry(300, 600, 200, 700)  # Set the x, y position and width, height of the label
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

if __name__ == "__main__":
    app = QApplication(sys.argv)

    splash = SplashScreen()
    if splash.exec_() == QDialog.Accepted:
        WelcomePage = QWidget()
        ui = Ui_WelcomePage()
        ui.setupUi(WelcomePage)
        WelcomePage.show()

    sys.exit(app.exec_())