from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QApplication
from PyQt5.QtGui import QPixmap, QFont, QCursor
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QRect
import os
import math

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
        self.background_label.setFixedSize(1440, 850)

        # Set the background image
        current_directory = os.path.dirname(os.path.abspath(__file__))
        background_image_path = os.path.join(current_directory, '..', 'resources', 'images', 'WELCOME.png')
        if os.path.exists(background_image_path):
            self.background_label.setPixmap(QPixmap(background_image_path).scaled(1440, 850))
        else:
            print(f"Background image not found: {background_image_path}")

        # Add the background label to the content layout
        content_layout.addWidget(self.background_label)

        # Create the LogIn button
        self.LogIn_2 = QPushButton("Log In", content_widget)
        self.LogIn_2.setGeometry(QRect(1243, 523, 150, 45))
        font = QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LogIn_2.setFont(font)
        self.LogIn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.LogIn_2.setStyleSheet("""
            font:30px;
            color: #FFFFFF;
            border: 2px solid #FFFFFF;
            background: transparent;
            border-radius: 5px;
        """)
        self.LogIn_2.setObjectName("LogIn_2")

        # Create the SignUp button
        self.SignUp = QPushButton("Sign Up", content_widget)
        self.SignUp.setGeometry(QRect(1243, 594, 150, 45))
        self.SignUp.setFont(font)
        self.SignUp.setCursor(QCursor(Qt.PointingHandCursor))
        self.SignUp.setStyleSheet("""
            font:30px;
            color: #FFFFFF;
            border: 2px solid #FFFFFF;
            background: transparent;
            border-radius: 5px;
        """)
        self.SignUp.setObjectName("SignUp")

        

       
       

        # Set the layout of the main window
        main_layout = QVBoxLayout(WelcomePage)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(content_widget)
        WelcomePage.setLayout(main_layout)

        # Create a floating circle button outside the scroll area
        self.circle_button = QPushButton(WelcomePage)
        self.circle_button.setGeometry(1300, 750, 50, 50)
        self.circle_button.setStyleSheet("""
            border-radius: 25px;
            background-color: #FF9F89;
            font-size: 20px;
            color: white;
        """)
        self.circle_button.setText("+")

        # Create the buttons that will appear with animations outside the scroll area
        self.buttons = []
        button_labels = ["Page 1", "Page 2", "Page 3", "Page 4", "Page 5"]
        button_colors = ["#4CAF50", "#008CBA", "#f44336", "#FFC107", "#9C27B0"]
        for i, label in enumerate(button_labels):
            button = QPushButton(label, WelcomePage)
            button.setGeometry(1300, 750, 50, 50)  # Initially place buttons at the circle position
            button.setStyleSheet(f"""
                background-color: {button_colors[i]};
                border: none;
                color: white;
                text-align: center;
                font-size: 15px;
                border-radius: 25px;
            """)
            button.hide()
            self.buttons.append(button)

        # Add an attribute to store animations
        self.animations = []

        # Connect the circle button to the method to show/hide buttons with animations
        self.circle_button.clicked.connect(self.toggle_buttons)

        # Connect the buttons to their respective methods for redirection
        self.buttons[0].clicked.connect(lambda: self.open_page("Page 1"))
        self.buttons[1].clicked.connect(lambda: self.open_page("Page 2"))
        self.buttons[2].clicked.connect(lambda: self.open_page("Page 3"))
        self.buttons[3].clicked.connect(lambda: self.open_page("Page 4"))
        self.buttons[4].clicked.connect(lambda: self.open_page("Page 5"))

    def toggle_buttons(self):
        # Clear previous animations to prevent memory leaks
        self.animations.clear()

        if self.buttons[0].isVisible():
            # Animate buttons back to the circle button position and hide them
            for button in self.buttons:
                self.animate_button(button, 1300, 750, hide=True)
            self.circle_button.setText("+")
        else:
            # Arrange buttons in a closer circular pattern around the circle button
            radius = 60  # Reduced radius for closer arrangement
            angle_step = 360 / len(self.buttons)  # Divide full circle by the number of buttons
            for i, button in enumerate(self.buttons):
                angle = angle_step * i
                x = 1300 + int(radius * math.cos(math.radians(angle)))
                y = 750 + int(radius * math.sin(math.radians(angle)))
                self.animate_button(button, x, y, hide=False)
            self.circle_button.setText("-")

    def animate_button(self, button, x, y, hide):
        button.show()
        animation = QPropertyAnimation(button, b"pos")
        animation.setDuration(250)
        animation.setStartValue(button.pos())
        animation.setEndValue(QPoint(x, y))
        animation.start()

        # Hide the button after animation if required
        if hide:
            animation.finished.connect(button.hide)

        # Store the animation to prevent it from being garbage-collected
        self.animations.append(animation)

    def open_page(self, page_name):
        welcome_page = QDialog()
        welcome_page.setWindowTitle(page_name)
        welcome_page.setFixedSize(400, 300)
        label = QLabel(f"Welcome to {page_name}", welcome_page)
        label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout(welcome_page)
        layout.addWidget(label)
        welcome_page.exec_()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    WelcomePage = QWidget()
    ui = Ui_WelcomePage()
    ui.setupUi(WelcomePage)
    WelcomePage.show()
    sys.exit(app.exec_())