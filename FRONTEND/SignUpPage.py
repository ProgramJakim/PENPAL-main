# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PENPAL\SignUpPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QLabel
import os, requests
import re
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'FRONTEND')))
from InterestPage import Ui_Interest
from TermsAndCondition import Ui_TermsAndCondition
# Get the absolute path of the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Build the general path to the resources/images folder
images_folder = os.path.join(current_directory, '..', 'resources', 'images')
Sign_Up_assets_folder = os.path.join(current_directory, '..', 'resources', 'images', 'Sign_Up_assets')

class Ui_SignUp(object):
    def setupUi(self, SignUp, username="", password="", age="", gender="", location="", social_media_link="", gmail=""):
        SignUp.setObjectName("SignUp")
        SignUp.resize(1440, 850)
        SignUp.setStyleSheet("background-color: rgb(255, 249, 240);")

#Header
        self.SU_Header = QtWidgets.QFrame(SignUp)
        self.SU_Header.setGeometry(QtCore.QRect(0, 0, 1440, 105))
        self.SU_Header.setStyleSheet("background: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, y1:0, x2:1, y2:0, \n"
"    stop:0 #EDC27E, \n"
"    stop:0.526 #EDC27E, \n"
"    stop:1 #DC586D\n"
");\n"
"\n"
"")
        self.SU_Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SU_Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SU_Header.setObjectName("SU_Header")
        
#Header Icon
        self.SU_HeaderIcon = QtWidgets.QLabel(self.SU_Header)
        self.SU_HeaderIcon.setGeometry(QtCore.QRect(-60, -20, 274, 146))
        self.SU_HeaderIcon.setStyleSheet("background: transparent;\n"
"")
        self.SU_HeaderIcon.setText("")
        self.SU_HeaderIcon.setPixmap(QtGui.QPixmap(os.path.join(images_folder , "HeaderIcon.png")))
        self.SU_HeaderIcon.setScaledContents(True)
        self.SU_HeaderIcon.setObjectName("SU_HeaderIcon")
        
#Main Panerl
        self.SU_MainPanel = QtWidgets.QFrame(SignUp)
        self.SU_MainPanel.setGeometry(QtCore.QRect(182, 120, 1080, 700))
        self.SU_MainPanel.setStyleSheet("background-color: rgb(255, 240, 216);")
        self.SU_MainPanel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SU_MainPanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SU_MainPanel.setObjectName("SU_MainPanel")
        
#Side Panel
        self.SU_SidePanel = QtWidgets.QFrame(self.SU_MainPanel)
        self.SU_SidePanel.setGeometry(QtCore.QRect(0, 0, 421, 700))
        self.SU_SidePanel.setStyleSheet("background-color: rgb(255, 214, 182);")
        self.SU_SidePanel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SU_SidePanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SU_SidePanel.setObjectName("SU_SidePanel")

#Side Panel Background Image
        self.SU_SidePanelBg = QtWidgets.QLabel(self.SU_SidePanel)
        self.SU_SidePanelBg.setGeometry(QtCore.QRect(-170, 0, 931, 650))
        self.SU_SidePanelBg.setText("")
        self.SU_SidePanelBg.setPixmap(QtGui.QPixmap(os.path.join( Sign_Up_assets_folder , "SU_SidePanel.png")))
        self.SU_SidePanelBg.setScaledContents(True)
        self.SU_SidePanelBg.setObjectName("SU_SidePanelBg")
        
#Welcome Back Image
        self.SU_WelcomeBackLBL = QtWidgets.QLabel(self.SU_SidePanel)
        self.SU_WelcomeBackLBL.setGeometry(QtCore.QRect(-160, 50, 741, 461))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(28)
        self.SU_WelcomeBackLBL.setFont(font)
        self.SU_WelcomeBackLBL.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;")
        self.SU_WelcomeBackLBL.setText("")
        self.SU_WelcomeBackLBL.setPixmap(QtGui.QPixmap(os.path.join(Sign_Up_assets_folder , "SU_LogInStatement.png")))
        self.SU_WelcomeBackLBL.setScaledContents(True)
        self.SU_WelcomeBackLBL.setObjectName("SU_WelcomeBackLBL")
        
#Log In Push Button
        self.SU_LogInPB = QtWidgets.QPushButton(self.SU_SidePanel)
        self.SU_LogInPB.setGeometry(QtCore.QRect(150, 370, 119, 36))
        self.SU_LogInPB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SU_LogInPB.setStyleSheet("border-color: rgb(122, 12, 12);\n"
"color: rgb(122, 12, 12);\n"
"border: 3px solid #550808;\n"
"background-color: rgb(229, 141, 118);\n"
"border-radius: 10px;\n"
"text-decoration: underline;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.5);\n"
"text-color: #E58D76;\n"
"\n"
"")
        self.SU_LogInPB.setObjectName("SU_LogInPB")
        
#Icon Image
        self.SU_Icon = QtWidgets.QLabel(self.SU_SidePanel)
        self.SU_Icon.setGeometry(QtCore.QRect(200, -10, 274, 146))
        self.SU_Icon.setStyleSheet("background: transparent;\n"
"")
        self.SU_Icon.setText("")
        self.SU_Icon.setPixmap(QtGui.QPixmap(os.path.join(images_folder , "Icon.png")))
        self.SU_Icon.setScaledContents(True)
        self.SU_Icon.setObjectName("SU_Icon")
        
#Username Label
        self.SU_UsernameLBL = QtWidgets.QLabel(self.SU_MainPanel)
        self.SU_UsernameLBL.setGeometry(QtCore.QRect(490, 90, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SU_UsernameLBL.setFont(font)
        self.SU_UsernameLBL.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;")
        self.SU_UsernameLBL.setObjectName("SU_UsernameLBL")
        
#Password Label
        self.SU_PasswordLBL = QtWidgets.QLabel(self.SU_MainPanel)
        self.SU_PasswordLBL.setGeometry(QtCore.QRect(490, 160, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SU_PasswordLBL.setFont(font)
        self.SU_PasswordLBL.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;")
        self.SU_PasswordLBL.setObjectName("SU_PasswordLBL")
        
#Username Line Edit (Text Box)
        self.SU_UsernameLE = QtWidgets.QLineEdit(self.SU_MainPanel)
        self.SU_UsernameLE.setGeometry(QtCore.QRect(550, 120, 421, 31))
        self.SU_UsernameLE.setStyleSheet("border-color: rgb(229, 141, 118);\n"
"border: 3px solid #E58D76;\n"
"border-radius: 5px;\n"
"background: transparent;")
        self.SU_UsernameLE.setObjectName("SU_UsernameLE")
        
#Password Line Edit (Text Box)
        self.SU_PasswordLE = QtWidgets.QLineEdit(self.SU_MainPanel)
        self.SU_PasswordLE.setGeometry(QtCore.QRect(550, 190, 421, 31))
        self.SU_PasswordLE.setStyleSheet("border-color: rgb(229, 141, 118);\n"
"border: 3px solid #E58D76;\n"
"border-radius: 5px;\n"
"background: transparent;")
        self.SU_PasswordLE.setObjectName("SU_PasswordLE")

#Sign Up Push Button
        self.SU_SignUpPB= QtWidgets.QPushButton(self.SU_MainPanel)
        self.SU_SignUpPB.setGeometry(QtCore.QRect(700, 595, 119, 36))
        self.SU_SignUpPB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SU_SignUpPB.setStyleSheet("border-color: rgb(229, 141, 118);\n"
"border: 3px solid #E58D76;\n"
"border-radius: 10px;\n"
"text-decoration: none;"
"text-color: #E58D76;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.5);\n"
"background: transparent;\n"
"")
        self.SU_SignUpPB.setObjectName("SU_SignUpPB")



#Interest Button
        self.SU_InterestPB = QtWidgets.QPushButton(self.SU_MainPanel)
        self.SU_InterestPB.setGeometry(QtCore.QRect(550, 550, 119, 36))
        self.SU_InterestPB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SU_InterestPB.setStyleSheet("border-color: rgb(229, 141, 118);\n"
"border: 3px solid #E58D76;\n"
"border-radius: 10px;\n"
"text-decoration: none;"
"text-color: #E58D76;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.5);\n"
"background: transparent;\n"
"")
        self.SU_InterestPB.setObjectName("SU_InterestPB")

# Date of Birth Label
        self.SU_DOBLBL = QtWidgets.QLabel(self.SU_MainPanel)
        self.SU_DOBLBL.setGeometry(QtCore.QRect(490, 240, 500, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SU_DOBLBL.setFont(font)
        self.SU_DOBLBL.setStyleSheet("color: rgb(98, 65, 66);\nbackground: transparent;")
        self.SU_DOBLBL.setObjectName("SU_DOBLBL")
        self.SU_DOBLBL.setText("Date of Birth:")

# Date of Birth Input
        self.SU_DOB = QtWidgets.QDateEdit(self.SU_MainPanel)
        self.SU_DOB.setGeometry(QtCore.QRect(550, 280, 141, 31))
        self.SU_DOB.setCalendarPopup(True)
        self.SU_DOB.setStyleSheet("border-color: rgb(229, 141, 118);\nborder: 3px solid #E58D76;\nborder-radius: 5px;\nbackground: transparent;")
        self.SU_DOB.setObjectName("SU_DOB")

# Customize the calendar popup
        calendar = self.SU_DOB.calendarWidget()
        calendar.setStyleSheet("""
        QWidget {
                background-color: white;
                color: black;
        }
        QAbstractItemView {
                selection-background-color: rgb(229, 141, 118);
                selection-color: white;
        }
        QToolButton {
                background-color: rgb(229, 141, 118);
                color: white;
        }
        QToolButton::hover {
                background-color: rgb(255, 187, 173);
        }
        QToolButton::pressed {
                background-color: rgb(255, 187, 173);
        }
        QMenu {
                background-color: white;
                color: black;
        }
        QMenu::item::selected {
                background-color: rgb(229, 141, 118);
                color: white;
        }
        """)
        
#Gender Check Box
        self.SU_GenderCB = QtWidgets.QComboBox(self.SU_MainPanel)
        self.SU_GenderCB.setGeometry(QtCore.QRect(830, 280, 141, 31))
        self.SU_GenderCB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SU_GenderCB.setStyleSheet("border-color: rgb(229, 141, 118);\n"
"background-color: rgba(229, 141, 118, 0.5);\n"
"border: 3px solid #E58D76;\n"
"border-radius: 5px;\n"
"")
        self.SU_GenderCB.setObjectName("SU_GenderCB")
        self.SU_GenderCB.addItem("")
        self.SU_GenderCB.addItem("")
        self.SU_GenderCB.addItem("")
        
#Gender Label
        self.SU_GenderLBL = QtWidgets.QLabel(self.SU_MainPanel)
        self.SU_GenderLBL.setGeometry(QtCore.QRect(720, 240, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SU_GenderLBL.setFont(font)
        self.SU_GenderLBL.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;")
        self.SU_GenderLBL.setObjectName("SU_GenderLBL")
        
#Location Label
        self.SU_LocationLBL_ = QtWidgets.QLabel(self.SU_MainPanel)
        self.SU_LocationLBL_.setGeometry(QtCore.QRect(490, 325, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SU_LocationLBL_.setFont(font)
        self.SU_LocationLBL_.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;")
        self.SU_LocationLBL_.setObjectName("SU_LocationLBL_")
        
#Location Line Edit (Text Box)
        self.SU_LocationLE = QtWidgets.QLineEdit(self.SU_MainPanel)
        self.SU_LocationLE.setGeometry(QtCore.QRect(550, 355, 421, 31))
        self.SU_LocationLE.setStyleSheet("border-color: rgb(229, 141, 118);\n"
"border: 3px solid #E58D76;\n"
"border-radius: 5px;\n"
"background: transparent;")
        self.SU_LocationLE.setObjectName("SU_LocationLE")
        
#Social Link Label
        self.SU_SocialLinkLBL = QtWidgets.QLabel(self.SU_MainPanel)
        self.SU_SocialLinkLBL.setGeometry(QtCore.QRect(490, 465, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SU_SocialLinkLBL.setFont(font)
        self.SU_SocialLinkLBL.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;")
        self.SU_SocialLinkLBL.setObjectName("SU_SocialLinkLBL")
        
#Social Link Line Edit (Text Box)
        self.SU_SocialLinkLE = QtWidgets.QLineEdit(self.SU_MainPanel)
        self.SU_SocialLinkLE.setGeometry(QtCore.QRect(550, 495, 421, 31))
        self.SU_SocialLinkLE.setStyleSheet("border-color: rgb(229, 141, 118);\n"
"border: 3px solid #E58D76;\n"
"border-radius: 5px;\n"
"background: transparent;")
        self.SU_SocialLinkLE.setObjectName("SU_SocialLinkLE")
        
#Terms and Privacy Check Box
        self.SU_TermsandPrivacyChB = QtWidgets.QCheckBox(self.SU_MainPanel)
        self.SU_TermsandPrivacyChB.setGeometry(QtCore.QRect(680, 555, 291, 20))
        self.SU_TermsandPrivacyChB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SU_TermsandPrivacyChB.setStyleSheet("background: transparent;    \n"
"")
        self.SU_TermsandPrivacyChB.setObjectName("SU_TermsandPrivacyChB")
        
#Shadow Image
        self.SU_Shadow = QtWidgets.QLabel(self.SU_MainPanel)
        self.SU_Shadow.setGeometry(QtCore.QRect(40, 0, 851, 700))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(16)
        self.SU_Shadow.setFont(font)
        self.SU_Shadow.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;")
        self.SU_Shadow.setText("")
        self.SU_Shadow.setPixmap(QtGui.QPixmap(os.path.join(Sign_Up_assets_folder , "SU_Shadow.png")))
        self.SU_Shadow.setScaledContents(True)
        self.SU_Shadow.setObjectName("SU_Shadow")
        
#Create An Account Label
        self.SU_CreateanAccount = QtWidgets.QLabel(self.SU_MainPanel)
        self.SU_CreateanAccount.setGeometry(QtCore.QRect(540, 20, 451, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.SU_CreateanAccount.setFont(font)
        self.SU_CreateanAccount.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;")
        self.SU_CreateanAccount.setObjectName("SU_CreateanAccount")
        
#Email Label
        self.SU_EmailLBL = QtWidgets.QLabel(self.SU_MainPanel)
        self.SU_EmailLBL.setGeometry(QtCore.QRect(490, 395, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SU_EmailLBL.setFont(font)
        self.SU_EmailLBL.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;")
        self.SU_EmailLBL.setObjectName("SU_EmailLBL")
        
#Email Line Edit (Text Edit )
        self.SU_EmailLE = QtWidgets.QLineEdit(self.SU_MainPanel)
        self.SU_EmailLE.setGeometry(QtCore.QRect(550, 425, 421, 31))
        self.SU_EmailLE.setStyleSheet("border-color: rgb(229, 141, 118);\n"
"border: 3px solid #E58D76;\n"
"border-radius: 5px;\n"
"background: transparent;")
        
        
        self.SU_EmailLE.setObjectName("SU_EmailLE")
        self.SU_Shadow.raise_()
        self.SU_SidePanel.raise_()
        self.SU_UsernameLBL.raise_()
        self.SU_PasswordLBL.raise_()
        self.SU_UsernameLE.raise_()
        self.SU_PasswordLE.raise_()
        self.SU_SignUpPB.raise_()
        self.SU_InterestPB.raise_()
        self.SU_DOBLBL.raise_()
        self.SU_DOB.raise_()
        self.SU_GenderCB.raise_()
        self.SU_GenderLBL.raise_()
        self.SU_LocationLBL_.raise_()
        self.SU_LocationLE.raise_()
        self.SU_SocialLinkLBL.raise_()
        self.SU_SocialLinkLE.raise_()
        self.SU_TermsandPrivacyChB.raise_()
        self.SU_CreateanAccount.raise_()
        self.SU_EmailLBL.raise_()
        self.SU_EmailLE.raise_()

        # Pre-fill the form fields
        self.SU_UsernameLE.setText(username)
        self.SU_PasswordLE.setText(password)
        self.SU_GenderCB.setCurrentText(gender)
        self.SU_LocationLE.setText(location)
        self.SU_SocialLinkLE.setText(social_media_link)
        self.SU_EmailLE.setText(gmail)
        self.error_message_label = QLabel() 

        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)


    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "Dialog"))
        self.SU_LogInPB.setText(_translate("SignUp", "Log In"))
        self.SU_UsernameLBL.setText(_translate("SignUp", "Username:"))
        self.SU_PasswordLBL.setText(_translate("SignUp", "Password:"))
        self.SU_InterestPB.setText(_translate("SignUp", "Select Interests"))
        self.SU_SignUpPB.setText(_translate("SignUp", "Sign Up"))
        self.SU_GenderCB.setItemText(0, _translate("SignUp", "Male"))
        self.SU_GenderCB.setItemText(1, _translate("SignUp", "Female"))
        self.SU_GenderCB.setItemText(2, _translate("SignUp", "Neutral"))
        self.SU_GenderLBL.setText(_translate("SignUp", "Gender:"))
        self.SU_LocationLBL_.setText(_translate("SignUp", "Location:"))
        self.SU_SocialLinkLBL.setText(_translate("SignUp", "Social Link:"))
        self.SU_TermsandPrivacyChB.setText(_translate("SignUp", "Accept the Terms and Condition; Privacy Policy"))
        self.SU_CreateanAccount.setText(_translate("SignUp", "Create an Account"))
        self.SU_EmailLBL.setText(_translate("SignUp", "Email:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUp = QtWidgets.QDialog()
    ui = Ui_SignUp()
    ui.setupUi(SignUp)
    SignUp.show()
    sys.exit(app.exec_())
