# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\chris\OneDrive\Desktop\For Python Code\penpal\Confrim NPass.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1440, 780)
        Dialog.setMinimumSize(QtCore.QSize(581, 96))
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LI_Header = QtWidgets.QFrame(Dialog)
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
        self.LI_HeaderIcon.setPixmap(QtGui.QPixmap("C:\\Users\\chris\\OneDrive\\Desktop\\For Python Code\\penpal\\../../../../Downloads/HeaderIcon.png"))
        self.LI_HeaderIcon.setScaledContents(True)
        self.LI_HeaderIcon.setObjectName("LI_HeaderIcon")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(261, 149, 901, 602))
        self.frame.setMinimumSize(QtCore.QSize(901, 602))
        self.frame.setStyleSheet("background-color: rgb(255, 240, 216);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 220, 351, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(351, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(122, 12, 12); font-size: 23px;\n"
"background: transparent;")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(100, 280, 323, 36))
        self.frame_2.setMinimumSize(QtCore.QSize(323, 36))
        self.frame_2.setStyleSheet("background-color: rgb(255, 240, 216);\n"
"border: 2px solid #E58D76;\n"
"background: transparent;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(300, 460, 119, 36))
        self.frame_3.setMinimumSize(QtCore.QSize(119, 36))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setStyleSheet("border-color: rgb(220, 97, 88);\n"
"border: 3px solid #DC6158;\n"
"border-radius: 5px;\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(28, -23, 350, 81))
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
        self.ForgotPassTEXT.setGeometry(QtCore.QRect(90, 180, 488, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.ForgotPassTEXT.sizePolicy().hasHeightForWidth())
        self.ForgotPassTEXT.setSizePolicy(sizePolicy)
        self.ForgotPassTEXT.setMinimumSize(QtCore.QSize(488, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(36)
        font.setBold(False)
        self.ForgotPassTEXT.setFont(font)
        self.ForgotPassTEXT.setStyleSheet("color: rgb(220, 97, 88); font-size: 40px; font-weight: bold;")
        self.ForgotPassTEXT.setObjectName("ForgotPassTEXT")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1031, 601))
        self.label_4.setStyleSheet("background: transparent;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:\\Users\\chris\\OneDrive\\Desktop\\For Python Code\\penpal\\../../PenpalFE/FPshadow.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(-50, 0, 245, 127))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\chris\\OneDrive\\Desktop\\For Python Code\\penpal\\../../PenpalFE/FPlogo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.FPimage1 = QtWidgets.QLabel(self.frame)
        self.FPimage1.setGeometry(QtCore.QRect(170, 0, 1131, 602))
        self.FPimage1.setMinimumSize(QtCore.QSize(421, 602))
        self.FPimage1.setStyleSheet("background: transparent;")
        self.FPimage1.setText("")
        self.FPimage1.setPixmap(QtGui.QPixmap("C:\\Users\\chris\\OneDrive\\Desktop\\For Python Code\\penpal\\../../PenpalFE/FPimage1.png"))
        self.FPimage1.setScaledContents(True)
        self.FPimage1.setObjectName("FPimage1")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 320, 351, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(351, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(122, 12, 12); font-size: 23px;\n"
"background: transparent;")
        self.label_3.setObjectName("label_3")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(100, 380, 323, 36))
        self.frame_4.setMinimumSize(QtCore.QSize(323, 36))
        self.frame_4.setStyleSheet("background-color: rgb(255, 240, 216);\n"
"border: 2px solid #E58D76;\n"
"background: transparent;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "ENTER YOUR NEW PASSWORD:"))
        self.label_5.setText(_translate("Dialog", "SUBMIT"))
        self.ForgotPassTEXT.setText(_translate("Dialog", "FORGOT PASSWORD"))
        self.label_3.setText(_translate("Dialog", "CONFIRM YOUR NEW PASSWORD:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
