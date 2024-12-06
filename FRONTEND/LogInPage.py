# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PENPAL\LogInPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from FRONTEND.SignUpPage import Ui_SignUp  # Import Signup UI
import sys
import os


class Ui_LogIn(object):
    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(1440, 780)
        LogIn.setStyleSheet("background-color: rgb(255, 249, 240);\n"
"\n"
"")
        self.LI_Header = QtWidgets.QFrame(LogIn)
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
        self.LI_HeaderIcon = QtWidgets.QLabel(self.LI_Header)
        self.LI_HeaderIcon.setGeometry(QtCore.QRect(-70, -20, 274, 146))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(28)
        self.LI_HeaderIcon.setFont(font)
        self.LI_HeaderIcon.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;")
        self.LI_HeaderIcon.setText("")
        self.LI_HeaderIcon.setPixmap(QtGui.QPixmap("C:\\PENPAL\\HeaderIcon.png"))
        self.LI_HeaderIcon.setScaledContents(True)
        self.LI_HeaderIcon.setObjectName("LI_HeaderIcon")
        self.LI_MainPanel = QtWidgets.QFrame(LogIn)
        self.LI_MainPanel.setGeometry(QtCore.QRect(182, 136, 1082, 602))
        self.LI_MainPanel.setStyleSheet("background-color: rgb(255, 240, 216);")
        self.LI_MainPanel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LI_MainPanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LI_MainPanel.setObjectName("LI_MainPanel")
        self.LI_SidePanel = QtWidgets.QFrame(self.LI_MainPanel)
        self.LI_SidePanel.setGeometry(QtCore.QRect(660, 0, 421, 602))
        self.LI_SidePanel.setStyleSheet("background-color: rgb(255, 214, 182);")
        self.LI_SidePanel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LI_SidePanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LI_SidePanel.setObjectName("LI_SidePanel")
        self.LI_SidePanelBg = QtWidgets.QLabel(self.LI_SidePanel)
        self.LI_SidePanelBg.setGeometry(QtCore.QRect(-310, 0, 1071, 601))
        self.LI_SidePanelBg.setText("")
        self.LI_SidePanelBg.setPixmap(QtGui.QPixmap("C:\\PENPAL\\LI_SidePanel.png"))
        self.LI_SidePanelBg.setScaledContents(True)
        self.LI_SidePanelBg.setObjectName("LI_SidePanelBg")
        self.LI_StatementLBL = QtWidgets.QLabel(self.LI_SidePanel)
        self.LI_StatementLBL.setGeometry(QtCore.QRect(-140, 80, 721, 421))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LI_StatementLBL.setFont(font)
        self.LI_StatementLBL.setStyleSheet("color: rgb(122, 12, 12);\n"
"background: transparent;")
        self.LI_StatementLBL.setText("")
        self.LI_StatementLBL.setPixmap(QtGui.QPixmap("C:\\PENPAL\\LI_SignUpStatement.png"))
        self.LI_StatementLBL.setScaledContents(True)
        self.LI_StatementLBL.setObjectName("LI_StatementLBL")
        self.LI_SignUpPB = QtWidgets.QPushButton(self.LI_SidePanel)
        self.LI_SignUpPB.setGeometry(QtCore.QRect(160, 370, 119, 36))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.LI_SignUpPB.setFont(font)
        self.LI_SignUpPB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LI_SignUpPB.setStyleSheet("border-color: rgb(122, 12, 12);\n"
"color: rgb(122, 12, 12);\n"
"border: 3px solid #550808;\n"
"background-color: rgb(229, 141, 118);\n"
"border-radius: 10px;\n"
"text-decoration: underline;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.5);\n"
"text-color: #E58D76;\n"
"\n"
"")
        self.LI_SignUpPB.setCheckable(False)
        self.LI_SignUpPB.setAutoDefault(False)
        self.LI_SignUpPB.setDefault(True)
        self.LI_SignUpPB.setObjectName("LI_SignUpPB")
        self.LI_LogInToPenpal = QtWidgets.QLabel(self.LI_MainPanel)
        self.LI_LogInToPenpal.setGeometry(QtCore.QRect(130, 150, 411, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.LI_LogInToPenpal.setFont(font)
        self.LI_LogInToPenpal.setStyleSheet("color: rgb(122, 12, 12);\n"
"background: transparent;")
        self.LI_LogInToPenpal.setObjectName("LI_LogInToPenpal")
        self.LI_UsernameLBL = QtWidgets.QLabel(self.LI_MainPanel)
        self.LI_UsernameLBL.setGeometry(QtCore.QRect(30, 220, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LI_UsernameLBL.setFont(font)
        self.LI_UsernameLBL.setStyleSheet("color: rgb(122, 12, 12);\n"
"background: transparent;")
        self.LI_UsernameLBL.setObjectName("LI_UsernameLBL")
        self.LI_PasswordLBL = QtWidgets.QLabel(self.LI_MainPanel)
        self.LI_PasswordLBL.setGeometry(QtCore.QRect(30, 320, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LI_PasswordLBL.setFont(font)
        self.LI_PasswordLBL.setStyleSheet("color: rgb(122, 12, 12);\n"
"background: transparent;")
        self.LI_PasswordLBL.setObjectName("LI_PasswordLBL")
        self.LI_PasswordLE = QtWidgets.QLineEdit(self.LI_MainPanel)
        self.LI_PasswordLE.setGeometry(QtCore.QRect(120, 380, 441, 41))
        self.LI_PasswordLE.setStyleSheet("border-color: rgb(229, 141, 118);\n"
"border: 3px solid #E58D76;\n"
"border-radius: 5px;\n"
"background: transparent;")
        self.LI_PasswordLE.setObjectName("LI_PasswordLE")
        self.LI_LogInPB = QtWidgets.QPushButton(self.LI_MainPanel)
        self.LI_LogInPB.setGeometry(QtCore.QRect(250, 480, 119, 36))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.LI_LogInPB.setFont(font)
        self.LI_LogInPB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LI_LogInPB.setStyleSheet("border-color: rgb(229, 141, 118);\n"
"border: 3px solid #E58D76;\n"
"border-radius: 10px;\n"
"text-decoration: underline;\n"
"text-color: #E58D76;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.5);\n"
"background: transparent;\n"
"")
        self.LI_LogInPB.setDefault(False)
        self.LI_LogInPB.setFlat(False)
        self.LI_LogInPB.setObjectName("LI_LogInPB")
        self.LI_Icon = QtWidgets.QLabel(self.LI_MainPanel)
        self.LI_Icon.setGeometry(QtCore.QRect(-40, -10, 274, 146))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(28)
        self.LI_Icon.setFont(font)
        self.LI_Icon.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;")
        self.LI_Icon.setText("")
        self.LI_Icon.setPixmap(QtGui.QPixmap("C:\\PENPAL\\Icon.png"))
        self.LI_Icon.setScaledContents(True)
        self.LI_Icon.setObjectName("LI_Icon")
        self.LI_UsernameLE = QtWidgets.QLineEdit(self.LI_MainPanel)
        self.LI_UsernameLE.setGeometry(QtCore.QRect(120, 280, 441, 41))
        self.LI_UsernameLE.setStyleSheet("border-color: rgb(229, 141, 118);\n"
"border: 3px solid #E58D76;\n"
"border-radius: 5px;\n"
"background: transparent;")
        self.LI_UsernameLE.setObjectName("LI_UsernameLE")
        self.LI_ForgotPasswordLBL = QtWidgets.QLabel(self.LI_MainPanel)
        self.LI_ForgotPasswordLBL.setGeometry(QtCore.QRect(240, 430, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setUnderline(True)
        self.LI_ForgotPasswordLBL.setFont(font)
        self.LI_ForgotPasswordLBL.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LI_ForgotPasswordLBL.setStyleSheet("color: rgb(122, 12, 12);\n"
"background: transparent;\n"
"text-decoration: underline\n"
"")
        self.LI_ForgotPasswordLBL.setObjectName("LI_ForgotPasswordLBL")
        self.label = QtWidgets.QLabel(self.LI_MainPanel)
        self.label.setGeometry(QtCore.QRect(190, 0, 941, 671))
        self.label.setStyleSheet("background: transparent;\n"
"")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\PENPAL\\LI_Shadow.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.LI_SidePanel.raise_()
        self.LI_Icon.raise_()
        self.LI_ForgotPasswordLBL.raise_()
        self.LI_PasswordLE.raise_()
        self.LI_PasswordLBL.raise_()
        self.LI_UsernameLE.raise_()
        self.LI_UsernameLBL.raise_()
        self.LI_LogInToPenpal.raise_()
        self.LI_LogInPB.raise_()

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)
        
         # Connect buttons
        self.LI_SignUpPB.clicked.connect(self.openSignUpPage)
        
         # Persistent windows
        self.logInWindow = LogIn
        self.signUpWindow = None  # Initialize later
        
    def openSignUpPage(self):
        """Switch to the SignUp page."""
        if self.signUpWindow is None:  # Create only if not already created
            self.signUpWindow = QtWidgets.QDialog()  # Create dialog
            self.ui = Ui_SignUp()  # Use the imported SignUp class
            self.ui.setupUi(self.signUpWindow)

        self.logInWindow.hide()  # Hide the Login page
        self.signUpWindow.show()  # Show the Signup page

    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "Dialog"))
        self.LI_SignUpPB.setText(_translate("LogIn", "Sign Up"))
        self.LI_LogInToPenpal.setText(_translate("LogIn", "Log In to Penpal"))
        self.LI_UsernameLBL.setText(_translate("LogIn", "Username:"))
        self.LI_PasswordLBL.setText(_translate("LogIn", "Password:"))
        self.LI_LogInPB.setText(_translate("LogIn", "Log In"))
        self.LI_ForgotPasswordLBL.setText(_translate("LogIn", "Forgot Password?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QDialog()
    ui = Ui_LogIn()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())
