# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PENPAL\AccountSettings.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import requests

# Get the absolute path of the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Build the general path to the resources/images folder
images_folder = os.path.join(current_directory, '..', 'resources', 'images')
Account_Settings_assets_folder = os.path.join(current_directory, '..', 'resources', 'images', 'Account_Settings_assets')

class Ui_AccountSettings(object):
    def setupUi(self, AccountSettings):
        AccountSettings.setObjectName("AccountSettings")
        AccountSettings.setFixedSize(1440, 750)
        self.user_id = None
        self.username = None
        
#Header
        self.AS_Header = QtWidgets.QFrame(AccountSettings)
        self.AS_Header.setGeometry(QtCore.QRect(0, 0, 1440, 103))
        self.AS_Header.setStyleSheet("background: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, y1:0, x2:1, y2:0, \n"
"    stop:0 #EDC27E, \n"
"    stop:0.526 #EDC27E, \n"
"    stop:1 #DC586D\n"
");\n"
"\n"
"")
        self.AS_Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AS_Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AS_Header.setObjectName("AS_Header")
        
#Home Push Button
        self.AS_HomePB = QtWidgets.QPushButton(self.AS_Header)
        self.AS_HomePB.setGeometry(QtCore.QRect(920, 50, 150, 45))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.AS_HomePB.setFont(font)
        self.AS_HomePB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AS_HomePB.setStyleSheet("color:rgb(255, 255, 255);\n"
"border-color: rgb(229, 141, 118);\n"
"border: 3px solid #FFFFFF;\n"
"border-radius: 20px;\n"
"background: transparent;\n"
"")
        self.AS_HomePB.setObjectName("AS_HomePB")
        
#Menu Push Button
        self.AS_MenuPB = QtWidgets.QPushButton(self.AS_Header)
        self.AS_MenuPB.setGeometry(QtCore.QRect(1080, 50, 150, 45))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.AS_MenuPB.setFont(font)
        self.AS_MenuPB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AS_MenuPB.setStyleSheet("color:rgb(255, 255, 255);\n"
"border-color: rgb(229, 141, 118);\n"
"border: 3px solid #FFFFFF;\n"
"border-radius: 20px;\n"
"background: transparent;\n"
"")
        self.AS_MenuPB.setObjectName("AS_MenuPB")
        
#Log Out Push Button
        self.AS_LogOutPB = QtWidgets.QPushButton(self.AS_Header)
        self.AS_LogOutPB.setGeometry(QtCore.QRect(1240, 50, 150, 45))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.AS_LogOutPB.setFont(font)
        self.AS_LogOutPB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AS_LogOutPB.setStyleSheet("color:rgb(255, 255, 255);\n"
"border-color: rgb(229, 141, 118);\n"
"border: 3px solid #FFFFFF;\n"
"border-radius: 20px;\n"
"background: transparent;\n"
"")
        self.AS_LogOutPB.setObjectName("AS_LogOutPB")
        
#Header Icon
        self.AS_HeaderIcon = QtWidgets.QLabel(self.AS_Header)
        self.AS_HeaderIcon.setGeometry(QtCore.QRect(-50, -30, 242, 159))
        self.AS_HeaderIcon.setStyleSheet("background:transparent;")
        self.AS_HeaderIcon.setText("")
        self.AS_HeaderIcon.setPixmap(QtGui.QPixmap(os.path.join(images_folder ,'HeaderIcon.png')))
        self.AS_HeaderIcon.setScaledContents(True)
        self.AS_HeaderIcon.setObjectName("AS_HeaderIcon")
        
#Background Image
        self.AS_BackgroundImage = QtWidgets.QLabel(AccountSettings)
        self.AS_BackgroundImage.setGeometry(QtCore.QRect(0, 0, 1440, 780))
        self.AS_BackgroundImage.setText("")
        self.AS_BackgroundImage.setPixmap(QtGui.QPixmap(os.path.join(Account_Settings_assets_folder ,'AS_BackgroundIm.png')))
        self.AS_BackgroundImage.setScaledContents(True)
        self.AS_BackgroundImage.setObjectName("AS_BackgroundImage")
        
#Display Frame
        self.AS_DisplayFrame = QtWidgets.QFrame(AccountSettings)
        self.AS_DisplayFrame.setGeometry(QtCore.QRect(120, 150, 445, 600))
        self.AS_DisplayFrame.setStyleSheet("background-color: rgb(255, 240, 216);\n"
"border-radius: 5px;\n"
"border: 3px solid #BE7928;\n"
"")
        self.AS_DisplayFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AS_DisplayFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AS_DisplayFrame.setObjectName("AS_DisplayFrame")
        
#Edit Frame
        self.AS_EditFrame = QtWidgets.QFrame(AccountSettings)
        self.AS_EditFrame.setGeometry(QtCore.QRect(590, 150, 711, 600))
        self.AS_EditFrame.setStyleSheet("\n"
"border-radius: 5px;\n"
"border: 3px solid #BE7928;\n"
"background-color: rgb(255, 214, 182);")
        self.AS_EditFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AS_EditFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AS_EditFrame.setObjectName("AS_EditFrame")
        
#Account Settings Label
        self.AS_AccountSettingsLBL = QtWidgets.QLabel(AccountSettings)
        self.AS_AccountSettingsLBL.setGeometry(QtCore.QRect(840, 170, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AS_AccountSettingsLBL.setFont(font)
        self.AS_AccountSettingsLBL.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);")
        self.AS_AccountSettingsLBL.setObjectName("AS_AccountSettingsLBL")
        
#Default Profile
        self.AS_DefaultProfile = QtWidgets.QLabel(AccountSettings)
        self.AS_DefaultProfile.setGeometry(QtCore.QRect(130, 160, 100, 100))
        self.AS_DefaultProfile.setText("")
        self.AS_DefaultProfile.setPixmap(QtGui.QPixmap(os.path.join( images_folder , "DefaultProfile.png")))
        self.AS_DefaultProfile.setScaledContents(True)
        self.AS_DefaultProfile.setObjectName("AS_DefaultProfile")
        
#Username Label
        self.AS_Username = QtWidgets.QLabel(AccountSettings)
        self.AS_Username.setGeometry(QtCore.QRect(240, 190, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AS_Username.setFont(font)
        self.AS_Username.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);")
        self.AS_Username.setScaledContents(True)
        self.AS_Username.setObjectName("AS_Username")
        
#Age Display
        self.AS_AgeDisplay = QtWidgets.QLabel(AccountSettings)
        self.AS_AgeDisplay.setGeometry(QtCore.QRect(220, 280, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AS_AgeDisplay.setFont(font)
        self.AS_AgeDisplay.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);\n"
"")
        self.AS_AgeDisplay.setScaledContents(True)
        self.AS_AgeDisplay.setObjectName("AS_AgeDisplay")
        
#Age
        self.AS_Age = QtWidgets.QLabel(AccountSettings)
        self.AS_Age.setGeometry(QtCore.QRect(140, 280, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AS_Age.setFont(font)
        self.AS_Age.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);\n"
"")
        self.AS_Age.setScaledContents(True)
        self.AS_Age.setObjectName("AS_Age")
        
#Gender
        self.AS_Gender = QtWidgets.QLabel(AccountSettings)
        self.AS_Gender.setGeometry(QtCore.QRect(140, 340, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AS_Gender.setFont(font)
        self.AS_Gender.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);\n"
"")
        self.AS_Gender.setScaledContents(True)
        self.AS_Gender.setObjectName("AS_Gender")
        
#Gender Display
        self.AS_GenderDisplay = QtWidgets.QLabel(AccountSettings)
        self.AS_GenderDisplay.setGeometry(QtCore.QRect(270, 340, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AS_GenderDisplay.setFont(font)
        self.AS_GenderDisplay.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);\n"
"")
        self.AS_GenderDisplay.setScaledContents(True)
        self.AS_GenderDisplay.setObjectName("AS_GenderDisplay")
        
#Location
        self.AS_Location = QtWidgets.QLabel(AccountSettings)
        self.AS_Location.setGeometry(QtCore.QRect(140, 400, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AS_Location.setFont(font)
        self.AS_Location.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);\n"
"")
        self.AS_Location.setScaledContents(True)
        self.AS_Location.setObjectName("AS_Location")
        
#Location Display
        self.AS_LocationDisplay = QtWidgets.QLabel(AccountSettings)
        self.AS_LocationDisplay.setGeometry(QtCore.QRect(290, 400, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AS_LocationDisplay.setFont(font)
        self.AS_LocationDisplay.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);\n"
"")
        self.AS_LocationDisplay.setScaledContents(True)
        self.AS_LocationDisplay.setObjectName("AS_LocationDisplay")
        
#Social Links
        self.AS_SociaLinks = QtWidgets.QLabel(AccountSettings)
        self.AS_SociaLinks.setGeometry(QtCore.QRect(140, 460, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AS_SociaLinks.setFont(font)
        self.AS_SociaLinks.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);\n"
"")
        self.AS_SociaLinks.setScaledContents(True)
        self.AS_SociaLinks.setObjectName("AS_SociaLinks")

#Social Link Display
        self.AS_SocialLinkDisplay = QtWidgets.QLabel(AccountSettings)
        self.AS_SocialLinkDisplay.setGeometry(QtCore.QRect(250, 510, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AS_SocialLinkDisplay.setFont(font)
        self.AS_SocialLinkDisplay.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);\n"
"")
        self.AS_SocialLinkDisplay.setScaledContents(True)
        self.AS_SocialLinkDisplay.setObjectName("AS_SocialLinkDisplay")
        
#Preferences
        self.AS_Preferences = QtWidgets.QLabel(AccountSettings)
        self.AS_Preferences.setGeometry(QtCore.QRect(140, 570, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AS_Preferences.setFont(font)
        self.AS_Preferences.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);\n"
"")
        self.AS_Preferences.setScaledContents(True)
        self.AS_Preferences.setObjectName("AS_Preferences")
        
#Preference 1 Display
        self.AS_Preference1Display = QtWidgets.QLabel(AccountSettings)
        self.AS_Preference1Display.setGeometry(QtCore.QRect(340, 570, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AS_Preference1Display.setFont(font)
        self.AS_Preference1Display.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);\n"
"")
        self.AS_Preference1Display.setScaledContents(True)
        self.AS_Preference1Display.setObjectName("AS_Preference1Display")
        
#Preference 2 Display
        self.AS_Preference2Display = QtWidgets.QLabel(AccountSettings)
        self.AS_Preference2Display.setGeometry(QtCore.QRect(150, 620, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AS_Preference2Display.setFont(font)
        self.AS_Preference2Display.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);\n"
"")
        self.AS_Preference2Display.setScaledContents(True)
        self.AS_Preference2Display.setObjectName("AS_Preference2Display")
        
#Preference 3 Display
        self.AS_Preference3Display = QtWidgets.QLabel(AccountSettings)
        self.AS_Preference3Display.setGeometry(QtCore.QRect(350, 620, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AS_Preference3Display.setFont(font)
        self.AS_Preference3Display.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);\n"
"")
        self.AS_Preference3Display.setScaledContents(True)
        self.AS_Preference3Display.setObjectName("AS_Preference3Display")
        
#Preference 4 Display
        self.AS_Preference4Display = QtWidgets.QLabel(AccountSettings)
        self.AS_Preference4Display.setGeometry(QtCore.QRect(150, 670, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AS_Preference4Display.setFont(font)
        self.AS_Preference4Display.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);\n"
"")
        self.AS_Preference4Display.setScaledContents(True)
        self.AS_Preference4Display.setObjectName("AS_Preference4Display")
        
#Preference 5 Display
        self.AS_Preference5Display = QtWidgets.QLabel(AccountSettings)
        self.AS_Preference5Display.setGeometry(QtCore.QRect(350, 670, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AS_Preference5Display.setFont(font)
        self.AS_Preference5Display.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);\n"
"")
        self.AS_Preference5Display.setScaledContents(True)
        self.AS_Preference5Display.setObjectName("AS_Preference5Display")
        
#Edit Avatar (Default Profile)
        self.AS_EditAvatar = QtWidgets.QLabel(AccountSettings)
        self.AS_EditAvatar.setGeometry(QtCore.QRect(610, 220, 80, 80))
        self.AS_EditAvatar.setText("")
        self.AS_EditAvatar.setPixmap(QtGui.QPixmap(os.path.join(images_folder , "DefaultProfile.png")))
        self.AS_EditAvatar.setScaledContents(True)
        self.AS_EditAvatar.setObjectName("AS_EditAvatar")
        
#Username Number 2  (inside the editing frame)
        self.AS_Username2 = QtWidgets.QLabel(AccountSettings)
        self.AS_Username2.setGeometry(QtCore.QRect(700, 230, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.AS_Username2.setFont(font)
        self.AS_Username2.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);")
        self.AS_Username2.setScaledContents(True)
        self.AS_Username2.setObjectName("AS_Username2")
        
#Edit Password Label
        self.AS_EditPassword = QtWidgets.QLabel(AccountSettings)
        self.AS_EditPassword.setGeometry(QtCore.QRect(620, 320, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.AS_EditPassword.setFont(font)
        self.AS_EditPassword.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);")
        self.AS_EditPassword.setScaledContents(True)
        self.AS_EditPassword.setObjectName("AS_EditPassword")
        
#Confirm Password Label
        self.AS_ConfirmPassword = QtWidgets.QLabel(AccountSettings)
        self.AS_ConfirmPassword.setGeometry(QtCore.QRect(620, 410, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.AS_ConfirmPassword.setFont(font)
        self.AS_ConfirmPassword.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);")
        self.AS_ConfirmPassword.setScaledContents(True)
        self.AS_ConfirmPassword.setObjectName("AS_ConfirmPassword")
        
#Edit Social Link Label
        self.AS_EditSocialLink = QtWidgets.QLabel(AccountSettings)
        self.AS_EditSocialLink.setGeometry(QtCore.QRect(620, 520, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.AS_EditSocialLink.setFont(font)
        self.AS_EditSocialLink.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);")
        self.AS_EditSocialLink.setScaledContents(True)
        self.AS_EditSocialLink.setObjectName("AS_EditSocialLink")
        
#Confirm Social Link Label
        self.AS_ConfirmSocialLink = QtWidgets.QLabel(AccountSettings)
        self.AS_ConfirmSocialLink.setGeometry(QtCore.QRect(620, 600, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.AS_ConfirmSocialLink.setFont(font)
        self.AS_ConfirmSocialLink.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);")
        self.AS_ConfirmSocialLink.setScaledContents(True)
        self.AS_ConfirmSocialLink.setObjectName("AS_ConfirmSocialLink")
        
#Save Changes Push Button
        self.AS_SaveChangesPB = QtWidgets.QPushButton(AccountSettings)
        self.AS_SaveChangesPB.setGeometry(QtCore.QRect(1180, 710, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.AS_SaveChangesPB.setFont(font)
        self.AS_SaveChangesPB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AS_SaveChangesPB.setStyleSheet("background-color: rgb(255, 187, 173);\n"
"")
        self.AS_SaveChangesPB.setObjectName("AS_SaveChangesPB")
        
#Enter New Password Line Edit (Text Box)
        self.AS_EnterNewPassLE = QtWidgets.QLineEdit(AccountSettings)
        self.AS_EnterNewPassLE.setGeometry(QtCore.QRect(750, 360, 431, 41))
        self.AS_EnterNewPassLE.setStyleSheet("border: 3px solid #7A0C0C;\n"
"background-color: rgb(255, 240, 216);\n"
"\n"
"")
        self.AS_EnterNewPassLE.setObjectName("AS_EnterNewPassLE")
        
#Confirm New Password Line Edit (Text Box)
        self.AS_ConfirmNewPass = QtWidgets.QLineEdit(AccountSettings)
        self.AS_ConfirmNewPass.setGeometry(QtCore.QRect(750, 450, 431, 41))
        self.AS_ConfirmNewPass.setStyleSheet("border: 3px solid #7A0C0C;\n" 
"background-color: rgb(255, 240, 216);\n"
"\n"
"")
        self.AS_ConfirmNewPass.setObjectName("AS_ConfirmNewPass")
        
#Enter New Social Link Line Edit (Text Box)
        self.AS_EnterNewSocialLinkLE = QtWidgets.QLineEdit(AccountSettings)
        self.AS_EnterNewSocialLinkLE.setGeometry(QtCore.QRect(750, 560, 431, 41))
        self.AS_EnterNewSocialLinkLE.setStyleSheet("border: 3px solid #7A0C0C;\n"
"background-color: rgb(255, 240, 216);\n"
"\n"
"")
        self.AS_EnterNewSocialLinkLE.setObjectName("AS_EnterNewSocialLinkLE")
        
#Confirm New Social Link Line Edit (Text Box)
        self.AS_ConfirmNewSocialLinkLE = QtWidgets.QLineEdit(AccountSettings)
        self.AS_ConfirmNewSocialLinkLE.setGeometry(QtCore.QRect(750, 640, 431, 41))
        self.AS_ConfirmNewSocialLinkLE.setStyleSheet("border: 3px solid #7A0C0C;\n"
"background-color: rgb(255, 240, 216);\n"
"\n"
"")
        self.AS_ConfirmNewSocialLinkLE.setObjectName("AS_ConfirmNewSocialLinkLE")
        
#Delete Account Push Button
        self.AS_DeleteAccPB = QtWidgets.QPushButton(AccountSettings)
        self.AS_DeleteAccPB.setGeometry(QtCore.QRect(1080, 710, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.AS_DeleteAccPB.setFont(font)
        self.AS_DeleteAccPB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AS_DeleteAccPB.setStyleSheet("background-color: rgb(255, 187, 173);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.AS_DeleteAccPB.setObjectName("AS_DeleteAccPB")
        
#Edit Avatar Push Button
        self.AS_EditAvatarPB = QtWidgets.QPushButton(AccountSettings)
        self.AS_EditAvatarPB.setGeometry(QtCore.QRect(710, 270, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.AS_EditAvatarPB.setFont(font)
        self.AS_EditAvatarPB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AS_EditAvatarPB.setStyleSheet("background-color: rgb(255, 187, 173);\n"
"")
        self.AS_EditAvatarPB.setObjectName("AS_EditAvatarPB")
        
        
        self.AS_BackgroundImage.raise_()
        self.AS_Header.raise_()
        self.AS_DisplayFrame.raise_()
        self.AS_EditFrame.raise_()
        self.AS_AccountSettingsLBL.raise_()
        self.AS_DefaultProfile.raise_()
        self.AS_Username.raise_()
        self.AS_AgeDisplay.raise_()
        self.AS_Age.raise_()
        self.AS_Gender.raise_()
        self.AS_GenderDisplay.raise_()
        self.AS_Location.raise_()
        self.AS_LocationDisplay.raise_()
        self.AS_SociaLinks.raise_()
        self.AS_SocialLinkDisplay.raise_()
        self.AS_Preferences.raise_()
        self.AS_Preference1Display.raise_()
        self.AS_Preference2Display.raise_()
        self.AS_Preference3Display.raise_()
        self.AS_Preference4Display.raise_()
        self.AS_Preference5Display.raise_()
        self.AS_EditAvatar.raise_()
        self.AS_Username2.raise_()
        self.AS_EditPassword.raise_()
        self.AS_ConfirmPassword.raise_()
        self.AS_EditSocialLink.raise_()
        self.AS_ConfirmSocialLink.raise_()
        self.AS_SaveChangesPB.raise_()
        self.AS_EnterNewPassLE.raise_()
        self.AS_ConfirmNewPass.raise_()
        self.AS_EnterNewSocialLinkLE.raise_()
        self.AS_ConfirmNewSocialLinkLE.raise_()
        self.AS_DeleteAccPB.raise_()
        self.AS_EditAvatarPB.raise_()

        self.retranslateUi(AccountSettings)
        QtCore.QMetaObject.connectSlotsByName(AccountSettings)

    def retranslateUi(self, AccountSettings):
        _translate = QtCore.QCoreApplication.translate
        AccountSettings.setWindowTitle(_translate("AccountSettings", "Dialog"))
        self.AS_HomePB.setText(_translate("AccountSettings", "Home"))
        self.AS_MenuPB.setText(_translate("AccountSettings", "Menu"))
        self.AS_LogOutPB.setText(_translate("AccountSettings", "Log Out"))
        self.AS_AccountSettingsLBL.setText(_translate("AccountSettings", "Account Settings"))
        self.AS_Username.setText(_translate("AccountSettings", "Username"))
        self.AS_AgeDisplay.setText(_translate("AccountSettings", "Age"))
        self.AS_Age.setText(_translate("AccountSettings", "Age:"))
        self.AS_Gender.setText(_translate("AccountSettings", "Gender:"))
        self.AS_GenderDisplay.setText(_translate("AccountSettings", "Gender"))
        self.AS_Location.setText(_translate("AccountSettings", "Location:"))
        self.AS_LocationDisplay.setText(_translate("AccountSettings", "Location"))
        self.AS_SociaLinks.setText(_translate("AccountSettings", "Social Links:"))
        self.AS_SocialLinkDisplay.setText(_translate("AccountSettings", "Social Link 1"))
        self.AS_Preferences.setText(_translate("AccountSettings", "Preferences:"))
        self.AS_Preference1Display.setText(_translate("AccountSettings", "Preference1"))
        self.AS_Preference2Display.setText(_translate("AccountSettings", "Preference2"))
        self.AS_Preference3Display.setText(_translate("AccountSettings", "Preference3"))
        self.AS_Preference4Display.setText(_translate("AccountSettings", "Preference4"))
        self.AS_Preference5Display.setText(_translate("AccountSettings", "Preference5"))
        self.AS_Username2.setText(_translate("AccountSettings", "Username"))
        self.AS_EditPassword.setText(_translate("AccountSettings", "Enter New Password:"))
        self.AS_ConfirmPassword.setText(_translate("AccountSettings", "Confirm New Password:"))
        self.AS_EditSocialLink.setText(_translate("AccountSettings", "Enter New Social Link:"))
        self.AS_ConfirmSocialLink.setText(_translate("AccountSettings", "Confirm New Social Link:"))
        self.AS_SaveChangesPB.setText(_translate("AccountSettings", "Save Changes"))
        self.AS_DeleteAccPB.setText(_translate("AccountSettings", "Delete Account"))
        self.AS_EditAvatarPB.setText(_translate("AccountSettings", "Edit Avatar"))

#USERNAME DISPLAY
        self.display_username()

    def set_user_info(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.display_username()
        
    def display_username(self):
        username = self.get_username_from_server()
        self.AS_Username.setText(username)
        self.AS_Username2.setText(username)

    
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
    AccountSettings = QtWidgets.QDialog()
    ui = Ui_AccountSettings()
    ui.setupUi(AccountSettings)
    AccountSettings.show()
    sys.exit(app.exec_())
