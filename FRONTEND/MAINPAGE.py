# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\chris\OneDrive\Desktop\For Python Code\penpal\MAINPAGE.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'FRONTEND')))
from HomePage import Ui_Homepage
from AccountSettings import Ui_AccountSettings

# Get the absolute path of the current directory (LogInPage.py)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Build the general path to the resources/images folder
images_folder = os.path.join(current_directory, '..', 'resources', 'images')
Forget_Pass_assets_folder = os.path.join(current_directory, '..', 'resources', 'images', 'Forget_Pass_assets')


class Ui_Main_Page(object):
    def setupUi(self, Main_Page):
        Main_Page.setObjectName("Main_Page")
        Main_Page.setFixedSize(1440, 850)
        Main_Page.setMinimumSize(QtCore.QSize(0, 20))
        Main_Page.setMaximumSize(QtCore.QSize(16777193, 16777215))
        Main_Page.setSizeIncrement(QtCore.QSize(0, 24))
        self.LI_Header = QtWidgets.QFrame(Main_Page)
        self.LI_Header.setGeometry(QtCore.QRect(0, 0, 1440, 105))
        self.LI_Header.setStyleSheet("background: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, y1:0, x2:1, y2:0, \n"
"    stop:0 #EDC27E, \n"
"    stop:0.526 #EDC27E, \n"
"    stop:1 #DC586D\n"
");\n"
"\n"
"")
        self.LI_Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LI_Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LI_Header.setObjectName("LI_Header")
        self.MP_UpIcon = QtWidgets.QLabel(self.LI_Header)
        self.MP_UpIcon.setGeometry(QtCore.QRect(-50, -10, 182, 121))
        self.MP_UpIcon.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.MP_UpIcon.setSizeIncrement(QtCore.QSize(4, 0))
        self.MP_UpIcon.setStyleSheet("Background: transparent;")
        self.MP_UpIcon.setText("")
        self.MP_UpIcon.setPixmap(QtGui.QPixmap(os.path.join(Forget_Pass_assets_folder, 'GPfp.png')))
        self.MP_UpIcon.setScaledContents(True)
        self.MP_UpIcon.setObjectName("MP_UpIcon")
        self.MP_UPusername = QtWidgets.QLabel(self.LI_Header)
        self.MP_UPusername.setGeometry(QtCore.QRect(90, 20, 410, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.MP_UPusername.sizePolicy().hasHeightForWidth())
        self.MP_UPusername.setSizePolicy(sizePolicy)
        self.MP_UPusername.setMinimumSize(QtCore.QSize(488, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(26)
        font.setBold(False)
        self.MP_UPusername.setFont(font)
        self.MP_UPusername.setStyleSheet("background: transparent; /* Ensures no background color */\n"
"color: rgb(255, 255, 255); /* White text */\n"
"text-shadow: 2px 2px 5px #821B1A; /* Dark red shadow *")
        self.MP_UPusername.setObjectName("MP_UPusername")
        self.MP_ProfilePB = QtWidgets.QPushButton(self.LI_Header)
        self.MP_ProfilePB.setGeometry(QtCore.QRect(815, 30, 200, 45))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.MP_ProfilePB.setFont(font)
        self.MP_ProfilePB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MP_ProfilePB.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 700 14pt \"Times New Roman\";\n"
"border-color: rgb(229, 141, 118);\n"
"border: 3px solid #FFFFFF;\n"
"border-radius: 20px;\n"
"background: transparent;\n"
"")
        self.MP_ProfilePB.setObjectName("MP_ProfilePB")
        self.MP_MenuPB = QtWidgets.QPushButton(self.LI_Header)
        self.MP_MenuPB.setGeometry(QtCore.QRect(1020, 30, 200, 45))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.MP_MenuPB.setFont(font)
        self.MP_MenuPB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MP_MenuPB.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 700 14pt \"Times New Roman\";\n"
"border-color: rgb(229, 141, 118);\n"
"border: 3px solid #FFFFFF;\n"
"border-radius: 20px;\n"
"background: transparent;\n"
"")
        self.MP_MenuPB.setObjectName("MP_MenuPB")
        self.MP_LogoutPB = QtWidgets.QPushButton(self.LI_Header)
        self.MP_LogoutPB.setGeometry(QtCore.QRect(1225, 30, 200, 45))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.MP_LogoutPB.setFont(font)
        self.MP_LogoutPB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MP_LogoutPB.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 700 14pt \"Times New Roman\";\n"
"border-color: rgb(229, 141, 118);\n"
"border: 3px solid #FFFFFF;\n"
"border-radius: 20px;\n"
"background: transparent;\n"
"")
        self.MP_LogoutPB.setObjectName("MP_LogoutPB")
        self.MP_Shape3 = QtWidgets.QFrame(Main_Page)
        self.MP_Shape3.setGeometry(QtCore.QRect(830, 630, 179, 436))
        self.MP_Shape3.setStyleSheet("background-color: rgb(255, 240, 216);\n"
"border-radius: 5px;\n"
"border: 3px solid #BE7928;")
        self.MP_Shape3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MP_Shape3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MP_Shape3.setObjectName("MP_Shape3")
        self.MP_Shape2 = QtWidgets.QFrame(Main_Page)
        self.MP_Shape2.setGeometry(QtCore.QRect(720, 590, 254, 518))
        self.MP_Shape2.setStyleSheet("background-color: rgb(255, 240, 216);\n"
"border-radius: 5px;\n"
"border: 3px solid #BE7928;")
        self.MP_Shape2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MP_Shape2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MP_Shape2.setObjectName("MP_Shape2")
        self.MP_Shape1 = QtWidgets.QFrame(Main_Page)
        self.MP_Shape1.setGeometry(QtCore.QRect(450, 510, 489, 699))
        self.MP_Shape1.setStyleSheet("background-color: rgb(255, 240, 216);\n"
"border-radius: 5px;\n"
"border: 3px solid #BE7928;")
        self.MP_Shape1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MP_Shape1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MP_Shape1.setObjectName("MP_Shape1")
        self.MP_Profile_Display = QtWidgets.QLabel(self.MP_Shape1)
        self.MP_Profile_Display.setGeometry(QtCore.QRect(160, 20, 171, 101))
        self.MP_Profile_Display.setStyleSheet("border: none;")
        self.MP_Profile_Display.setText("")
        self.MP_Profile_Display.setPixmap(QtGui.QPixmap(os.path.join(Forget_Pass_assets_folder, 'GPfp.png')))
        self.MP_Profile_Display.setScaledContents(True)
        self.MP_Profile_Display.setObjectName("MP_Profile_Display")
        self.MP_Username = QtWidgets.QLabel(self.MP_Shape1)
        self.MP_Username.setGeometry(QtCore.QRect(190, 110, 488, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.MP_Username.sizePolicy().hasHeightForWidth())
        self.MP_Username.setSizePolicy(sizePolicy)
        self.MP_Username.setMinimumSize(QtCore.QSize(488, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        self.MP_Username.setFont(font)
        self.MP_Username.setStyleSheet("font-size: 36px;\n"
"text-align: center;\n"
"background: transparent;\n"
"color: #BE7928;\n"
"text-align: left;\n"
"border: none;")
        self.MP_Username.setObjectName("MP_Username")
        self.MP_Age = QtWidgets.QLabel(self.MP_Shape1)
        self.MP_Age.setGeometry(QtCore.QRect(50, 180, 351, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MP_Age.sizePolicy().hasHeightForWidth())
        self.MP_Age.setSizePolicy(sizePolicy)
        self.MP_Age.setMinimumSize(QtCore.QSize(351, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.MP_Age.setFont(font)
        self.MP_Age.setStyleSheet("color: rgb(122, 12, 12);\n"
"border: none;\n"
"font: 700 16pt \"Rockwell\";\n"
"background: none;")
        self.MP_Age.setObjectName("MP_Age")
        self.MP_Gender = QtWidgets.QLabel(self.MP_Shape1)
        self.MP_Gender.setGeometry(QtCore.QRect(50, 240, 351, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MP_Gender.sizePolicy().hasHeightForWidth())
        self.MP_Gender.setSizePolicy(sizePolicy)
        self.MP_Gender.setMinimumSize(QtCore.QSize(351, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.MP_Gender.setFont(font)
        self.MP_Gender.setStyleSheet("color: rgb(122, 12, 12);\n"
"border: none;\n"
"font: 700 16pt \"Rockwell\";\n"
"background: none;\n"
"")
        self.MP_Gender.setObjectName("MP_Gender")
        self.MP_Location = QtWidgets.QLabel(self.MP_Shape1)
        self.MP_Location.setGeometry(QtCore.QRect(50, 300, 351, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MP_Location.sizePolicy().hasHeightForWidth())
        self.MP_Location.setSizePolicy(sizePolicy)
        self.MP_Location.setMinimumSize(QtCore.QSize(351, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.MP_Location.setFont(font)
        self.MP_Location.setStyleSheet("color: rgb(122, 12, 12);\n"
"border: none;\n"
"font: 700 16pt \"Rockwell\";\n"
"background: none;")
        self.MP_Location.setObjectName("MP_Location")
        self.MP_Preference = QtWidgets.QLabel(self.MP_Shape1)
        self.MP_Preference.setGeometry(QtCore.QRect(50, 360, 351, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MP_Preference.sizePolicy().hasHeightForWidth())
        self.MP_Preference.setSizePolicy(sizePolicy)
        self.MP_Preference.setMinimumSize(QtCore.QSize(351, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.MP_Preference.setFont(font)
        self.MP_Preference.setStyleSheet("color: rgb(122, 12, 12);\n"
"border: none;\n"
"font: 700 16pt \"Rockwell\";\n"
"background: none;\n"
"")
        self.MP_Preference.setObjectName("MP_Preference")
        self.MP_Preference1 = QtWidgets.QLabel(self.MP_Shape1)
        self.MP_Preference1.setGeometry(QtCore.QRect(15, 430, 351, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MP_Preference1.sizePolicy().hasHeightForWidth())
        self.MP_Preference1.setSizePolicy(sizePolicy)
        self.MP_Preference1.setMinimumSize(QtCore.QSize(351, 36))
        self.MP_Preference1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.MP_Preference1.setFont(font)
        self.MP_Preference1.setStyleSheet("color: rgb(122, 12, 12);\n"
"border: none;\n"
"font: 700 16pt \"Rockwell\";\n"
"background: none;\n"
"")
        self.MP_Preference1.setObjectName("MP_Preference1")
        self.MP_Preference2 = QtWidgets.QLabel(self.MP_Shape1)
        self.MP_Preference2.setGeometry(QtCore.QRect(180, 430, 351, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MP_Preference2.sizePolicy().hasHeightForWidth())
        self.MP_Preference2.setSizePolicy(sizePolicy)
        self.MP_Preference2.setMinimumSize(QtCore.QSize(351, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.MP_Preference2.setFont(font)
        self.MP_Preference2.setStyleSheet("color: rgb(122, 12, 12);\n"
"border: none;\n"
"font: 700 16pt \"Rockwell\";\n"
"background: none;\n"
"")
        self.MP_Preference2.setObjectName("MP_Preference2")
        self.MP_Preference3 = QtWidgets.QLabel(self.MP_Shape1)
        self.MP_Preference3.setGeometry(QtCore.QRect(346, 430, 351, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MP_Preference3.sizePolicy().hasHeightForWidth())
        self.MP_Preference3.setSizePolicy(sizePolicy)
        self.MP_Preference3.setMinimumSize(QtCore.QSize(351, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.MP_Preference3.setFont(font)
        self.MP_Preference3.setStyleSheet("color: rgb(122, 12, 12);\n"
"border: none;\n"
"font: 700 16pt \"Rockwell\";\n"
"background: none;\n"
"")
        self.MP_Preference3.setObjectName("MP_Preference3")
        self.MP_Preference4 = QtWidgets.QLabel(self.MP_Shape1)
        self.MP_Preference4.setGeometry(QtCore.QRect(110, 500, 351, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MP_Preference4.sizePolicy().hasHeightForWidth())
        self.MP_Preference4.setSizePolicy(sizePolicy)
        self.MP_Preference4.setMinimumSize(QtCore.QSize(351, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.MP_Preference4.setFont(font)
        self.MP_Preference4.setStyleSheet("color: rgb(122, 12, 12);\n"
"border: none;\n"
"font: 700 16pt \"Rockwell\";\n"
"background: none;\n"
"")
        self.MP_Preference4.setObjectName("MP_Preference4")
        self.MP_Preference5 = QtWidgets.QLabel(self.MP_Shape1)
        self.MP_Preference5.setGeometry(QtCore.QRect(260, 500, 351, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MP_Preference5.sizePolicy().hasHeightForWidth())
        self.MP_Preference5.setSizePolicy(sizePolicy)
        self.MP_Preference5.setMinimumSize(QtCore.QSize(351, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.MP_Preference5.setFont(font)
        self.MP_Preference5.setStyleSheet("color: rgb(122, 12, 12);\n"
"border: none;\n"
"font: 700 16pt \"Rockwell\";\n"
"background: none;\n"
"")
        self.MP_Preference5.setObjectName("MP_Preference5")
        self.MP_DescriptionText = QtWidgets.QLabel(Main_Page)
        self.MP_DescriptionText.setGeometry(QtCore.QRect(190, 340, 1011, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MP_DescriptionText.sizePolicy().hasHeightForWidth())
        self.MP_DescriptionText.setSizePolicy(sizePolicy)
        self.MP_DescriptionText.setMinimumSize(QtCore.QSize(351, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        self.MP_DescriptionText.setFont(font)
        self.MP_DescriptionText.setStyleSheet("color: rgb(190, 121, 40); font-size: 36px;\n"
"background: transparent;\n"
"\n"
"")
        self.MP_DescriptionText.setObjectName("MP_DescriptionText")
        self.MP_Welcome = QtWidgets.QLabel(Main_Page)
        self.MP_Welcome.setGeometry(QtCore.QRect(330, 170, 381, 211))
        self.MP_Welcome.setStyleSheet("background: transparent;")
        self.MP_Welcome.setText("")
        self.MP_Welcome.setPixmap(QtGui.QPixmap(os.path.join(Forget_Pass_assets_folder, 'FPWEL.png')))
        self.MP_Welcome.setScaledContents(True)
        self.MP_Welcome.setObjectName("MP_Welcome")
        self.MP_TO_PENPAL = QtWidgets.QLabel(Main_Page)
        self.MP_TO_PENPAL.setGeometry(QtCore.QRect(630, 173, 381, 211))
        self.MP_TO_PENPAL.setStyleSheet("background: transparent;")
        self.MP_TO_PENPAL.setText("")
        self.MP_TO_PENPAL.setPixmap(QtGui.QPixmap(os.path.join(Forget_Pass_assets_folder, 'FPWEL (2).png')))
        self.MP_TO_PENPAL.setScaledContents(True)
        self.MP_TO_PENPAL.setWordWrap(False)
        self.MP_TO_PENPAL.setObjectName("MP_TO_PENPAL")
        self.MP_GroupImage = QtWidgets.QLabel(Main_Page)
        self.MP_GroupImage.setGeometry(QtCore.QRect(0, 420, 1545, 892))
        self.MP_GroupImage.setText("")
        self.MP_GroupImage.setPixmap(QtGui.QPixmap(os.path.join(Forget_Pass_assets_folder, 'FPgroup.png')))
        self.MP_GroupImage.setScaledContents(True)
        self.MP_GroupImage.setObjectName("MP_GroupImage")
        self.MP_GroupImage.raise_()
        self.LI_Header.raise_()
        self.MP_Shape3.raise_()
        self.MP_Shape2.raise_()
        self.MP_Shape1.raise_()
        self.MP_DescriptionText.raise_()
        self.MP_Welcome.raise_()
        self.MP_TO_PENPAL.raise_()

        self.retranslateUi(Main_Page)
        QtCore.QMetaObject.connectSlotsByName(Main_Page)

    def retranslateUi(self, Main_Page):
        _translate = QtCore.QCoreApplication.translate
        Main_Page.setWindowTitle(_translate("Main_Page", "Dialog"))
        self.MP_UPusername.setText(_translate("Main_Page", "USERNAME"))
        self.MP_ProfilePB.setText(_translate("Main_Page", "PROFILE"))
        self.MP_MenuPB.setText(_translate("Main_Page", "MENU"))
        self.MP_LogoutPB.setText(_translate("Main_Page", "LOG OUT"))
        self.MP_Username.setText(_translate("Main_Page", "Username"))
        self.MP_Age.setText(_translate("Main_Page", "Age:"))
        self.MP_Gender.setText(_translate("Main_Page", "Gender:"))
        self.MP_Location.setText(_translate("Main_Page", "Location:"))
        self.MP_Preference.setText(_translate("Main_Page", "Preferences:"))
        self.MP_Preference1.setText(_translate("Main_Page", "Pref.1"))
        self.MP_Preference2.setText(_translate("Main_Page", "Pref.2"))
        self.MP_Preference3.setText(_translate("Main_Page", "Pref.3"))
        self.MP_Preference4.setText(_translate("Main_Page", "Pref.4"))
        self.MP_Preference5.setText(_translate("Main_Page", "Pref.5"))
        self.MP_DescriptionText.setText(_translate("Main_Page", "<html><head/><body><p align=\"center\">EXPLORE AND CONNECT WITH PEOPLE WHO SHARE YOUR INTERESTS. SWIPE RIGHT </p><p align=\"center\">TO CONNECT, LEFT TO PASS. HAPPY CONNECTING WITH LIKE-MINDED INDIVIDUALS!</p></body></html>"))
      

#USERNAME DISPLAY
        self.username = "Default Username"  # Set a default username
        self.display_username()

    def set_user_info(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.display_username()
    
    def display_username(self):
        username = self.get_username_from_server()
        self.MP_UPusername.setText(username)
       

    def get_username_from_server(self):
        try:
            response = requests.get("http://localhost:5000/get_username", params={"username": self.username})
            if response.status_code == 200:
                return self.username
            else:
                return self.username
        except requests.RequestException as e:
            print(f"Error fetching username: {e}")
            return "Unknown User"


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_Page = QtWidgets.QDialog()
    ui = Ui_Main_Page()
    ui.setupUi(Main_Page)
    Main_Page.show()
    sys.exit(app.exec_())
