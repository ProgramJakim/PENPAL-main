# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PENPAL\SignUpPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
import os, requests
import re
import sys

# Get the absolute path of the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Build the general path to the resources/images folder
images_folder = os.path.join(current_directory, '..', 'resources', 'images')
Sign_Up_assets_folder = os.path.join(current_directory, '..', 'resources', 'images', 'Sign_Up_assets')

class Ui_SignUp(object):
    def setupUi(self, SignUp):
        SignUp.setObjectName("SignUp")
        SignUp.resize(1440, 780)
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
        self.SU_MainPanel.setGeometry(QtCore.QRect(182, 136, 1082, 602))
        self.SU_MainPanel.setStyleSheet("background-color: rgb(255, 240, 216);")
        self.SU_MainPanel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SU_MainPanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SU_MainPanel.setObjectName("SU_MainPanel")
        
#Side Panel
        self.SU_SidePanel = QtWidgets.QFrame(self.SU_MainPanel)
        self.SU_SidePanel.setGeometry(QtCore.QRect(0, 0, 421, 602))
        self.SU_SidePanel.setStyleSheet("background-color: rgb(255, 214, 182);")
        self.SU_SidePanel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SU_SidePanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SU_SidePanel.setObjectName("SU_SidePanel")

#Side Panel Background Image
        self.SU_SidePanelBg = QtWidgets.QLabel(self.SU_SidePanel)
        self.SU_SidePanelBg.setGeometry(QtCore.QRect(-170, 0, 931, 601))
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
        self.SU_SignUpPB = QtWidgets.QPushButton(self.SU_MainPanel)
        self.SU_SignUpPB.setGeometry(QtCore.QRect(680, 540, 119, 36))
        self.SU_SignUpPB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SU_SignUpPB.setStyleSheet("border-color: rgb(229, 141, 118);\n"
"border: 3px solid #E58D76;\n"
"border-radius: 10px;\n"
"text-decoration: underline;\n"
"text-color: #E58D76;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.5);\n"
"background: transparent;\n"
"")
        self.SU_SignUpPB.setObjectName("SU_SignUpPB")
        
#Age Label
        self.SU_AgeLBL = QtWidgets.QLabel(self.SU_MainPanel)
        self.SU_AgeLBL.setGeometry(QtCore.QRect(490, 240, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SU_AgeLBL.setFont(font)
        self.SU_AgeLBL.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;")
        self.SU_AgeLBL.setObjectName("SU_AgeLBL")
        
#Gender Check Box
        self.SU_GenderCB = QtWidgets.QComboBox(self.SU_MainPanel)
        self.SU_GenderCB.setGeometry(QtCore.QRect(830, 240, 141, 31))
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
        self.SU_LocationLBL_.setGeometry(QtCore.QRect(490, 290, 171, 21))
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
        self.SU_LocationLE.setGeometry(QtCore.QRect(550, 320, 421, 31))
        self.SU_LocationLE.setStyleSheet("border-color: rgb(229, 141, 118);\n"
"border: 3px solid #E58D76;\n"
"border-radius: 5px;\n"
"background: transparent;")
        self.SU_LocationLE.setObjectName("SU_LocationLE")
        
#Social Link Label
        self.SU_SocialLinkLBL = QtWidgets.QLabel(self.SU_MainPanel)
        self.SU_SocialLinkLBL.setGeometry(QtCore.QRect(490, 430, 151, 21))
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
        self.SU_SocialLinkLE.setGeometry(QtCore.QRect(550, 460, 421, 31))
        self.SU_SocialLinkLE.setStyleSheet("border-color: rgb(229, 141, 118);\n"
"border: 3px solid #E58D76;\n"
"border-radius: 5px;\n"
"background: transparent;")
        self.SU_SocialLinkLE.setObjectName("SU_SocialLinkLE")
        
#Terms and Privacy Check Box
        self.SU_TermsandPrivacyChB = QtWidgets.QCheckBox(self.SU_MainPanel)
        self.SU_TermsandPrivacyChB.setGeometry(QtCore.QRect(600, 510, 291, 20))
        self.SU_TermsandPrivacyChB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SU_TermsandPrivacyChB.setStyleSheet("background: transparent;    \n"
"")
        self.SU_TermsandPrivacyChB.setObjectName("SU_TermsandPrivacyChB")
        self.SU_TermsandPrivacyChB.clicked.connect(lambda: self.open_terms_and_conditions(SignUp))  # Connect checkbox to method

#Age Line Edit (Text Box)
        self.SU_AgeLE = QtWidgets.QLineEdit(self.SU_MainPanel)
        self.SU_AgeLE.setGeometry(QtCore.QRect(550, 240, 121, 31))
        self.SU_AgeLE.setStyleSheet("border-color: rgb(229, 141, 118);\n"
"border: 3px solid #E58D76;\n"
"border-radius: 5px;\n"
"background: transparent;")
        self.SU_AgeLE.setObjectName("SU_AgeLE")
        
#Shadow Image
        self.SU_Shadow = QtWidgets.QLabel(self.SU_MainPanel)
        self.SU_Shadow.setGeometry(QtCore.QRect(40, 0, 851, 611))
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
        self.SU_EmailLBL.setGeometry(QtCore.QRect(490, 360, 81, 21))
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
        self.SU_EmailLE.setGeometry(QtCore.QRect(550, 390, 421, 31))
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
        self.SU_AgeLBL.raise_()
        self.SU_GenderCB.raise_()
        self.SU_GenderLBL.raise_()
        self.SU_LocationLBL_.raise_()
        self.SU_LocationLE.raise_()
        self.SU_SocialLinkLBL.raise_()
        self.SU_SocialLinkLE.raise_()
        self.SU_TermsandPrivacyChB.raise_()
        self.SU_AgeLE.raise_()
        self.SU_CreateanAccount.raise_()
        self.SU_EmailLBL.raise_()
        self.SU_EmailLE.raise_()

        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)

        # Connect buttons
        self.SU_LogInPB.clicked.connect(lambda: self.backtoLogInPage(SignUp))

        # Connect the SignUp button to the method to send data
        self.SU_SignUpPB.clicked.connect(self.handle_signup)
        self.SU_SignUpPB.clicked.connect(self.on_sign_up_button_click)

     
    def handle_signup(self):
        username = self.SU_UsernameLE.text()
        password = self.SU_PasswordLE.text()
        age = self.SU_AgeLE.text()
        gender = self.SU_GenderCB.currentText()
        location = self.SU_LocationLE.text()
        social_media_link = self.SU_SocialLinkLE.text()
        gmail = self.SU_EmailLE.text()  # New field for Gmail account

        # Check if all fields are filled
        if not username or not password or not age or not location or not gender or not gmail:
                self.show_error_message("Please fill in all the required fields.")
                return False  # Indicate that the sign-up process should not continue

        # Validate password
        password_issue = self.validate_password(password)
        if password_issue:
                self.show_error_message(f"Error: {password_issue}. Please re-enter your password.")
                self.SU_PasswordLE.clear()  # Clear the password field to prompt re-entry
                return False  # Indicate that the sign-up process should not continue

        # Validate social media link
        if not self.validate_social_link():
                self.show_error_message("Invalid social media link. Please enter a valid link.")
                self.SU_SocialLinkLE.clear()  # Clear the link field to prompt re-entry
                return False  # Indicate that the sign-up process should not continue

        # Check if username already exists
        data = {'username': username}

        try:
                # First, check if the username exists
                response = requests.post('http://127.0.0.1:5000/check_username', json=data)

                if response.status_code == 400:  # Assuming the backend returns 400 if the username exists
                        self.show_error_message("Username already exists. Please choose another username.")
                        self.SU_UsernameLE.clear()  # Clear the username field to prompt re-entry
                        return False  # Indicate that the sign-up process should not continue

                # If the username is available, proceed with the sign-up process
                sign_up_data = {
                        'username': username,
                        'password': password,
                        'age': int(age),
                        'gender': gender,
                        'location': location,
                        'social_media_link': social_media_link,
                        'gmail': gmail  # Include the Gmail field in the sign-up data
                }

                # Send the data to the backend to create the account
                response = requests.post('http://127.0.0.1:5000/signup', json=sign_up_data)

                if response.status_code == 201:
                        self.show_success_message("Account created successfully!")

                        # Clear the input fields after sign-up
                        self.SU_UsernameLE.clear()
                        self.SU_PasswordLE.clear()
                        self.SU_AgeLE.clear()
                        self.SU_GenderCB.setCurrentIndex(0)  # Reset to first item (if applicable)
                        self.SU_LocationLE.clear()
                        self.SU_SocialLinkLE.clear()
                        self.SU_EmailLE.clear()  # Clear the Gmail field

                        self.show_success_message("You can continue creating another account or stay here.")

                        return True  # Indicate that the sign-up process succeeded
                else:
                        error_message = response.json().get('error', 'Unknown error occurred')
                        self.show_error_message(f"Error: {error_message}")
                        return False  # Indicate failure

        except requests.exceptions.RequestException as e:
                self.show_error_message(f"Request failed: {str(e)}")
                return False  # Indicate failure

    def show_success_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Success")
        msg.exec_()

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def validate_password(self, password):
        if len(password) < 8:
            return "Password must be at least 8 characters long."
        if not any(char.isdigit() for char in password):
            return "Password must include at least one number."
        if not any(char.isupper() for char in password):
            return "Password must include at least one uppercase letter."
        if not any(char in "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|" for char in password):
            return "Password must include at least one special character."
        return None

    def validate_social_link(self):
        social_link = self.SU_SocialLinkLE.text()
        # Updated pattern to allow periods in the path
        pattern = r"^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(/[\w\-\.]*)*$"
        return bool(re.match(pattern, social_link))
    def on_sign_up_button_click(self):
        if self.handle_signup():  # If sign-up is successful, proceed
            self.backtoLogInPage()
        else:
            # If there's an issue (password, social link, etc.), the user will have to fix it
            pass

    def backtoLogInPage(self, current_dialog):
        from LogInPage import Ui_LogIn
        self.logInWindow = QtWidgets.QDialog()
        self.ui = Ui_LogIn()
        self.ui.setupUi(self.logInWindow)
        self.logInWindow.show()
        current_dialog.close()

    def open_terms_and_conditions(self, current_dialog):
        from TermsAndCondition import Ui_Dialog
        self.termsWindow = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.termsWindow)
        self.termsWindow.show()
        current_dialog.close()

    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "Dialog"))
        self.SU_LogInPB.setText(_translate("SignUp", "Log In"))
        self.SU_UsernameLBL.setText(_translate("SignUp", "Username:"))
        self.SU_PasswordLBL.setText(_translate("SignUp", "Password:"))
        self.SU_SignUpPB.setText(_translate("SignUp", "Sign Up"))
        self.SU_AgeLBL.setText(_translate("SignUp", "Age: "))
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
