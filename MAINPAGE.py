# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\chris\OneDrive\Desktop\For Python Code\penpal\MAINPAGE.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1440, 1307)
        Dialog.setMinimumSize(QtCore.QSize(0, 20))
        Dialog.setMaximumSize(QtCore.QSize(16777193, 16777215))
        Dialog.setSizeIncrement(QtCore.QSize(0, 24))
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
        self.label = QtWidgets.QLabel(self.LI_Header)
        self.label.setGeometry(QtCore.QRect(-50, -10, 182, 121))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setSizeIncrement(QtCore.QSize(4, 0))
        self.label.setStyleSheet("Background: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\chris\\OneDrive\\Desktop\\For Python Code\\penpal\\../../../../Downloads/GPfp.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.ForgotPassTEXT = QtWidgets.QLabel(self.LI_Header)
        self.ForgotPassTEXT.setGeometry(QtCore.QRect(90, 30, 488, 41))
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
        self.ForgotPassTEXT.setStyleSheet("background: transparent; /* Ensures no background color */\n"
"color: rgb(255, 255, 255); /* White text */\n"
"text-shadow: 2px 2px 5px #821B1A; /* Dark red shadow *")
        self.ForgotPassTEXT.setObjectName("ForgotPassTEXT")
        self.pushButton = QtWidgets.QPushButton(self.LI_Header)
        self.pushButton.setGeometry(QtCore.QRect(930, 30, 150, 45))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 700 14pt \"Times New Roman\";\n"
"border-color: rgb(229, 141, 118);\n"
"border: 3px solid #FFFFFF;\n"
"border-radius: 20px;\n"
"background: transparent;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.LI_Header)
        self.pushButton_2.setGeometry(QtCore.QRect(1090, 30, 150, 45))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 700 14pt \"Times New Roman\";\n"
"border-color: rgb(229, 141, 118);\n"
"border: 3px solid #FFFFFF;\n"
"border-radius: 20px;\n"
"background: transparent;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.LI_Header)
        self.pushButton_3.setGeometry(QtCore.QRect(1250, 30, 150, 45))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 700 14pt \"Times New Roman\";\n"
"border-color: rgb(229, 141, 118);\n"
"border: 3px solid #FFFFFF;\n"
"border-radius: 20px;\n"
"background: transparent;\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(830, 630, 179, 436))
        self.frame_2.setStyleSheet("background-color: rgb(255, 240, 216);\n"
"border-radius: 5px;\n"
"border: 3px solid #BE7928;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(720, 590, 254, 518))
        self.frame_3.setStyleSheet("background-color: rgb(255, 240, 216);\n"
"border-radius: 5px;\n"
"border: 3px solid #BE7928;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setGeometry(QtCore.QRect(450, 510, 489, 699))
        self.frame_4.setStyleSheet("background-color: rgb(255, 240, 216);\n"
"border-radius: 5px;\n"
"border: 3px solid #BE7928;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(160, 20, 171, 101))
        self.label_4.setStyleSheet("border: none;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:\\Users\\chris\\OneDrive\\Desktop\\For Python Code\\penpal\\../../PenpalFE/GPfp.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.ForgotPassTEXT_2 = QtWidgets.QLabel(self.frame_4)
        self.ForgotPassTEXT_2.setGeometry(QtCore.QRect(190, 110, 488, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.ForgotPassTEXT_2.sizePolicy().hasHeightForWidth())
        self.ForgotPassTEXT_2.setSizePolicy(sizePolicy)
        self.ForgotPassTEXT_2.setMinimumSize(QtCore.QSize(488, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        self.ForgotPassTEXT_2.setFont(font)
        self.ForgotPassTEXT_2.setStyleSheet("font-size: 36px;\n"
"text-align: center;\n"
"background: transparent;\n"
"color: #BE7928;\n"
"text-align: left;\n"
"border: none;")
        self.ForgotPassTEXT_2.setObjectName("ForgotPassTEXT_2")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(50, 180, 351, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(351, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(122, 12, 12);\n"
"border: none;\n"
"font: 700 16pt \"Rockwell\";\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(50, 250, 351, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(351, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(122, 12, 12); font-size: 32px;\n"
"border: none;\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setGeometry(QtCore.QRect(50, 320, 351, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(351, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(122, 12, 12); font-size: 32px;\n"
"border: none;\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(50, 390, 351, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(351, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(122, 12, 12); font-size: 32px;\n"
"border: none;\n"
"")
        self.label_14.setObjectName("label_14")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(190, 340, 1011, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(351, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(-1)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(190, 121, 40); font-size: 36px;\n"
"background: transparent;\n"
"\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(330, 170, 381, 211))
        self.label_6.setStyleSheet("background: transparent;")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("C:\\Users\\chris\\OneDrive\\Desktop\\For Python Code\\penpal\\../../PenpalFE/FPWEL.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(630, 173, 381, 211))
        self.label_3.setStyleSheet("background: transparent;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:\\Users\\chris\\OneDrive\\Desktop\\For Python Code\\penpal\\../../PenpalFE/FPWEL (2).png"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 420, 1545, 892))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\chris\\OneDrive\\Desktop\\For Python Code\\penpal\\../../PenpalFE/FPgroup.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.LI_Header.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_3.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ForgotPassTEXT.setText(_translate("Dialog", "USERNAME"))
        self.pushButton.setText(_translate("Dialog", "PROFILE"))
        self.pushButton_2.setText(_translate("Dialog", "MENU"))
        self.pushButton_3.setText(_translate("Dialog", "LOG OUT"))
        self.ForgotPassTEXT_2.setText(_translate("Dialog", "Username"))
        self.label_7.setText(_translate("Dialog", "Age:"))
        self.label_8.setText(_translate("Dialog", "GENDER:"))
        self.label_9.setText(_translate("Dialog", "LOCATION:"))
        self.label_14.setText(_translate("Dialog", "PREFERENCES:"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">EXPLORE AND CONNECT WITH PEOPLE WHO SHARE YOUR INTERESTS. SWIPE RIGHT </p><p align=\"center\">TO CONNECT, LEFT TO PASS. HAPPY CONNECTING WITH LIKE-MINDED INDIVIDUALS!</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
