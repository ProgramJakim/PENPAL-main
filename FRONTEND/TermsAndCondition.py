# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PENPAL\TermsAndCondition.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

# Get the absolute path of the current directory (LogInPage.py)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Build the general path to the resources/images folder
images_folder = os.path.join(current_directory, '..', 'resources' , 'images')




class Ui_TermsAndCondition(object):
    def setupUi(self, TermsAndCondition, username="", password="", age="", gender="", location="", social_media_link="", gmail=""):
        TermsAndCondition.setObjectName("TermsAndCondition")
        TermsAndCondition.resize(1440, 780)
        TermsAndCondition.setStyleSheet("background-color: rgb(255, 249, 240);")
        
        self.username = username
        self.password = password
        self.age = age
        self.gender = gender
        self.location = location
        self.social_media_link = social_media_link
        self.gmail = gmail
        
#Header
        self.TAC_Header = QtWidgets.QFrame(TermsAndCondition)
        self.TAC_Header.setGeometry(QtCore.QRect(0, 0, 1440, 103))
        self.TAC_Header.setStyleSheet("background: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, y1:0, x2:1, y2:0, \n"
"    stop:0 #EDC27E, \n"
"    stop:0.526 #EDC27E, \n"
"    stop:1 #DC586D\n"
");\n"
"\n"
"")
        self.TAC_Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TAC_Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TAC_Header.setObjectName("TAC_Header")
        
#Header Icon
        self.TAC_HeaderIcon = QtWidgets.QLabel(self.TAC_Header)
        self.TAC_HeaderIcon.setGeometry(QtCore.QRect(-60, -20, 274, 146))
        self.TAC_HeaderIcon.setStyleSheet("background: transparent;")
        self.TAC_HeaderIcon.setText("")
        self.TAC_HeaderIcon.setPixmap(QtGui.QPixmap(os.path.join(images_folder, 'HeaderIcon.png')))
        self.TAC_HeaderIcon.setScaledContents(True)
        self.TAC_HeaderIcon.setObjectName("TAC_HeaderIcon")
        
#Side Image
        self.TAC_SideImage = QtWidgets.QLabel(TermsAndCondition)
        self.TAC_SideImage.setGeometry(QtCore.QRect(960, 330, 481, 371))
        self.TAC_SideImage.setStyleSheet("background: transparent;")
        self.TAC_SideImage.setText("")
        self.TAC_SideImage.setPixmap(QtGui.QPixmap(os.path.join(images_folder, "SideImage.png")))
        self.TAC_SideImage.setScaledContents(True)
        self.TAC_SideImage.setObjectName("TAC_SideImage")
        
#Terms And Condition Label
        self.TAC_TermandConditionLBL = QtWidgets.QLabel(TermsAndCondition)
        self.TAC_TermandConditionLBL.setGeometry(QtCore.QRect(430, 170, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.TAC_TermandConditionLBL.setFont(font)
        self.TAC_TermandConditionLBL.setStyleSheet("color: rgb(122, 12, 12);\n"
"background: transparent;")
        self.TAC_TermandConditionLBL.setObjectName("TAC_TermandConditionLBL")
        
#Terms And Condition Statement Text Edit
        self.TAC_TermsSatmentTE = QtWidgets.QTextEdit(TermsAndCondition)
        self.TAC_TermsSatmentTE.setGeometry(QtCore.QRect(190, 210, 761, 498))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TAC_TermsSatmentTE.setFont(font)
        self.TAC_TermsSatmentTE.setStyleSheet("border: 3px solid #DD5B6E;\n"
"border-radius: 5px;\n"
"background-color: #FFBCAD;")
        self.TAC_TermsSatmentTE.setObjectName("TAC_TermsSatmentTE")
        
#Terms And Condition Header
        self.TAC_TermsHeader = QtWidgets.QFrame(TermsAndCondition)
        self.TAC_TermsHeader.setGeometry(QtCore.QRect(190, 160, 761, 51))
        self.TAC_TermsHeader.setStyleSheet("border: 3px solid #DD5B6E;\n"
"border-radius: 5px;\n"
"background-color: #FFECDA;\n"
"")
        self.TAC_TermsHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TAC_TermsHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TAC_TermsHeader.setObjectName("TAC_TermsHeader")
        
#Continue Push Button
        self.TAC_ContinuePB = QtWidgets.QPushButton(TermsAndCondition)
        self.TAC_ContinuePB.setGeometry(QtCore.QRect(790, 720, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.TAC_ContinuePB.setFont(font)
        self.TAC_ContinuePB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TAC_ContinuePB.setStyleSheet("border-color: rgb(229, 141, 118);\n"
"border: 3px solid #E58D76;\n"
"border-radius: 10px;\n"
"text-decoration: underline;\n"
"color: #E58D76;\n"
"background: transparent;\n"
"")
        self.TAC_ContinuePB.setObjectName("TAC_ContinuePB")
        self.TAC_TermsHeader.raise_()
        self.TAC_Header.raise_()
        self.TAC_SideImage.raise_()
        self.TAC_TermandConditionLBL.raise_()
        self.TAC_TermsSatmentTE.raise_()
        self.TAC_ContinuePB.raise_()

        self.retranslateUi(TermsAndCondition)
        QtCore.QMetaObject.connectSlotsByName(TermsAndCondition)

    

    def retranslateUi(self, TermsAndCondition):
        _translate = QtCore.QCoreApplication.translate
        TermsAndCondition.setWindowTitle(_translate("TermsAndCondition", "TermsAndCondition"))
        self.TAC_TermandConditionLBL.setText(_translate("TermsAndCondition", "Terms and Conditions"))
        self.TAC_TermsSatmentTE.setHtml(_translate("TermsAndCondition", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">By using our services, you agree to comply with and be bound by the following </span><span style=\" font-weight:600; color:#000000;\">Terms of Service</span><span style=\" color:#000000;\">. Please read them carefully.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">1. Acceptance of Terms</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">    By accessing or using Penpal, you acknowledge that you have read, understood, and agree to these Terms of Service. If you do not agree, you must not use the platform.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">2. Eligibility</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">    You must be at least 18 years old to use Penpal. If you are under the age of majority in your jurisdiction, you may only use Penpal with the permission of a parent or legal guardian.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">3. User Accounts</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">    </span><span style=\" font-weight:600; color:#000000;\">3.1. Account Creation:</span><span style=\" color:#000000;\"> To use certain features, you must create an account. You are responsible for keeping your login details secure.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">    3.2. Accuracy of Information:</span><span style=\" color:#000000;\"> You agree to provide accurate and truthful information during registration and update it as necessary.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">    </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">    3.3. Account Security:</span><span style=\" color:#000000;\"> You are responsible for any activity that occurs under your account. Notify us immediately if you suspect unauthorized access.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">4. Use of the Service</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">    You agree to use Penpal in a manner that is lawful and respectful to other users. Prohibited activities include:</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">    1.</span><span style=\" color:#000000;\"> Impersonating another person or entity.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">    2.</span><span style=\" color:#000000;\"> Harassing, threatening, or discriminating against others.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">    3.</span><span style=\" color:#000000;\"> Sharing inappropriate or harmful content.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">    4.</span><span style=\" color:#000000;\"> Using the platform for commercial or promotional purposes without authorization.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">5. Friend Recommendations</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">    Penpal suggests friends based on shared interests, social circles, and other factors. These suggestions are not endorsements, and we encourage users to interact responsibly.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">6. Privacy</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">    Your privacy is important to us. By using Penpal, you agree to our Privacy Policy, which explains how we collect, use, and protect your data.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">7. Content Ownership</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">    7.1.User Content:</span><span style=\" color:#000000;\"> You retain ownership of the content you share on Penpal but grant us a non-exclusive, royalty-free license to use, display, and distribute it as necessary to operate the service.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">    7.2. Prohibited Content: </span><span style=\" color:#000000;\">Do not post content that violates laws, infringes copyrights, or is otherwise inappropriate.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">8. Termination</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">    We reserve the right to suspend or terminate your account at our discretion if you violate these terms or engage in harmful behavior.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">9. Limitation of Liability</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">    Penpal is provided &quot;as is.&quot; We are not responsible for any damages, loss, or harm resulting from your use of the platform. Use Penpal at your own risk.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">10. Changes to Terms</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">    We may update these Terms of Service from time to time. Significant changes will be communicated through the platform. Continued use after changes signifies your acceptance.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000;\">11. Contact Us</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">    For questions or concerns about these Terms of Service, contact us at support@penpal.com.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">By creating an account or using Penpal, you acknowledge that you have read, understood, and agree to these Terms of Service. Thank you for being a part of our community!</span></p></body></html>"))
        self.TAC_ContinuePB.setText(_translate("TermsAndCondition", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TermsAndCondition = QtWidgets.QDialog()
    ui = Ui_TermsAndCondition()
    ui.setupUi(TermsAndCondition)
    TermsAndCondition.show()
    sys.exit(app.exec_())
