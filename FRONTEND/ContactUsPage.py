# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\chris\OneDrive\Desktop\For Python Code\penpal\ContactUsPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

# Get the absolute path of the current directory (LogInPage.py)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Build the general path to the resources/images folder
images_folder = os.path.join(current_directory, '..', 'resources', 'images')
CU_assets_folder = os.path.join(current_directory, '..', 'resources', 'images', 'CU_assets')


class Ui_ContactUs(object):
    def setupUi(self, ContactUs):
        ContactUs.setObjectName("ContactUs")
        ContactUs.setFixedSize(1440, 850)
        ContactUs.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CUHeader = QtWidgets.QFrame(ContactUs)
        self.CUHeader.setGeometry(QtCore.QRect(0, 0, 1440, 105))
        self.CUHeader.setStyleSheet("background: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, y1:0, x2:1, y2:0, \n"
"    stop:0 #EDC27E, \n"
"    stop:0.526 #EDC27E, \n"
"    stop:1 #DC586D\n"
");\n"
"\n"
"")
        self.CUHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CUHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CUHeader.setObjectName("CUHeader")
        self.HeaderIcon = QtWidgets.QLabel(self.CUHeader)
        self.HeaderIcon.setGeometry(QtCore.QRect(-70, -20, 274, 146))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(28)
        self.HeaderIcon.setFont(font)
        self.HeaderIcon.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;")
        self.HeaderIcon.setText("")
        self.HeaderIcon.setPixmap(QtGui.QPixmap(os.path.join(images_folder , "HeaderIcon.png")))
        self.HeaderIcon.setScaledContents(True)
        self.HeaderIcon.setObjectName("HeaderIcon")
        self.CUimage1 = QtWidgets.QLabel(ContactUs)
        self.CUimage1.setGeometry(QtCore.QRect(-10, 100, 1451, 981))
        self.CUimage1.setText("")
        self.CUimage1.setPixmap(QtGui.QPixmap(os.path.join(CU_assets_folder , "CUimage1.png")))
        self.CUimage1.setScaledContents(True)
        self.CUimage1.setObjectName("CUimage1")
        self.HPlshadow1 = QtWidgets.QLabel(ContactUs)
        self.HPlshadow1.setGeometry(QtCore.QRect(130, 270, 1451, 981))
        self.HPlshadow1.setStyleSheet("background: transparent;")
        self.HPlshadow1.setText("")
        self.HPlshadow1.setPixmap(QtGui.QPixmap(os.path.join(CU_assets_folder , "HP1shadow1.png")))
        self.HPlshadow1.setScaledContents(True)
        self.HPlshadow1.setObjectName("HPlshadow1")
        self.CU = QtWidgets.QLabel(ContactUs)
        self.CU.setGeometry(QtCore.QRect(340, -130, 1451, 681))
        self.CU.setStyleSheet("background: transparent;")
        self.CU.setText("")
        self.CU.setPixmap(QtGui.QPixmap(os.path.join(CU_assets_folder , "CU.png")))
        self.CU.setScaledContents(True)
        self.CU.setObjectName("CU")
        self.CUtxt = QtWidgets.QLabel(ContactUs)
        self.CUtxt.setGeometry(QtCore.QRect(420, 190, 971, 431))
        self.CUtxt.setStyleSheet("background: transparent;")
        self.CUtxt.setText("")
        self.CUtxt.setPixmap(QtGui.QPixmap(os.path.join(CU_assets_folder , "CUtext.png")))
        self.CUtxt.setScaledContents(True)
        self.CUtxt.setObjectName("CUtxt")
        self.CUicon1 = QtWidgets.QLabel(ContactUs)
        self.CUicon1.setGeometry(QtCore.QRect(450, 750, 221, 121))
        self.CUicon1.setStyleSheet("background: transparent;")
        self.CUicon1.setText("")
        self.CUicon1.setPixmap(QtGui.QPixmap(os.path.join(CU_assets_folder , "CUicon1.png")))
        self.CUicon1.setScaledContents(True)
        self.CUicon1.setObjectName("CUicon1")
        self.CUicon2 = QtWidgets.QLabel(ContactUs)
        self.CUicon2.setGeometry(QtCore.QRect(710, 750, 191, 121))
        self.CUicon2.setStyleSheet("background: transparent;")
        self.CUicon2.setText("")
        self.CUicon2.setPixmap(QtGui.QPixmap(os.path.join(CU_assets_folder , "CUicon2.png")))
        self.CUicon2.setScaledContents(True)
        self.CUicon2.setObjectName("CUicon2")
        self.CUicon3 = QtWidgets.QLabel(ContactUs)
        self.CUicon3.setGeometry(QtCore.QRect(1010, 720, 291, 171))
        self.CUicon3.setStyleSheet("background: transparent;")
        self.CUicon3.setText("")
        self.CUicon3.setPixmap(QtGui.QPixmap(os.path.join(CU_assets_folder , "CUicon3.png")))
        self.CUicon3.setScaledContents(True)
        self.CUicon3.setObjectName("CUicon3")
        self.CUicon4 = QtWidgets.QLabel(ContactUs)
        self.CUicon4.setGeometry(QtCore.QRect(540, 920, 221, 131))
        self.CUicon4.setStyleSheet("background: transparent;")
        self.CUicon4.setText("")
        self.CUicon4.setPixmap(QtGui.QPixmap(os.path.join(CU_assets_folder , "CUicon4.png")))
        self.CUicon4.setScaledContents(True)
        self.CUicon4.setObjectName("CUicon4")
        self.CUicon5 = QtWidgets.QLabel(ContactUs)
        self.CUicon5.setGeometry(QtCore.QRect(860, 920, 251, 151))
        self.CUicon5.setStyleSheet("background: transparent;")
        self.CUicon5.setText("")
        self.CUicon5.setPixmap(QtGui.QPixmap(os.path.join(CU_assets_folder , "CUicon5.png")))
        self.CUicon5.setScaledContents(True)
        self.CUicon5.setObjectName("CUicon5")
        self.CUtext5 = QtWidgets.QLabel(ContactUs)
        self.CUtext5.setGeometry(QtCore.QRect(1060, 980, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        self.CUtext5.setFont(font)
        self.CUtext5.setStyleSheet("background: transparent;\n"
"font-size: 40px;\n"
"Color: #7A0C0C;")
        self.CUtext5.setObjectName("CUtext5")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(ContactUs)
        self.commandLinkButton.setGeometry(QtCore.QRect(560, 820, 181, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setStyleSheet("background: transparent;\n"
"font-size: 30px;\n"
"Color: #7A0C0C;")
        icon = QtGui.QIcon.fromTheme("dot")
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(ContactUs)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(860, 810, 222, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setStyleSheet("background: transparent;\n"
"font-size: 30px;\n"
"Color: #7A0C0C;")
        icon = QtGui.QIcon.fromTheme("dot")
        self.commandLinkButton_2.setIcon(icon)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(ContactUs)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(1210, 810, 111, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.commandLinkButton_3.setFont(font)
        self.commandLinkButton_3.setStyleSheet("background: transparent;\n"
"font-size: 30px;\n"
"Color: #7A0C0C;")
        icon = QtGui.QIcon.fromTheme("dot")
        self.commandLinkButton_3.setIcon(icon)
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(ContactUs)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(700, 980, 222, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.commandLinkButton_4.setFont(font)
        self.commandLinkButton_4.setStyleSheet("background: transparent;\n"
"font-size: 30px;\n"
"Color: #7A0C0C;")
        icon = QtGui.QIcon.fromTheme("dot")
        self.commandLinkButton_4.setIcon(icon)
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")

        # Create the BACK button
        self.CUbackButton = QtWidgets.QPushButton("BACK", ContactUs)
        self.CUbackButton.setGeometry(QtCore.QRect(1252, 35, 150, 45))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.CUbackButton.setFont(font)
        self.CUbackButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CUbackButton.setStyleSheet("""
            font:30px;
            color: #FFFFFF;
            border: 2px solid #FFFFFF;
            background: transparent;
            border-radius: 5px;
        """)
        self.CUbackButton.setObjectName("Back")
        # Add hover effect to change background color
        self.CUbackButton.setStyleSheet("""
            QPushButton {
                font:30px;
                color: #FFFFFF;
                border: 2px solid #FFFFFF;
                background: transparent;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FFFFFF;
                color: #000000;
            }
        """)
        

        self.retranslateUi(ContactUs)
        QtCore.QMetaObject.connectSlotsByName(ContactUs)


    def retranslateUi(self, ContactUs):
        _translate = QtCore.QCoreApplication.translate
        ContactUs.setWindowTitle(_translate("ContactUs", "ContactUs"))
        self.CUtext5.setText(_translate("ContactUs", "09*********"))
        self.commandLinkButton.setText(_translate("ContactUs", "FACEBOOK"))
        self.commandLinkButton_2.setText(_translate("ContactUs", "INSTAGRAM"))
        self.commandLinkButton_3.setText(_translate("ContactUs", "EMAIL"))
        self.commandLinkButton_4.setText(_translate("ContactUs", "TELEGRAM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ContactUs = QtWidgets.QDialog()
    ui = Ui_ContactUs()
    ui.setupUi(ContactUs)
    ContactUs.show()
    sys.exit(app.exec_())
