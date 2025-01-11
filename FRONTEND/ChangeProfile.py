# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PENPAL\ChangeProfile.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import requests
import re
import shutil
from PyQt5.QtWidgets import QMainWindow, QLabel, QDialog # Add this import
from PyQt5.QtGui import QPixmap

# Get the absolute path of the current directory 
current_directory = os.path.dirname(os.path.abspath(__file__))

# Build the general path to the resources/images folder
images_folder = os.path.join(current_directory, '..', 'resources' , 'images')
Change_Profile_assets_folder = os.path.join(current_directory, '..', 'resources' , 'images', 'Change_Profile_assets')


class Ui_ChangeProfile(object):
    def __init__(self):
        self.username = ""  # Initialize the username attribute
        self.selected_profile_picture = None  # Step 1: Add a variable to store the selected profile picture
        self.ChangeProfile = None
        self.main_window = None 

    def setupUi(self, ChangeProfile):
        self.ChangeProfile = ChangeProfile  # Store the ChangeProfile object
        ChangeProfile.setObjectName("Change Profile Picture")
        ChangeProfile.resize(1440, 780)
        
#Background Image
        self.CP_BackgroundImage = QtWidgets.QLabel(ChangeProfile)
        self.CP_BackgroundImage.setGeometry(QtCore.QRect(-80, -20, 1531, 841))
        self.CP_BackgroundImage.setText("")
        self.CP_BackgroundImage.setPixmap(QtGui.QPixmap(os.path.join(Change_Profile_assets_folder , "CP_BackgroundIm.png")))
        self.CP_BackgroundImage.setScaledContents(True)
        self.CP_BackgroundImage.setObjectName("CP_BackgroundImage")
        
#Profile Frame
        self.CP_ProfileFrame = QtWidgets.QFrame(ChangeProfile)
        self.CP_ProfileFrame.setGeometry(QtCore.QRect(194, 139, 1042, 607))
        self.CP_ProfileFrame.setStyleSheet("background-color: rgb(255, 240, 216);\n"
"border-radius: 5px;\n"
"border: 3px solid #BE7928;\n"
"")
        self.CP_ProfileFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CP_ProfileFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CP_ProfileFrame.setObjectName("CP_ProfileFrame")
        
#Header
        self.CP_Header = QtWidgets.QFrame(ChangeProfile)
        self.CP_Header.setGeometry(QtCore.QRect(0, 0, 1440, 105))
        self.CP_Header.setStyleSheet("background: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, y1:0, x2:1, y2:0, \n"
"    stop:0 #EDC27E, \n"
"    stop:0.526 #EDC27E, \n"
"    stop:1 #DC586D\n"
");\n"
"\n"
"")
        self.CP_Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CP_Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CP_Header.setObjectName("CP_Header")
        
#Header Icon
        self.CP_HeaderIcon = QtWidgets.QLabel(self.CP_Header)
        self.CP_HeaderIcon.setGeometry(QtCore.QRect(-60, -30, 242, 159))
        self.CP_HeaderIcon.setStyleSheet("background:transparent;")
        self.CP_HeaderIcon.setText("")
        self.CP_HeaderIcon.setPixmap(QtGui.QPixmap(os.path.join(images_folder , "HeaderIcon.png")))
        self.CP_HeaderIcon.setScaledContents(True)
        self.CP_HeaderIcon.setObjectName("CP_HeaderIcon")
        self.CP_SelectProfile = QtWidgets.QLabel(ChangeProfile)
        self.CP_SelectProfile.setGeometry(QtCore.QRect(510, 140, 431, 81))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        
#Select Profile Label
        self.CP_SelectProfile.setFont(font)
        self.CP_SelectProfile.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);")
        self.CP_SelectProfile.setObjectName("CP_SelectProfile")
        
#Default Profile
        self.CP_DefaultProfile = QtWidgets.QLabel(ChangeProfile)
        self.CP_DefaultProfile.setGeometry(QtCore.QRect(210, 210, 100, 100))
        self.CP_DefaultProfile.setLineWidth(1)
        self.CP_DefaultProfile.setText("")
        self.CP_DefaultProfile.setPixmap(QtGui.QPixmap(os.path.join(images_folder , "DefaultProfile.png")))
        self.CP_DefaultProfile.setScaledContents(True)
        self.CP_DefaultProfile.setObjectName("CP_DefaultProfile")
        
#Profile 1
        self.CP_profile1 = QtWidgets.QLabel(ChangeProfile)
        self.CP_profile1.setGeometry(QtCore.QRect(420, 330, 100, 100))
        self.CP_profile1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CP_profile1.setStyleSheet("")
        self.CP_profile1.setLineWidth(1)
        self.CP_profile1.setText("")
        self.CP_profile1.setPixmap(QtGui.QPixmap(os.path.join(Change_Profile_assets_folder ,"profile1.png")))
        self.CP_profile1.setScaledContents(True)
        self.CP_profile1.setObjectName("CP_profile1")
        self.CP_profile1.mousePressEvent = lambda event: self.select_profile_picture("profile1.png")  # Step 2: Add event handler
        
#Profile 2
        self.CP_profile2 = QtWidgets.QLabel(ChangeProfile)
        self.CP_profile2.setGeometry(QtCore.QRect(580, 330, 100, 100))
        self.CP_profile2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CP_profile2.setStyleSheet("")
        self.CP_profile2.setLineWidth(1)
        self.CP_profile2.setText("")
        self.CP_profile2.setPixmap(QtGui.QPixmap(os.path.join(Change_Profile_assets_folder , "profile2.png")))
        self.CP_profile2.setScaledContents(True)
        self.CP_profile2.setObjectName("CP_profile2")
        self.CP_profile2.mousePressEvent = lambda event: self.select_profile_picture("profile2.png")  # Step 2: Add event handler
        
#Profile 3
        self.CP_profile3 = QtWidgets.QLabel(ChangeProfile)
        self.CP_profile3.setGeometry(QtCore.QRect(740, 330, 100, 100))
        self.CP_profile3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CP_profile3.setStyleSheet("")
        self.CP_profile3.setLineWidth(1)
        self.CP_profile3.setText("")
        self.CP_profile3.setPixmap(QtGui.QPixmap(os.path.join(Change_Profile_assets_folder , "profile3.png")))
        self.CP_profile3.setScaledContents(True)
        self.CP_profile3.setObjectName("CP_profile3")
        self.CP_profile3.mousePressEvent = lambda event: self.select_profile_picture("profile3.png")  # Step 2: Add event handler
        
#Profile 4
        self.CP_profile4 = QtWidgets.QLabel(ChangeProfile)
        self.CP_profile4.setGeometry(QtCore.QRect(900, 330, 100, 100))
        self.CP_profile4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CP_profile4.setStyleSheet("")
        self.CP_profile4.setLineWidth(1)
        self.CP_profile4.setText("")
        self.CP_profile4.setPixmap(QtGui.QPixmap(os.path.join(Change_Profile_assets_folder , "profile4.png")))
        self.CP_profile4.setScaledContents(True)
        self.CP_profile4.setObjectName("CP_profile4")
        self.CP_profile4.mousePressEvent = lambda event: self.select_profile_picture("profile4.png")  # Step 2: Add event handler
        
#Profile 5
        self.CP_profile5 = QtWidgets.QLabel(ChangeProfile)
        self.CP_profile5.setGeometry(QtCore.QRect(420, 450, 100, 100))
        self.CP_profile5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CP_profile5.setStyleSheet("")
        self.CP_profile5.setLineWidth(1)
        self.CP_profile5.setText("")
        self.CP_profile5.setPixmap(QtGui.QPixmap(os.path.join(Change_Profile_assets_folder , "profile5.png")))
        self.CP_profile5.setScaledContents(True)
        self.CP_profile5.setObjectName("CP_profile5")
        self.CP_profile5.mousePressEvent = lambda event: self.select_profile_picture("profile5.png")  # Step 2: Add event handler
        
#Profile 6
        self.CP_profile6 = QtWidgets.QLabel(ChangeProfile)
        self.CP_profile6.setGeometry(QtCore.QRect(580, 450, 100, 100))
        self.CP_profile6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CP_profile6.setStyleSheet("")
        self.CP_profile6.setLineWidth(1)
        self.CP_profile6.setText("")
        self.CP_profile6.setPixmap(QtGui.QPixmap(os.path.join(Change_Profile_assets_folder , "profile6.png")))
        self.CP_profile6.setScaledContents(True)
        self.CP_profile6.setObjectName("CP_profile6")
        self.CP_profile6.mousePressEvent = lambda event: self.select_profile_picture("profile6.png")  # Step 2: Add event handler
        
#Profile 7
        self.CP_profile7 = QtWidgets.QLabel(ChangeProfile)
        self.CP_profile7.setGeometry(QtCore.QRect(740, 450, 100, 100))
        self.CP_profile7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CP_profile7.setStyleSheet("")
        self.CP_profile7.setLineWidth(1)
        self.CP_profile7.setText("")
        self.CP_profile7.setPixmap(QtGui.QPixmap(os.path.join(Change_Profile_assets_folder , "profile7.png")))
        self.CP_profile7.setScaledContents(True)
        self.CP_profile7.setObjectName("CP_profile7")
        self.CP_profile7.mousePressEvent = lambda event: self.select_profile_picture("profile7.png")  # Step 2: Add event handler
        
#Profile 8
        self.CP_profile8 = QtWidgets.QLabel(ChangeProfile)
        self.CP_profile8.setGeometry(QtCore.QRect(900, 450, 100, 100))
        self.CP_profile8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CP_profile8.setStyleSheet("")
        self.CP_profile8.setLineWidth(1)
        self.CP_profile8.setText("")
        self.CP_profile8.setPixmap(QtGui.QPixmap(os.path.join(Change_Profile_assets_folder , "profile8.png")))
        self.CP_profile8.setScaledContents(True)
        self.CP_profile8.setObjectName("CP_profile8")
        self.CP_profile8.mousePressEvent = lambda event: self.select_profile_picture("profile8.png")  # Step 2: Add event handler
        
#Profile 9
        self.CP_profile9 = QtWidgets.QLabel(ChangeProfile)
        self.CP_profile9.setGeometry(QtCore.QRect(420, 570, 100, 100))
        self.CP_profile9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CP_profile9.setStyleSheet("")
        self.CP_profile9.setLineWidth(1)
        self.CP_profile9.setText("")
        self.CP_profile9.setPixmap(QtGui.QPixmap(os.path.join(Change_Profile_assets_folder , "profile9.png")))
        self.CP_profile9.setScaledContents(True)
        self.CP_profile9.setObjectName("CP_profile9")
        self.CP_profile9.mousePressEvent = lambda event: self.select_profile_picture("profile9.png")  # Step 2: Add event handler
        
#Profile 10
        self.CP_profile10 = QtWidgets.QLabel(ChangeProfile)
        self.CP_profile10.setGeometry(QtCore.QRect(580, 570, 100, 100))
        self.CP_profile10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CP_profile10.setStyleSheet("")
        self.CP_profile10.setLineWidth(1)
        self.CP_profile10.setText("")
        self.CP_profile10.setPixmap(QtGui.QPixmap(os.path.join(Change_Profile_assets_folder , "profile10.png")))
        self.CP_profile10.setScaledContents(True)
        self.CP_profile10.setObjectName("CP_profile10")
        self.CP_profile10.mousePressEvent = lambda event: self.select_profile_picture("profile10.png")  # Step 2: Add event handler
        
#Profile 11
        self.CP_profile11 = QtWidgets.QLabel(ChangeProfile)
        self.CP_profile11.setGeometry(QtCore.QRect(740, 570, 100, 100))
        self.CP_profile11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CP_profile11.setStyleSheet("")
        self.CP_profile11.setLineWidth(1)
        self.CP_profile11.setText("")
        self.CP_profile11.setPixmap(QtGui.QPixmap(os.path.join(Change_Profile_assets_folder , "profile11.png")))
        self.CP_profile11.setScaledContents(True)
        self.CP_profile11.setObjectName("CP_profile11")
        self.CP_profile11.mousePressEvent = lambda event: self.select_profile_picture("profile11.png")  # Step 2: Add event handler
        
#Profile 12
        self.CP_profile12 = QtWidgets.QLabel(ChangeProfile)
        self.CP_profile12.setGeometry(QtCore.QRect(900, 570, 100, 100))
        self.CP_profile12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CP_profile12.setStyleSheet("")
        self.CP_profile12.setLineWidth(1)
        self.CP_profile12.setText("")
        self.CP_profile12.setPixmap(QtGui.QPixmap(os.path.join(Change_Profile_assets_folder , "profile12.png")))
        self.CP_profile12.setScaledContents(True)
        self.CP_profile12.setObjectName("CP_profile12")
        self.CP_profile12.mousePressEvent = lambda event: self.select_profile_picture("profile12.png")  # Step 2: Add event handler
        
#Cancel Changes Push Button
        self.CP_CancelChangesPB = QtWidgets.QPushButton(ChangeProfile)
        self.CP_CancelChangesPB.setGeometry(QtCore.QRect(960, 690, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.CP_CancelChangesPB.setFont(font)
        self.CP_CancelChangesPB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CP_CancelChangesPB.setStyleSheet("background-color: rgb(255, 187, 173);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.CP_CancelChangesPB.setObjectName("CP_CancelChangesPB")
        
#Save Changes Push Button
        self.CP_SaveChangesPB = QtWidgets.QPushButton(ChangeProfile)
        self.CP_SaveChangesPB.setGeometry(QtCore.QRect(1090, 690, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.CP_SaveChangesPB.setFont(font)
        self.CP_SaveChangesPB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CP_SaveChangesPB.setStyleSheet("background-color: rgb(255, 187, 173);\n"
"")
        self.CP_SaveChangesPB.setObjectName("CP_SaveChangesPB")
        self.CP_SaveChangesPB.clicked.connect(self.save_changes)  # Step 3: Connect the button

#Username Label
        self.CP_Username = QtWidgets.QLabel(ChangeProfile)
        self.CP_Username.setGeometry(QtCore.QRect(320, 240, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.CP_Username.setFont(font)
        self.CP_Username.setStyleSheet("Background: transparent;\n"
"color: rgb(122, 12, 12);")
        self.CP_Username.setScaledContents(True)
        self.CP_Username.setObjectName("CP_Username")
        
        self.CP_BackgroundImage.raise_()
        self.CP_ProfileFrame.raise_()
        self.CP_Header.raise_()
        self.CP_DefaultProfile.raise_()
        self.CP_SelectProfile.raise_()
        self.CP_profile1.raise_()
        self.CP_profile2.raise_()
        self.CP_profile3.raise_()
        self.CP_profile4.raise_()
        self.CP_profile5.raise_()
        self.CP_profile6.raise_()
        self.CP_profile7.raise_()
        self.CP_profile8.raise_()
        self.CP_profile9.raise_()
        self.CP_profile10.raise_()
        self.CP_profile11.raise_()
        self.CP_profile12.raise_()
        self.CP_CancelChangesPB.raise_()
        self.CP_SaveChangesPB.raise_()
        self.CP_Username.raise_()

        self.retranslateUi(ChangeProfile)
        QtCore.QMetaObject.connectSlotsByName(ChangeProfile)

    def retranslateUi(self, ChangeProfile):
        _translate = QtCore.QCoreApplication.translate
        ChangeProfile.setWindowTitle(_translate("ChangeProfile", "ChangeProfile"))
        self.CP_SelectProfile.setText(_translate("ChangeProfile", "Select your Profile"))
        self.CP_CancelChangesPB.setText(_translate("ChangeProfile", "Cancel"))
        self.CP_SaveChangesPB.setText(_translate("ChangeProfile", "Save Changes"))
        self.CP_Username.setText(_translate("ChangeProfile", "Username"))


#INFORMATION DISPLAY
        self.display_username()

    def set_user_info(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.display_username()

    def display_username(self):
        username = self.get_username_from_server()
        self.CP_Username.setText(username)

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
        
    def select_profile_picture(self, profile_picture):
        self.selected_profile_picture = profile_picture  # Step 2: Update the variable
        print(f"Selected profile picture: {self.selected_profile_picture}")  # Debug statement

        # Update the default profile picture preview
        self.CP_DefaultProfile.setPixmap(QtGui.QPixmap(os.path.join(Change_Profile_assets_folder, self.selected_profile_picture)))

    def save_changes(self):
        if self.selected_profile_picture:
                print(f"Saving profile picture: {self.selected_profile_picture}")  # Debug statement
                default_profile_path = os.path.join(Change_Profile_assets_folder, "default_profile.png")
                selected_profile_path = os.path.join(Change_Profile_assets_folder, self.selected_profile_picture)
                try:
                    shutil.copyfile(selected_profile_path, default_profile_path)
                    print(f"Copied {selected_profile_path} to {default_profile_path}")  # Debug statement
                    QtWidgets.QMessageBox.information(self.ChangeProfile, "Profile Updated", "Your profile picture has been updated.")
                    self.close_change_profile()  # Close the Change Profile window and show Profile Settings window
                except Exception as e:
                    print(f"Error copying file: {e}")  # Debug statement
                    QtWidgets.QMessageBox.critical(self.ChangeProfile, "Error", f"Failed to update profile picture: {e}")
        else:
             QtWidgets.QMessageBox.warning(self.ChangeProfile, "No Selection", "Please select a profile picture.")


    def close_change_profile(self):
        print("Closing ChangeProfile window and opening AccountSettings window")  # Debug statement
        self.ChangeProfile.accept()  # Use accept() instead of close() to properly close the dialog
        if self.main_window:
            print("main_window is set, calling openAccountSettingsFromChangeProfile")  # Debug statement
            self.main_window.openAccountSettingsFromChangeProfile()
        else:
            print("main_window is not set")

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.initWindows()
        

    def initUI(self):
        self.profile_picture_label = QLabel(self)  # Ensure this label is defined
        self.profile_picture_label.setGeometry(50, 50, 100, 100)
        self.load_profile_picture()

    def initWindows(self):
        self.accountSettingsWindow = QDialog()  # Initialize the account settings window
        

    def load_profile_picture(self):
        profile_picture_path = os.path.join(Change_Profile_assets_folder, "default_profile.png")
        if os.path.exists(profile_picture_path):
            self.profile_picture_label.setPixmap(QPixmap(profile_picture_path))
        else:
            print("Default profile picture not found.")  # Debug statement

    def show_change_profile(self):
        self.change_profile_window = QDialog()
        self.change_profile_ui = Ui_ChangeProfile()
        self.change_profile_ui.setupUi(self.change_profile_window)
        self.change_profile_ui.main_window = self  # Pass the main window reference
        self.change_profile_ui.CP_SaveChangesPB.clicked.connect(self.load_profile_picture)  # Reload profile picture after saving changes
        self.change_profile_window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChangeProfile = QtWidgets.QDialog()
    ui = Ui_ChangeProfile()
    ui.setupUi(ChangeProfile)
    ChangeProfile.show()
    sys.exit(app.exec_())
