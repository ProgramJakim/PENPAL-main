# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\chris\OneDrive\Desktop\For Python Code\penpal\FB-RV.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import os
from PyQt5 import QtCore, QtGui, QtWidgets

# Get the absolute path of the current directory (LogInPage.py)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Build the general path to the resources/images folder
images_folder = os.path.join(current_directory, '..', 'resources', 'images')
FB_RV_assets_folder = os.path.join(current_directory, '..', 'resources', 'images', 'FB_RV_assets')


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1440, 1193)
        Dialog.setStyleSheet("\n"
"background-color: rgb(255, 249, 240);")
        self.HP_Header = QtWidgets.QFrame(Dialog)
        self.HP_Header.setGeometry(QtCore.QRect(0, 0, 1440, 105))
        self.HP_Header.setStyleSheet("background: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, y1:0, x2:1, y2:0, \n"
"    stop:0 #EDC27E, \n"
"    stop:0.526 #EDC27E, \n"
"    stop:1 #DC586D\n"
");\n"
"\n"
"")
        self.HP_Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HP_Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HP_Header.setObjectName("HP_Header")
        self.LI_HeaderIcon = QtWidgets.QLabel(self.HP_Header)
        self.LI_HeaderIcon.setGeometry(QtCore.QRect(-70, -20, 274, 146))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(28)
        self.LI_HeaderIcon.setFont(font)
        self.LI_HeaderIcon.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;")
        self.LI_HeaderIcon.setText("")
        self.LI_HeaderIcon.setPixmap(QtGui.QPixmap(os.path.join(FB_RV_assets_folder, 'HeaderIcon.png')))
        self.LI_HeaderIcon.setScaledContents(True)
        self.LI_HeaderIcon.setObjectName("LI_HeaderIcon")
        self.HP_footer = QtWidgets.QFrame(Dialog)
        self.HP_footer.setGeometry(QtCore.QRect(-40, 840, 1481, 361))
        self.HP_footer.setStyleSheet(" border: 2px solid brown;\n"
"    border-radius: 5px;  \n"
"background-color: rgb(255, 236, 218);")
        self.HP_footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HP_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HP_footer.setObjectName("HP_footer")
        self.HP_Icon = QtWidgets.QLabel(self.HP_footer)
        self.HP_Icon.setGeometry(QtCore.QRect(0, -30, 451, 301))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(28)
        self.HP_Icon.setFont(font)
        self.HP_Icon.setStyleSheet("background: transparent;\n"
"border: clear;")
        self.HP_Icon.setText("")
        self.HP_Icon.setPixmap(QtGui.QPixmap(os.path.join(images_folder, 'Icon.png')))
        self.HP_Icon.setScaledContents(True)
        self.HP_Icon.setObjectName("HP_Icon")
        self.LI_Icon = QtWidgets.QLabel(self.HP_footer)
        self.LI_Icon.setGeometry(QtCore.QRect(-60, -20, 541, 311))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(28)
        self.LI_Icon.setFont(font)
        self.LI_Icon.setStyleSheet("border: 1px solid transparent;\n"
"background: transparent;")
        self.LI_Icon.setText("")
        self.LI_Icon.setPixmap(QtGui.QPixmap(os.path.join(FB_RV_assets_folder, 'Icon.png')))
        self.LI_Icon.setScaledContents(True)
        self.LI_Icon.setObjectName("LI_Icon")
        self.HPshape1_12 = QtWidgets.QFrame(self.HP_footer)
        self.HPshape1_12.setGeometry(QtCore.QRect(850, 30, 3, 231))
        self.HPshape1_12.setStyleSheet("\n"
"\n"
"background-color: rgba(130, 27, 26, 0.5);")
        self.HPshape1_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HPshape1_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HPshape1_12.setLineWidth(0)
        self.HPshape1_12.setObjectName("HPshape1_12")
        self.HPshape1_15 = QtWidgets.QFrame(self.HPshape1_12)
        self.HPshape1_15.setGeometry(QtCore.QRect(500, 180, 501, 371))
        self.HPshape1_15.setStyleSheet("\n"
"background-color: rgba(220, 88, 109, 178);")
        self.HPshape1_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HPshape1_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HPshape1_15.setObjectName("HPshape1_15")
        self.HPshape1_16 = QtWidgets.QFrame(self.HPshape1_15)
        self.HPshape1_16.setGeometry(QtCore.QRect(40, 140, 431, 197))
        self.HPshape1_16.setStyleSheet("\n"
"\n"
"background-color: #FFE7D5;")
        self.HPshape1_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HPshape1_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HPshape1_16.setObjectName("HPshape1_16")
        self.HPshape1_17 = QtWidgets.QFrame(self.HPshape1_15)
        self.HPshape1_17.setGeometry(QtCore.QRect(160, 10, 311, 53))
        self.HPshape1_17.setStyleSheet("background-color: #FFE7D5;")
        self.HPshape1_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HPshape1_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HPshape1_17.setObjectName("HPshape1_17")
        self.GPfp_7 = QtWidgets.QLabel(self.HPshape1_15)
        self.GPfp_7.setGeometry(QtCore.QRect(-40, -10, 261, 161))
        self.GPfp_7.setStyleSheet("background: transparent;")
        self.GPfp_7.setText("")
        self.GPfp_7.setPixmap(QtGui.QPixmap(os.path.join(FB_RV_assets_folder, 'GPfp_7.png')))
        self.GPfp_7.setScaledContents(True)
        self.GPfp_7.setObjectName("GPfp_7")
        self.HPelimage6_6 = QtWidgets.QLabel(self.HPshape1_15)
        self.HPelimage6_6.setGeometry(QtCore.QRect(170, 20, 291, 161))
        self.HPelimage6_6.setStyleSheet("background: transparent;")
        self.HPelimage6_6.setText("")
        self.HPelimage6_6.setPixmap(QtGui.QPixmap(os.path.join(FB_RV_assets_folder, 'HPelimage6.png')))
        self.HPelimage6_6.setScaledContents(True)
        self.HPelimage6_6.setObjectName("HPelimage6_6")
        self.HPtext5 = QtWidgets.QLabel(self.HP_footer)
        self.HPtext5.setGeometry(QtCore.QRect(40, 210, 291, 221))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.HPtext5.setFont(font)
        self.HPtext5.setStyleSheet("font-size: 20px;\n"
"text-align: center;\n"
"background: transparent;\n"
"color: #7A0C0C;\n"
"border: none;")
        self.HPtext5.setScaledContents(False)
        self.HPtext5.setAlignment(QtCore.Qt.AlignCenter)
        self.HPtext5.setWordWrap(True)
        self.HPtext5.setObjectName("HPtext5")
        self.HPtext3 = QtWidgets.QLabel(self.HP_footer)
        self.HPtext3.setGeometry(QtCore.QRect(640, 30, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.HPtext3.setFont(font)
        self.HPtext3.setStyleSheet("font-size: 30px;\n"
"text-align: center;\n"
"background: transparent;\n"
"color: #7A0C0C;\n"
"border: none")
        self.HPtext3.setScaledContents(False)
        self.HPtext3.setAlignment(QtCore.Qt.AlignCenter)
        self.HPtext3.setWordWrap(True)
        self.HPtext3.setObjectName("HPtext3")
        self.HPtext4 = QtWidgets.QLabel(self.HP_footer)
        self.HPtext4.setGeometry(QtCore.QRect(890, 35, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.HPtext4.setFont(font)
        self.HPtext4.setStyleSheet("font-size: 30px;\n"
"text-align: center;\n"
"background: transparent;\n"
"color: #7A0C0C;\n"
"border: none")
        self.HPtext4.setScaledContents(False)
        self.HPtext4.setAlignment(QtCore.Qt.AlignCenter)
        self.HPtext4.setWordWrap(True)
        self.HPtext4.setObjectName("HPtext4")
        self.HPtext3.raise_()
        self.HPtext4.raise_()
        self.HP_Icon.raise_()
        self.LI_Icon.raise_()
        self.HPshape1_12.raise_()
        self.HPtext5.raise_()
        self.Aus = QtWidgets.QPushButton(Dialog)
        self.Aus.setGeometry(QtCore.QRect(650, 950, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Aus.setFont(font)
        self.Aus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Aus.setStyleSheet("font:30px;\n"
"color: #7A0C0C;\n"
"background: transparent;\n"
"border-radius: 5px; \n"
"\n"
"")
        self.Aus.setObjectName("Aus")
        self.ctu = QtWidgets.QPushButton(Dialog)
        self.ctu.setGeometry(QtCore.QRect(650, 1010, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ctu.setFont(font)
        self.ctu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ctu.setStyleSheet("font:30px;\n"
"color: #7A0C0C;\n"
"background: transparent;\n"
"border-radius: 5px; \n"
"\n"
"")
        self.ctu.setObjectName("ctu")
        self.trmsCon = QtWidgets.QPushButton(Dialog)
        self.trmsCon.setGeometry(QtCore.QRect(850, 950, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.trmsCon.setFont(font)
        self.trmsCon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.trmsCon.setStyleSheet("font:30px;\n"
"color: #7A0C0C;\n"
"background: transparent;\n"
"border-radius: 5px; \n"
"\n"
"")
        self.trmsCon.setObjectName("trmsCon")
        self.priPly = QtWidgets.QPushButton(Dialog)
        self.priPly.setGeometry(QtCore.QRect(850, 1010, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.priPly.setFont(font)
        self.priPly.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.priPly.setStyleSheet("font:30px;\n"
"color: #7A0C0C;\n"
"background: transparent;\n"
"border-radius: 5px; \n"
"\n"
"")
        self.priPly.setObjectName("priPly")
        self.Shape1 = QtWidgets.QLabel(Dialog)
        self.Shape1.setGeometry(QtCore.QRect(200, 240, 951, 451))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(28)
        self.Shape1.setFont(font)
        self.Shape1.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;\n"
"border: none;")
        self.Shape1.setText("")
        self.Shape1.setPixmap(QtGui.QPixmap(os.path.join(FB_RV_assets_folder, 'Shape1.png')))
        self.Shape1.setScaledContents(True)
        self.Shape1.setObjectName("Shape1")
        self.RV_FBT1 = QtWidgets.QLabel(Dialog)
        self.RV_FBT1.setGeometry(QtCore.QRect(230, 240, 451, 191))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(28)
        self.RV_FBT1.setFont(font)
        self.RV_FBT1.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;\n"
"border: none;")
        self.RV_FBT1.setText("")
        self.RV_FBT1.setPixmap(QtGui.QPixmap(os.path.join(FB_RV_assets_folder, 'RV_FBT1.png')))
        self.RV_FBT1.setScaledContents(True)
        self.RV_FBT1.setObjectName("RV_FBT1")
        self.RV_FBT2 = QtWidgets.QLabel(Dialog)
        self.RV_FBT2.setGeometry(QtCore.QRect(200, 290, 511, 331))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(28)
        self.RV_FBT2.setFont(font)
        self.RV_FBT2.setStyleSheet("color: rgb(98, 65, 66);\n"
"background: transparent;\n"
"border: none;")
        self.RV_FBT2.setText("")
        self.RV_FBT2.setPixmap(QtGui.QPixmap(os.path.join(FB_RV_assets_folder, 'RV_FBT2.png')))
        self.RV_FBT2.setScaledContents(True)
        self.RV_FBT2.setObjectName("RV_FBT2")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(710, 330, 401, 251))
        self.frame.setStyleSheet("background-color: rgb(255, 240, 216);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.SendReview = QtWidgets.QPushButton(Dialog)
        self.SendReview.setGeometry(QtCore.QRect(970, 610, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.SendReview.setFont(font)
        self.SendReview.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SendReview.setStyleSheet("font:25px;\n"
"background-color: rgb(229, 141, 118);\n"
"color: #FFFFFF;\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px; \n"
"\n"
"")
        self.SendReview.setObjectName("SendReview")
        self.Shape1.raise_()
        self.RV_FBT2.raise_()
        self.HP_Header.raise_()
        self.HP_footer.raise_()
        self.Aus.raise_()
        self.ctu.raise_()
        self.trmsCon.raise_()
        self.priPly.raise_()
        self.RV_FBT1.raise_()
        self.frame.raise_()
        self.SendReview.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.HPtext5.setText(_translate("Dialog", "All rights reserved.2025. PenPal"))
        self.HPtext3.setText(_translate("Dialog", "INFORMATION"))
        self.HPtext4.setText(_translate("Dialog", "LEGAL"))
        self.Aus.setText(_translate("Dialog", "ABOUT US"))
        self.ctu.setText(_translate("Dialog", "CONTACT US"))
        self.trmsCon.setText(_translate("Dialog", "TERMS AND CONDITION"))
        self.priPly.setText(_translate("Dialog", "PRIVACY AND POLICY"))
        self.SendReview.setText(_translate("Dialog", "SEND REVIEW"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
