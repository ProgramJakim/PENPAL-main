from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QApplication, QSpacerItem, QSizePolicy, QWidget
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import sys
import os

class ListItemWidget(QWidget):
    def __init__(self, text, image_path, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        
        # Profile picture
        self.image_label = QLabel(self)
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.image_label.setFixedWidth(50)  # Set fixed width for the profile picture
        layout.addWidget(self.image_label)
        
        # Username
        self.text_label = QLabel(text, self)
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.text_label.setFont(font)
        layout.addWidget(self.text_label)

         # Add left margin to the text label
        self.text_label.setContentsMargins(5, 0, 0, 0)
        layout.addWidget(self.text_label)

class NotificationWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Notifications")
        self.setFixedSize(900, 800)

        # Set background image
        background_image_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'images', 'Notification Page.png')
        if os.path.exists(background_image_path):
            self.background_label = QLabel(self)
            self.background_label.setGeometry(0, 0, 900, 800)
            pixmap = QPixmap(background_image_path)
            self.background_label.setPixmap(pixmap)
            self.background_label.setScaledContents(True)
        else:
            print(f"Background image not found at: {background_image_path}")

         

        self.accepted_requests_list = QListWidget(self)
        self.accepted_requests_list.setGeometry(0, 140, 475, 290)  # Set geometry (x, y, width, height)
        self.accepted_requests_list.setStyleSheet("background-color: #FCF2F3; border: none;")  # Set container background to white
        self.accepted_requests_list.setStyleSheet("""
            background-color: #FCF2F3; 
            border: none;
            QScrollBar:vertical {
                background: #FFC0CB;
                width: 16px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #FF69B4;
                min-height: 20px;
                border-radius: 8px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
                height: 0px;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)  # Set container background to white and customize scrollbar

      
        self.pending_requests_list = QListWidget(self)
        self.pending_requests_list.setGeometry(0, 430, 475, 300)  # Set geometry (x, y, width, height)
        self.pending_requests_list.setStyleSheet("background-color: #FCF2F3; border: none;")  # Set container background to white
        self.pending_requests_list.setStyleSheet("""
            background-color: #FCF2F3; 
            border: none;
            QScrollBar:vertical {
                background: #FFC0CB;
                width: 16px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #FF69B4;
                min-height: 20px;
                border-radius: 8px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
                height: 0px;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)  # Set container background to white and customize scrollbar



        self.users_added_list = QListWidget(self)
        self.users_added_list.setGeometry(480, 140, 425, 590)  # Set geometry (x, y, width, height)
        self.users_added_list.setStyleSheet("""
            background-color: #FCF2F3; 
            border: none;
            QScrollBar:vertical {
                background: #FFC0CB;
                width: 16px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #FF69B4;
                min-height: 20px;
                border-radius: 8px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
                height: 0px;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)  # Set container background to white and customize scrollbar


    def set_users_added_notification(self, users):
        self.users_added_list.clear()
        image_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'images', 'DefaultProfile.png')
        for user in users:
            item_text = f"You added {user}!"
            item = QListWidgetItem(self.users_added_list)
            widget = ListItemWidget(item_text, image_path)
            item.setSizeHint(widget.sizeHint())
            self.users_added_list.setItemWidget(item, widget)

    def set_accepted_requests_notification(self, requests):
        self.accepted_requests_list.clear()
        image_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'images', 'DefaultProfile.png')
        for username in requests:
            item_text = f"{username} Accepted you! You're now friends"
            item = QListWidgetItem(self.accepted_requests_list)
            widget = ListItemWidget(item_text, image_path)
            item.setSizeHint(widget.sizeHint())
            self.accepted_requests_list.setItemWidget(item, widget)


    def set_pending_requests_notification(self, requests):
        self.pending_requests_list.clear()
        image_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'images', 'DefaultProfile.png')
        print(f"Setting pending requests: {requests}")  # Debugging line
        for username in requests:
            item_text = f"{username} Added you!"
            item = QListWidgetItem(self.pending_requests_list)
            widget = ListItemWidget(item_text, image_path)
            item.setSizeHint(widget.sizeHint())
            self.pending_requests_list.setItemWidget(item, widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotificationWindow()
    window.set_users_added(["User1", "User2", "User3"])  # Example data
    window.set_accepted_requests(["Friend1", "Friend2"])  # Example data
    window.set_pending_requests(["User4", "User5"])  # Example data
    window.show()
    sys.exit(app.exec_())