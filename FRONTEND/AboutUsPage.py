from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QApplication, QPushButton, QDialog
from PyQt5.QtGui import QPixmap, QFont, QCursor
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QRect
import os
import math

class Ui_AboutUs(object):
    def setupUi(self, AboutUs):
        # Set the fixed size of the main window
        AboutUs.setFixedSize(1440, 780)

        # Create a scroll area
        scroll_area = QScrollArea(AboutUs)
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


        # Create the BACK button
        self.SignUp = QPushButton("BACK", content_widget)
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
        self.SignUp.setObjectName("Back")


        # Set the content widget as the scroll area's widget
        scroll_area.setWidget(content_widget)

        # Set the layout of the main window
        main_layout = QVBoxLayout(AboutUs)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(scroll_area)
        AboutUs.setLayout(main_layout)


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
    AboutUs = QWidget()
    ui = Ui_AboutUs()
    ui.setupUi(AboutUs)
    AboutUs.show()
    sys.exit(app.exec_())
