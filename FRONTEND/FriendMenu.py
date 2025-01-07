from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QPushButton, QApplication, QSpacerItem, QSizePolicy, QWidget
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QMetaObject, QCoreApplication
from PyQt5 import QtCore, QtWidgets, QtGui
import sys
import os

# Get the absolute path of the current directory (LogInPage.py)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Build the general path to the resources/images folder
images_folder = os.path.join(current_directory, '..', 'resources', 'images')

class FriendRequestItemWidget(QWidget):
    def __init__(self, username, image_path, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        
        # Profile picture
        self.FM_Profile = QLabel(self)
        pixmap = QPixmap(image_path)
        self.FM_Profile.setPixmap(pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.FM_Profile.setFixedWidth(50)  # Set fixed width for the profile picture
        layout.addWidget(self.FM_Profile)
        
        # Username
        self.FM_Username = QLabel(username, self)
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.FM_Username.setFont(font)
        layout.addWidget(self.FM_Username)

        # Add left margin to the text label
        self.FM_Username.setContentsMargins(5, 0, 0, 0)
        layout.addWidget(self.FM_Username)

        # Accept button
        self.FM_AcceptButton = QPushButton("Accept", self)
        self.FM_AcceptButton.setStyleSheet("background-color: #4CAF50; color: white;")
        layout.addWidget(self.FM_AcceptButton)

        # Decline button
        self.FM_DeclineButton = QPushButton("Decline", self)
        self.FM_DeclineButton.setStyleSheet("background-color: #f44336; color: white;")
        layout.addWidget(self.FM_DeclineButton)

class Ui_FriendMenu(object):
    def setupUi(self, FriendMenu):
        FriendMenu.setObjectName("FriendMenu")
        FriendMenu.resize(1440, 780)
        FriendMenu.setStyleSheet("background-color: rgb(255, 249, 240);")

        # Header
        self.FM_Header = QtWidgets.QFrame(FriendMenu)
        self.FM_Header.setGeometry(QtCore.QRect(0, 0, 1440, 105))
        self.FM_Header.setStyleSheet("background: qlineargradient(\n"
                                     "    spread:pad, \n"
                                     "    x1:0, y1:0, x2:1, y2:0, \n"
                                     "    stop:0 #EDC27E, \n"
                                     "    stop:0.526 #EDC27E, \n"
                                     "    stop:1 #DC586D\n"
                                     ");\n"
                                     "\n"
                                     "")
        self.FM_Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FM_Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FM_Header.setObjectName("FM_Header")

        # Header Icon
        self.FM_HeaderIcon = QtWidgets.QLabel(self.FM_Header)
        self.FM_HeaderIcon.setGeometry(QtCore.QRect(-50, -30, 242, 159))
        self.FM_HeaderIcon.setStyleSheet("background:transparent;\n"
                                         "")
        self.FM_HeaderIcon.setText("")
        self.FM_HeaderIcon.setPixmap(QtGui.QPixmap(os.path.join(images_folder, "HeaderIcon.png")))
        self.FM_HeaderIcon.setScaledContents(True)
        self.FM_HeaderIcon.setObjectName("FM_HeaderIcon")

        # Friend Request List
        self.FM_FriendRequestList = QListWidget(FriendMenu)
        self.FM_FriendRequestList.setGeometry(QtCore.QRect(140, 140, 711, 600))
        self.FM_FriendRequestList.setStyleSheet("""
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

        self.retranslateUi(FriendMenu)
        QMetaObject.connectSlotsByName(FriendMenu)

    def retranslateUi(self, FriendMenu):
        _translate = QtCore.QCoreApplication.translate
        FriendMenu.setWindowTitle(_translate("FriendMenu", "Friend Menu"))

    def set_friend_requests(self, requests):
        self.FM_FriendRequestList.clear()
        image_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'images', 'DefaultProfile.png')
        for username in requests:
            item = QListWidgetItem(self.FM_FriendRequestList)
            widget = FriendRequestItemWidget(username, image_path)
            item.setSizeHint(widget.sizeHint())
            self.FM_FriendRequestList.setItemWidget(item, widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    FriendMenu = QDialog()
    ui = Ui_FriendMenu()
    ui.setupUi(FriendMenu)
    ui.set_friend_requests(["User1", "User2", "User3"])  # Example data
    FriendMenu.show()
    sys.exit(app.exec_())