from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QApplication, QPushButton, QDialog
from PyQt5.QtGui import QPixmap, QFont, QCursor
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QRect
import os
import math

class Ui_Homepage(object):
    def setupUi(self, Homepage):
        # Set the fixed size of the main window
        Homepage.setFixedSize(1450, 900)

        # Create a scroll area
        scroll_area = QScrollArea(Homepage)
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Disable horizontal scrolling

        # Style the scrollbar
        scroll_area.setStyleSheet("""
            QScrollBar:vertical {
                border-radius: 15px;
                border: 4px solid #DD5B6E;
                background: rgba(255, 159, 137, 0.00);
                width: 22px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                border: 4px solid #DD5B6E;
                border-radius: 15px;
                background: #FF9F89;
                min-height: 20px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
                height: 0px;
            }
        """)

        # Create a widget to hold the content
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)

        # Create a label to hold the background image
        self.background_label = QLabel(content_widget)
        self.background_label.setFixedSize(1426, 4104)

        # Set the background image
        current_directory = os.path.dirname(os.path.abspath(__file__))
        background_image_path = os.path.join(current_directory, '..', 'resources', 'images', 'ABOUT US.png')
        if os.path.exists(background_image_path):
            self.background_label.setPixmap(QPixmap(background_image_path).scaled(1440, 4104))
        else:
            print(f"Background image not found: {background_image_path}")

        # Add the background label to the content layout
        content_layout.addWidget(self.background_label)

         # Create the LogIn button
        self.LogIn_2 = QPushButton("Log In", content_widget)
        self.LogIn_2.setGeometry(QRect(1091, 75, 150, 45))
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
        self.SignUp.setGeometry(QRect(1252, 75, 150, 45))
        font = QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
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


        # Set the content widget as the scroll area's widget
        scroll_area.setWidget(content_widget)

        # Set the layout of the main window
        main_layout = QVBoxLayout(Homepage)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(scroll_area)
        Homepage.setLayout(main_layout)

        # Create a floating circle button
        self.circle_button = QPushButton(Homepage)
        self.circle_button.setGeometry(1300, 750, 50, 50)
        self.circle_button.setStyleSheet("""
            border-radius: 25px;
            background-color: #FF9F89;
            font-size: 20px;
            color: white;
        """)
        self.circle_button.setText("+")

        # Create the buttons that will appear with animations
        self.buttons = []
        button_labels = ["Page 1", "Page 2", "Page 3", "Page 4", "Page 5"]
        button_colors = ["#4CAF50", "#008CBA", "#f44336", "#FFC107", "#9C27B0"]
        for i, label in enumerate(button_labels):
            button = QPushButton(label, Homepage)
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
        new_window = QDialog()
        new_window.setWindowTitle(page_name)
        new_window.setFixedSize(400, 300)
        label = QLabel(f"Welcome to {page_name}", new_window)
        label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout(new_window)
        layout.addWidget(label)
        new_window.exec_()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Homepage = QWidget()
    ui = Ui_Homepage()
    ui.setupUi(Homepage)
    Homepage.show()
    sys.exit(app.exec_())