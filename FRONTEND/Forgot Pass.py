# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\chris\OneDrive\Desktop\For Python Code\penpal\Forgot Pass.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os
from PyQt5 import QtCore, QtGui, QtWidgets

# Get the absolute path of the current directory (LogInPage.py)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Build the general path to the resources/images folder
images_folder = os.path.join(current_directory, '..', 'resources', 'images')
Interest_assets_folder = os.path.join(current_directory, '..', 'resources', 'images', 'Interest_assets')


class Ui_ForgotPassword_Fullpage(object):
    def setupUi(self, ForgotPassword_Fullpage):
        ForgotPassword_Fullpage.setObjectName("ForgotPassword_Fullpage")
        ForgotPassword_Fullpage.resize(1440, 780)
        ForgotPassword_Fullpage.setMinimumSize(QtCore.QSize(581, 96))
        ForgotPassword_Fullpage.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FP_Top = QtWidgets.QFrame(ForgotPassword_Fullpage)
        self.FP_Top.setGeometry(QtCore.QRect(0, 0, 1440, 105))
        self.FP_Top.setStyleSheet("background: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, y1:0, x2:1, y2:0, \n"
"    stop:0 #EDC27E, \n"
"    stop:0.526 #EDC27E, \n"
"    stop:1 #DC586D\n"
");\n"
"\n"
"")
        self.FP_Top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FP_Top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FP_Top.setObjectName("FP_Top")
        self.FP_HeaderIcon = QtWidgets.QLabel(self.FP_Top)
        self.FP_HeaderIcon.setGeometry(QtCore.QRect(-70, -20, 274, 146))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(28)
        self.FP_HeaderIcon.setFont(font)
        self.FP_HeaderIcon.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;")
        self.FP_HeaderIcon.setText("")
        self.FP_HeaderIcon.setPixmap(QtGui.QPixmap("C:\\Users\\chris\\OneDrive\\Desktop\\For Python Code\\penpal\\../../../../Downloads/HeaderIcon.png"))
        self.FP_HeaderIcon.setScaledContents(True)
        self.FP_HeaderIcon.setObjectName("FP_HeaderIcon")
        self.frame = QtWidgets.QFrame(ForgotPassword_Fullpage)
        self.frame.setGeometry(QtCore.QRect(261, 149, 901, 602))
        self.frame.setMinimumSize(QtCore.QSize(901, 602))
        self.frame.setStyleSheet("background-color: rgb(255, 240, 216);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.FP_EmailText = QtWidgets.QLabel(self.frame)
        self.FP_EmailText.setGeometry(QtCore.QRect(40, 240, 351, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FP_EmailText.sizePolicy().hasHeightForWidth())
        self.FP_EmailText.setSizePolicy(sizePolicy)
        self.FP_EmailText.setMinimumSize(QtCore.QSize(351, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        self.FP_EmailText.setFont(font)
        self.FP_EmailText.setStyleSheet("color: rgb(122, 12, 12); font-size: 23px;")
        self.FP_EmailText.setObjectName("FP_EmailText")
        self.FP_EmailBox = QtWidgets.QFrame(self.frame)
        self.FP_EmailBox.setGeometry(QtCore.QRect(100, 290, 323, 36))
        self.FP_EmailBox.setMinimumSize(QtCore.QSize(323, 36))
        self.FP_EmailBox.setStyleSheet("background-color: rgb(255, 240, 216);\n"
"border: 2px solid #E58D76;")
        self.FP_EmailBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FP_EmailBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FP_EmailBox.setObjectName("FP_EmailBox")
        self.FP_SubmitBox = QtWidgets.QFrame(self.frame)
        self.FP_SubmitBox.setGeometry(QtCore.QRect(300, 410, 119, 36))
        self.FP_SubmitBox.setMinimumSize(QtCore.QSize(119, 36))
        self.FP_SubmitBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.FP_SubmitBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FP_SubmitBox.setStyleSheet("border-color: rgb(220, 97, 88);\n"
"border: 3px solid #DC6158;\n"
"border-radius: 5px;\n"
"")
        self.FP_SubmitBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FP_SubmitBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FP_SubmitBox.setObjectName("FP_SubmitBox")
        self.label_5 = QtWidgets.QLabel(self.FP_SubmitBox)
        self.label_5.setGeometry(QtCore.QRect(32, -23, 350, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(350, 36))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777212))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(220, 97, 88); font-size: 23px;\n"
"background: transparent;\n"
"border: none")
        self.label_5.setObjectName("label_5")
        self.ForgotPassTEXT = QtWidgets.QLabel(self.frame)
        self.ForgotPassTEXT.setGeometry(QtCore.QRect(90, 135, 800, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.ForgotPassTEXT.sizePolicy().hasHeightForWidth())
        self.ForgotPassTEXT.setSizePolicy(sizePolicy)
        self.ForgotPassTEXT.setMinimumSize(QtCore.QSize(288, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(16)
        font.setBold(False)
        self.ForgotPassTEXT.setFont(font)
        self.ForgotPassTEXT.setStyleSheet("color:rgb(122, 12, 12);")
        self.ForgotPassTEXT.setObjectName("ForgotPassTEXT")
        self.FP_Shadow = QtWidgets.QLabel(self.frame)
        self.FP_Shadow.setGeometry(QtCore.QRect(-30, 0, 1031, 601))
        self.FP_Shadow.setStyleSheet("background: transparent;")
        self.FP_Shadow.setText("")
        self.FP_Shadow.setPixmap(QtGui.QPixmap("C:\\Users\\chris\\OneDrive\\Desktop\\For Python Code\\penpal\\../../PenpalFE/FPshadow.png"))
        self.FP_Shadow.setScaledContents(True)
        self.FP_Shadow.setObjectName("FP_Shadow")
        self.FPimage1 = QtWidgets.QLabel(self.frame)
        self.FPimage1.setGeometry(QtCore.QRect(140, 0, 1131, 602))
        self.FPimage1.setMinimumSize(QtCore.QSize(421, 602))
        self.FPimage1.setStyleSheet("background: transparent;")
        self.FPimage1.setText("")
        self.FPimage1.setPixmap(QtGui.QPixmap("C:\\Users\\chris\\OneDrive\\Desktop\\For Python Code\\penpal\\../../PenpalFE/FPimage1.png"))
        self.FPimage1.setScaledContents(True)
        self.FPimage1.setObjectName("FPimage1")
        self.FP_Logo = QtWidgets.QLabel(self.frame)
        self.FP_Logo.setGeometry(QtCore.QRect(-50, 0, 245, 127))
        self.FP_Logo.setText("")
        self.FP_Logo.setPixmap(QtGui.QPixmap("C:\\Users\\chris\\OneDrive\\Desktop\\For Python Code\\penpal\\../../PenpalFE/FPlogo.png"))
        self.FP_Logo.setScaledContents(True)
        self.FP_Logo.setObjectName("FP_Logo")

        self.retranslateUi(ForgotPassword_Fullpage)
        QtCore.QMetaObject.connectSlotsByName(ForgotPassword_Fullpage)

    def retranslateUi(self, ForgotPassword_Fullpage):
        _translate = QtCore.QCoreApplication.translate
        ForgotPassword_Fullpage.setWindowTitle(_translate("ForgotPassword_Fullpage", "Dialog"))
        self.FP_EmailText.setText(_translate("ForgotPassword_Fullpage", "EMAIL:"))
        self.label_5.setText(_translate("ForgotPassword_Fullpage", "Submit"))
        self.ForgotPassTEXT.setText(_translate("ForgotPassword_Fullpage", "FORGOT PASSWORD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ForgotPassword_Fullpage = QtWidgets.QDialog()
    ui = Ui_ForgotPassword_Fullpage()
    ui.setupUi(ForgotPassword_Fullpage)
    ForgotPassword_Fullpage.show()
    sys.exit(app.exec_())
