# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\chris\OneDrive\Desktop\For Python Code\penpal\FinaInterestPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'FRONTEND')))
from HomePage import Ui_Homepage
from MAINPAGE import Ui_Main_Page

# Get the absolute path of the current directory (LogInPage.py)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Build the general path to the resources/images folder
images_folder = os.path.join(current_directory, '..', 'resources', 'images')
Interest_assets_folder = os.path.join(current_directory, '..', 'resources', 'images', 'Interest_assets')

class Ui_Interest(object):
    def setupUi(self, Interest):
        Interest.setObjectName("Interest")
        Interest.resize(1440, 850)
        Interest.setStyleSheet("background-color:#FFF9F0;")
        self.CUHeader = QtWidgets.QFrame(Interest)
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
        self.HeaderIcon.setGeometry(QtCore.QRect(-60, -20, 274, 146))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(28)
        self.HeaderIcon.setFont(font)
        self.HeaderIcon.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;")
        self.HeaderIcon.setText("")
        self.HeaderIcon.setPixmap(QtGui.QPixmap(os.path.join(images_folder, 'HeaderIcon.png')))
        self.HeaderIcon.setScaledContents(True)
        self.HeaderIcon.setObjectName("HeaderIcon")
        self.INshape1 = QtWidgets.QFrame(Interest)
        self.INshape1.setGeometry(QtCore.QRect(109, 302, 286, 80))
        self.INshape1.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape1.setObjectName("INshape1")
        self.INicon1 = QtWidgets.QLabel(self.INshape1)
        self.INicon1.setGeometry(QtCore.QRect(5, 5, 70, 70))
        self.INicon1.setStyleSheet("background: transparent;\n"
"border:none;")
        self.INicon1.setText("")
        self.INicon1.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INicon1.png')))
        self.INicon1.setScaledContents(True)
        self.INicon1.setObjectName("INicon1")
        self.INTpushButton = QtWidgets.QPushButton(Interest)
        self.INTpushButton.setGeometry(QtCore.QRect(1154, 730, 150, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.INTpushButton.setFont(font)
        self.INTpushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.INTpushButton.setStyleSheet("background:rgb(255, 187, 173);\n"
"font:20px;\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.INTpushButton.setObjectName("INTpushButton")
        self.INTEREST = QtWidgets.QLabel(Interest)
        self.INTEREST.setGeometry(QtCore.QRect(610, 90, 231, 131))
        self.INTEREST.setStyleSheet("background: transparent;")
        self.INTEREST.setText("")
        self.INTEREST.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INTEREST.png')))
        self.INTEREST.setScaledContents(True)
        self.INTEREST.setObjectName("INTEREST")
        self.INtext_2 = QtWidgets.QLabel(Interest)
        self.INtext_2.setGeometry(QtCore.QRect(1230, 30, 231, 251))
        self.INtext_2.setStyleSheet("background: transparent;")
        self.INtext_2.setText("")
        self.INtext_2.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INimage1.png')))
        self.INtext_2.setScaledContents(True)
        self.INtext_2.setObjectName("INtext_2")
        self.INtext_3 = QtWidgets.QLabel(Interest)
        self.INtext_3.setGeometry(QtCore.QRect(-170, 480, 391, 341))
        self.INtext_3.setStyleSheet("background: transparent;")
        self.INtext_3.setText("")
        self.INtext_3.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INimage.png')))
        self.INtext_3.setScaledContents(True)
        self.INtext_3.setObjectName("INtext_3")
        self.AUtext1 = QtWidgets.QLabel(Interest)
        self.AUtext1.setGeometry(QtCore.QRect(200, 170, 1061, 111))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        self.AUtext1.setFont(font)
        self.AUtext1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.AUtext1.setStyleSheet("font-size: 30px;\n"
"text-align: center;\n"
"background: transparent;\n"
"color: #BE7928;\n"
"text-align: left;")
        self.AUtext1.setScaledContents(False)
        self.AUtext1.setAlignment(QtCore.Qt.AlignCenter)
        self.AUtext1.setWordWrap(True)
        self.AUtext1.setObjectName("AUtext1")
        self.INshape2 = QtWidgets.QFrame(Interest)
        self.INshape2.setGeometry(QtCore.QRect(109, 408, 286, 80))
        self.INshape2.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape2.setObjectName("INshape2")
        self.INicon2 = QtWidgets.QLabel(self.INshape2)
        self.INicon2.setGeometry(QtCore.QRect(5, 5, 70, 70))
        self.INicon2.setStyleSheet("background: transparent;\n"
"border:none;")
        self.INicon2.setText("")
        self.INicon2.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INicon2.png')))
        self.INicon2.setScaledContents(True)
        self.INicon2.setObjectName("INicon2")
        self.INshape3 = QtWidgets.QFrame(Interest)
        self.INshape3.setGeometry(QtCore.QRect(109, 516, 286, 80))
        self.INshape3.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape3.setObjectName("INshape3")
        self.INicon3 = QtWidgets.QLabel(self.INshape3)
        self.INicon3.setGeometry(QtCore.QRect(5, 5, 70, 70))
        self.INicon3.setStyleSheet("background: transparent;\n"
"border:none;")
        self.INicon3.setText("")
        self.INicon3.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INicon3.png')))
        self.INicon3.setScaledContents(True)
        self.INicon3.setObjectName("INicon3")
        self.INshape4 = QtWidgets.QFrame(Interest)
        self.INshape4.setGeometry(QtCore.QRect(259, 627, 286, 80))
        self.INshape4.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape4.setObjectName("INshape4")
        self.INshape1_7 = QtWidgets.QFrame(self.INshape4)
        self.INshape1_7.setGeometry(QtCore.QRect(29, 820, 286, 99))
        self.INshape1_7.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape1_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape1_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape1_7.setObjectName("INshape1_7")
        self.INshape1_8 = QtWidgets.QFrame(self.INshape4)
        self.INshape1_8.setGeometry(QtCore.QRect(29, 680, 286, 99))
        self.INshape1_8.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape1_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape1_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape1_8.setObjectName("INshape1_8")
        self.INshape1_2 = QtWidgets.QFrame(self.INshape4)
        self.INshape1_2.setGeometry(QtCore.QRect(29, 400, 286, 99))
        self.INshape1_2.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape1_2.setObjectName("INshape1_2")
        self.INshape1_9 = QtWidgets.QFrame(self.INshape4)
        self.INshape1_9.setGeometry(QtCore.QRect(29, 540, 286, 99))
        self.INshape1_9.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape1_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape1_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape1_9.setObjectName("INshape1_9")
        self.INshape1_10 = QtWidgets.QFrame(self.INshape4)
        self.INshape1_10.setGeometry(QtCore.QRect(29, 950, 286, 99))
        self.INshape1_10.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape1_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape1_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape1_10.setObjectName("INshape1_10")
        self.INicon4 = QtWidgets.QLabel(self.INshape4)
        self.INicon4.setGeometry(QtCore.QRect(5, 5, 70, 70))
        self.INicon4.setStyleSheet("background: transparent;\n"
"border:none;")
        self.INicon4.setText("")
        self.INicon4.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INicon4.png')))
        self.INicon4.setScaledContents(True)
        self.INicon4.setObjectName("INicon4")
        self.INshape5 = QtWidgets.QFrame(Interest)
        self.INshape5.setGeometry(QtCore.QRect(1089, 300, 286, 80))
        self.INshape5.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape5.setObjectName("INshape5")
        self.INicon5 = QtWidgets.QLabel(self.INshape5)
        self.INicon5.setGeometry(QtCore.QRect(5, 5, 70, 70))
        self.INicon5.setStyleSheet("background: transparent;\n"
"border:none;")
        self.INicon5.setText("")
        self.INicon5.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INicon5.png')))
        self.INicon5.setScaledContents(True)
        self.INicon5.setObjectName("INicon5")
        self.INshape6 = QtWidgets.QFrame(Interest)
        self.INshape6.setGeometry(QtCore.QRect(440, 302, 286, 80))
        self.INshape6.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape6.setObjectName("INshape6")
        self.INicon6 = QtWidgets.QLabel(self.INshape6)
        self.INicon6.setGeometry(QtCore.QRect(5, 5, 70, 70))
        self.INicon6.setStyleSheet("background: transparent;\n"
"border:none;")
        self.INicon6.setText("")
        self.INicon6.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INicon6.png')))
        self.INicon6.setScaledContents(True)
        self.INicon6.setObjectName("INicon6")
        self.INshape7 = QtWidgets.QFrame(Interest)
        self.INshape7.setGeometry(QtCore.QRect(440, 408, 286, 80))
        self.INshape7.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape7.setObjectName("INshape7")
        self.INicon7 = QtWidgets.QLabel(self.INshape7)
        self.INicon7.setGeometry(QtCore.QRect(5, 5, 70, 70))
        self.INicon7.setStyleSheet("background: transparent;\n"
"border:none;")
        self.INicon7.setText("")
        self.INicon7.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INicon7.png')))
        self.INicon7.setScaledContents(True)
        self.INicon7.setObjectName("INicon7")
        self.INshape8 = QtWidgets.QFrame(Interest)
        self.INshape8.setGeometry(QtCore.QRect(440, 516, 286, 80))
        self.INshape8.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape8.setObjectName("INshape8")
        self.INicon8 = QtWidgets.QLabel(self.INshape8)
        self.INicon8.setGeometry(QtCore.QRect(5, 5, 70, 70))
        self.INicon8.setStyleSheet("background: transparent;\n"
"border:none;")
        self.INicon8.setText("")
        self.INicon8.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INicon8.png')))
        self.INicon8.setScaledContents(True)
        self.INicon8.setObjectName("INicon8")
        self.INshape9 = QtWidgets.QFrame(Interest)
        self.INshape9.setGeometry(QtCore.QRect(610, 627, 286, 80))
        self.INshape9.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape9.setObjectName("INshape9")
        self.INicon9 = QtWidgets.QLabel(self.INshape9)
        self.INicon9.setGeometry(QtCore.QRect(5, 5, 70, 70))
        self.INicon9.setStyleSheet("background: transparent;\n"
"border:none;")
        self.INicon9.setText("")
        self.INicon9.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INicon9.png')))
        self.INicon9.setScaledContents(True)
        self.INicon9.setObjectName("INicon9")
        self.INshape10 = QtWidgets.QFrame(Interest)
        self.INshape10.setGeometry(QtCore.QRect(1090, 407, 286, 80))
        self.INshape10.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape10.setObjectName("INshape10")
        self.INicon10 = QtWidgets.QLabel(self.INshape10)
        self.INicon10.setGeometry(QtCore.QRect(5, 5, 70, 70))
        self.INicon10.setStyleSheet("background: transparent;\n"
"border:none;")
        self.INicon10.setText("")
        self.INicon10.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INicon10.png')))
        self.INicon10.setScaledContents(True)
        self.INicon10.setObjectName("INicon10")
        self.INshape11 = QtWidgets.QFrame(Interest)
        self.INshape11.setGeometry(QtCore.QRect(770, 302, 286, 80))
        self.INshape11.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape11.setObjectName("INshape11")
        self.INicon11 = QtWidgets.QLabel(self.INshape11)
        self.INicon11.setGeometry(QtCore.QRect(5, 5, 70, 70))
        self.INicon11.setStyleSheet("background: transparent;\n"
"border:none;")
        self.INicon11.setText("")
        self.INicon11.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INicon11.png')))
        self.INicon11.setScaledContents(True)
        self.INicon11.setObjectName("INicon11")
        self.INshape12 = QtWidgets.QFrame(Interest)
        self.INshape12.setGeometry(QtCore.QRect(770, 408, 286, 80))
        self.INshape12.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape12.setObjectName("INshape12")
        self.INicon12 = QtWidgets.QLabel(self.INshape12)
        self.INicon12.setGeometry(QtCore.QRect(5, 5, 70, 70))
        self.INicon12.setStyleSheet("background: transparent;\n"
"border:none;")
        self.INicon12.setText("")
        self.INicon12.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INicon12.png')))
        self.INicon12.setScaledContents(True)
        self.INicon12.setObjectName("INicon12")
        self.INshape13 = QtWidgets.QFrame(Interest)
        self.INshape13.setGeometry(QtCore.QRect(770, 516, 286, 80))
        self.INshape13.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape13.setObjectName("INshape13")
        self.INicon13 = QtWidgets.QLabel(self.INshape13)
        self.INicon13.setGeometry(QtCore.QRect(5, 5, 70, 70))
        self.INicon13.setStyleSheet("background: transparent;\n"
"border:none;")
        self.INicon13.setText("")
        self.INicon13.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INicon13.png')))
        self.INicon13.setScaledContents(True)
        self.INicon13.setObjectName("INicon13")
        self.INshape14 = QtWidgets.QFrame(Interest)
        self.INshape14.setGeometry(QtCore.QRect(940, 627, 286, 80))
        self.INshape14.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape14.setObjectName("INshape14")
        self.INicon14 = QtWidgets.QLabel(self.INshape14)
        self.INicon14.setGeometry(QtCore.QRect(5, 5, 70, 70))
        self.INicon14.setStyleSheet("background: transparent;\n"
"border:none;")
        self.INicon14.setText("")
        self.INicon14.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INicon14.png')))
        self.INicon14.setScaledContents(True)
        self.INicon14.setObjectName("INicon14")
        self.INshape15 = QtWidgets.QFrame(Interest)
        self.INshape15.setGeometry(QtCore.QRect(1090, 515, 286, 80))
        self.INshape15.setStyleSheet("background: transparent;\n"
"border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;\n"
"\n"
"")
        self.INshape15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.INshape15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.INshape15.setObjectName("INshape15")
        self.INicon15 = QtWidgets.QLabel(self.INshape15)
        self.INicon15.setGeometry(QtCore.QRect(5, 5, 70, 70))
        self.INicon15.setStyleSheet("background: transparent;\n"
"border:none;")
        self.INicon15.setText("")
        self.INicon15.setPixmap(QtGui.QPixmap(os.path.join(Interest_assets_folder, 'INicon15.png')))
        self.INicon15.setScaledContents(True)
        self.INicon15.setObjectName("INicon15")
        self.pushButton_1 = QtWidgets.QPushButton(Interest)
        self.pushButton_1.setGeometry(QtCore.QRect(210, 330, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1.setStyleSheet("border: none;\n"
"font:24px;\n"
"color: #7A0C0C;\n"
"\n"
"")
        self.pushButton_1.setCheckable(True)
        self.pushButton_1.setChecked(False)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Interest)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 440, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border: none;\n"
"font:24px;\n"
"color: #7A0C0C;\n"
"")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Interest)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 545, 138, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("border: none;\n"
"font:24px;\n"
"color: #7A0C0C;\n"
"\n"
"")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Interest)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 655, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("border: none;\n"
"font:24px;\n"
"color: #7A0C0C;\n"
"\n"
"")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Interest)
        self.pushButton_5.setGeometry(QtCore.QRect(1200, 330, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("border: none;\n"
"font:24px;\n"
"color: #7A0C0C;\n"
"\n"
"")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setChecked(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Interest)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 330, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("border: none;\n"
"font:24px;\n"
"color: #7A0C0C;\n"
"\n"
"")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Interest)
        self.pushButton_7.setGeometry(QtCore.QRect(550, 440, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("border: none;\n"
"font:24px;\n"
"color: #7A0C0C;\n"
"\n"
"")
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setChecked(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Interest)
        self.pushButton_8.setGeometry(QtCore.QRect(550, 545, 140, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("border: none;\n"
"font:24px;\n"
"color: #7A0C0C;\n"
"")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setChecked(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Interest)
        self.pushButton_9.setGeometry(QtCore.QRect(710, 655, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("border: none;\n"
"font:24px;\n"
"color: #7A0C0C;\n"
"\n"
"")
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setChecked(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Interest)
        self.pushButton_10.setGeometry(QtCore.QRect(1190, 440, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("border: none;\n"
"font:24px;\n"
"color: #7A0C0C;\n"
"")
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setChecked(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Interest)
        self.pushButton_11.setGeometry(QtCore.QRect(880, 330, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("border: none;\n"
"font:24px;\n"
"color: #7A0C0C;\n"
"\n"
"")
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setChecked(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Interest)
        self.pushButton_12.setGeometry(QtCore.QRect(880, 440, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("border: none;\n"
"font:24px;\n"
"color: #7A0C0C;\n"
"")
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setChecked(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Interest)
        self.pushButton_13.setGeometry(QtCore.QRect(890, 545, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("border: none;\n"
"font:24px;\n"
"color: #7A0C0C;\n"
"\n"
"")
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setChecked(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(Interest)
        self.pushButton_14.setGeometry(QtCore.QRect(1050, 655, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet("border: none;\n"
"font:24px;\n"
"color: #7A0C0C;\n"
"\n"
"")
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setChecked(False)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(Interest)
        self.pushButton_15.setGeometry(QtCore.QRect(1190, 545, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet("border: none;\n"
"font:24px;\n"
"color: #7A0C0C;\n"
"")
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setChecked(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.Placeholder1 = QtWidgets.QFrame(Interest)
        self.Placeholder1.setGeometry(QtCore.QRect(1020, 730, 120, 30))
        self.Placeholder1.setStyleSheet("border-radius: 3px solid;\n"
"Border: 2px solid #E58D76;")
        self.Placeholder1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Placeholder1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Placeholder1.setObjectName("Placeholder1")

        self.placeholderText = QtWidgets.QLabel(self.Placeholder1)
        self.placeholderText.setGeometry(QtCore.QRect(0, 0, 120, 30))
        self.placeholderText.setStyleSheet("background: transparent;")
        self.placeholderText.setAlignment(QtCore.Qt.AlignCenter)
        self.placeholderText.setObjectName("placeholderText")
      
        self.INtext_3.raise_()
        self.INTEREST.raise_()
        self.INtext_2.raise_()
        self.AUtext1.raise_()
        self.CUHeader.raise_()
        self.INshape1.raise_()
        self.INTpushButton.raise_()
        self.INshape2.raise_()
        self.INshape3.raise_()
        self.INshape4.raise_()
        self.INshape5.raise_()
        self.INshape6.raise_()
        self.INshape7.raise_()
        self.INshape8.raise_()
        self.INshape9.raise_()
        self.INshape10.raise_()
        self.INshape11.raise_()
        self.INshape12.raise_()
        self.INshape13.raise_()
        self.INshape14.raise_()
        self.INshape15.raise_()
        self.pushButton_1.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.pushButton_14.raise_()
        self.pushButton_15.raise_()
        self.Placeholder1.raise_()

#DONE BUTTON
        self.INTpushButton = QtWidgets.QPushButton(Interest)
        self.INTpushButton.setGeometry(QtCore.QRect(1154, 730, 150, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.INTpushButton.setFont(font)
        self.INTpushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.INTpushButton.setStyleSheet("background:rgb(255, 187, 173);\n"
        "font:20px;\n"
        "color: #FFFFFF;\n"
        "\n"
        "")
        self.INTpushButton.setObjectName("INTpushButton")


        self.retranslateUi(Interest)
        QtCore.QMetaObject.connectSlotsByName(Interest)


       
        
    
    def retranslateUi(self, Interest):
        _translate = QtCore.QCoreApplication.translate
        Interest.setWindowTitle(_translate("Interest", "Interest"))
        self.INTpushButton.setText(_translate("Interest", "DONE"))
        self.AUtext1.setText(_translate("Interest", "FIND FRIENDS WHO SHARE YOUR PASSIONS, FROM SPORTS TO ARTS AND BEYOND. START YOUR JOURNEY WITH LIKE-MINDED INDIVIDUALS ON PENPAL!"))
        self.pushButton_1.setText(_translate("Interest", "SPORTS"))
        self.pushButton_2.setText(_translate("Interest", "TECHNOLOGY"))
        self.pushButton_3.setText(_translate("Interest", "GAMING"))
        self.pushButton_4.setText(_translate("Interest", "ARTS"))
        self.pushButton_5.setText(_translate("Interest", "PHOTOGRAPHY"))
        self.pushButton_6.setText(_translate("Interest", "MUSIC"))
        self.pushButton_7.setText(_translate("Interest", "TRAVEL"))
        self.pushButton_8.setText(_translate("Interest", "COOKING"))
        self.pushButton_9.setText(_translate("Interest", "FASHION"))
        self.pushButton_10.setText(_translate("Interest", "EDUCATION"))
        self.pushButton_11.setText(_translate("Interest", "MOVIES"))
        self.pushButton_12.setText(_translate("Interest", "BOOKS"))
        self.pushButton_13.setText(_translate("Interest", "LIFESTYLE"))
        self.pushButton_14.setText(_translate("Interest", "SCIENCE"))
        self.pushButton_15.setText(_translate("Interest", "BUSINESS"))
        self.placeholderText.setText(_translate("Interest", "0 Selected"))
       
       


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Interest = QtWidgets.QDialog()
    ui = Ui_Interest()
    ui.setupUi(Interest)
    Interest.show()
    sys.exit(app.exec_())
