# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PENPAL\PrivacyPolicy.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

# Get the absolute path of the current directory (LogInPage.py)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Build the general path to the resources/images folder
images_folder = os.path.join(current_directory, '..', 'resources' , 'images')


class Ui_PrivacyPolicy(object):
    def setupUi(self, PrivacyPolicy):
        PrivacyPolicy.setObjectName("PrivacyPolicy")
        PrivacyPolicy.resize(1440, 780)
        PrivacyPolicy.setStyleSheet("background-color: rgb(255, 249, 240);")
        
#Header
        self.PP_Header = QtWidgets.QFrame(PrivacyPolicy)
        self.PP_Header.setGeometry(QtCore.QRect(0, 0, 1440, 103))
        self.PP_Header.setStyleSheet("background: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, y1:0, x2:1, y2:0, \n"
"    stop:0 #EDC27E, \n"
"    stop:0.526 #EDC27E, \n"
"    stop:1 #DC586D\n"
");\n"
"\n"
"")
        self.PP_Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PP_Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PP_Header.setObjectName("PP_Header")
        
#Header Icon
        self.PP_HeaderIcon = QtWidgets.QLabel(self.PP_Header)
        self.PP_HeaderIcon.setGeometry(QtCore.QRect(-60, -20, 274, 146))
        self.PP_HeaderIcon.setStyleSheet("background: transparent;")
        self.PP_HeaderIcon.setText("")
        self.PP_HeaderIcon.setPixmap(QtGui.QPixmap(os.path.join(images_folder , "HeaderIcon.png")))
        self.PP_HeaderIcon.setScaledContents(True)
        self.PP_HeaderIcon.setObjectName("PP_HeaderIcon")
        
#Side Image
        self.PP_SideImage = QtWidgets.QLabel(PrivacyPolicy)
        self.PP_SideImage.setGeometry(QtCore.QRect(960, 330, 481, 371))
        self.PP_SideImage.setStyleSheet("background: transparent;")
        self.PP_SideImage.setText("")
        self.PP_SideImage.setPixmap(QtGui.QPixmap(os.path.join(images_folder , "SideImage.png")))
        self.PP_SideImage.setScaledContents(True)
        self.PP_SideImage.setObjectName("PP_SideImage")
        
#Privacy Policy Label
        self.PP_PrivacyPolicyLBL = QtWidgets.QLabel(PrivacyPolicy)
        self.PP_PrivacyPolicyLBL.setGeometry(QtCore.QRect(480, 170, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PP_PrivacyPolicyLBL.setFont(font)
        self.PP_PrivacyPolicyLBL.setStyleSheet("color: rgb(122, 12, 12);\n"
"background: transparent;")
        self.PP_PrivacyPolicyLBL.setObjectName("PP_PrivacyPolicyLBL")
        
#Privacy Statement Text Edit
        self.PP_PrivacyStatementTE = QtWidgets.QTextEdit(PrivacyPolicy)
        self.PP_PrivacyStatementTE.setGeometry(QtCore.QRect(190, 210, 761, 498))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PP_PrivacyStatementTE.setFont(font)
        self.PP_PrivacyStatementTE.setStyleSheet("border: 3px solid #DD5B6E;\n"
"border-radius: 5px;\n"
"background-color: #FFBCAD;")
        self.PP_PrivacyStatementTE.setObjectName("PP_PrivacyStatementTE")
        self.PP_PrivacyStatementTE.setReadOnly(True)  # Make the text non-editable
        
#Header 2
        self.PP_Header_2 = QtWidgets.QFrame(PrivacyPolicy)
        self.PP_Header_2.setGeometry(QtCore.QRect(190, 160, 761, 51))
        self.PP_Header_2.setStyleSheet("border: 3px solid #DD5B6E;\n"
"border-radius: 5px;\n"
"background-color: #FFECDA;\n"
"")
        self.PP_Header_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PP_Header_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PP_Header_2.setObjectName("PP_Header_2")
        
#Back Push Button
        self.PP_BackPB = QtWidgets.QPushButton(PrivacyPolicy)
        self.PP_BackPB.setGeometry(QtCore.QRect(790, 720, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.PP_BackPB.setFont(font)
        self.PP_BackPB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PP_BackPB.setStyleSheet("border-color: rgb(229, 141, 118);\n"
"border: 3px solid #E58D76;\n"
"border-radius: 10px;\n"
"text-decoration: underline;\n"
"text-color: #E58D76;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.5);\n"
"background: transparent;\n"
"")
        self.PP_BackPB.setObjectName("PP_BackPB")
        self.PP_Header_2.raise_()
        self.PP_Header.raise_()
        self.PP_SideImage.raise_()
        self.PP_PrivacyPolicyLBL.raise_()
        self.PP_PrivacyStatementTE.raise_()
        self.PP_BackPB.raise_()

        self.retranslateUi(PrivacyPolicy)
        QtCore.QMetaObject.connectSlotsByName(PrivacyPolicy)

    

    def retranslateUi(self, PrivacyPolicy):
        _translate = QtCore.QCoreApplication.translate
        PrivacyPolicy.setWindowTitle(_translate("PrivacyPolicy", "Privacy Policy"))
        self.PP_PrivacyPolicyLBL.setText(_translate("PrivacyPolicy", "Privacy Policy"))
        self.PP_PrivacyStatementTE.setHtml(_translate("PrivacyPolicy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">                                             Welcome to Penpal!</span><br />Your privacy is important to us. This<span style=\" font-weight:600;\"> Privacy Policy</span> explains how we collect, use, store, and protect your information when you use our platform. By using Penpal, you agree to the practices described below.<br /><span style=\" font-weight:600;\"><br />1. Information We Collect</span><br />    We collect the following types of information to provide and improve our services:<br />        <span style=\" font-weight:600;\">1.1. Personal Information:</span> Name, email address, date of birth, and other details you provide during account creation.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />        <span style=\" font-weight:600;\">1.2. Profile Information:</span> Interests, hobbies, profile picture, and other optional details you choose to share.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />        <span style=\" font-weight:600;\">1.3. Usage Data:</span> Information about how you interact with Penpal, including features you use, friend recommendations you explore.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /><span style=\" font-weight:600;\">        1.4. Device Information</span>: IP address, device type, operating system, and browser information.<br /><br /><span style=\" font-weight:600;\">2. How We Use Your Information</span><br />    We use the information we collect to:<br />        <span style=\" font-weight:600;\">2.1. </span>Provide and improve the Penpal platform.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />        <span style=\" font-weight:600;\">2.2.</span> Personalize friend recommendations based on shared interests, location, and mutual connections.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />         <span style=\" font-weight:600;\">2.3.</span> Ensure account security and verify user identity.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />        <span style=\" font-weight:600;\">2.4.</span> Communicate with you regarding updates, changes, or promotions.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />        <span style=\" font-weight:600;\">2.5.</span> Monitor usage and analyze trends to enhance user experience.<br /><span style=\" font-weight:600;\"><br />3. Sharing Your Information</span><br />    We do not sell or rent your personal information. We may share your information:<br />        <span style=\" font-weight:600;\">3.1.</span> With other Penpal users, as part of friend suggestions and interactions.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />        <span style=\" font-weight:600;\">3.2. </span>With service providers who help us operate Penpal, under strict confidentiality agreements.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />        <span style=\" font-weight:600;\">3.3. </span>If required by law or to protect Penpal’s legal rights and safety.<br /><br /><span style=\" font-weight:600;\">4. Data Storage and Security</span><br />    We store your data securely using industry-standard encryption and access controls. While we take strong measures to protect your information, no system is entirely foolproof. Use Penpal at your own discretion.<br /><br /><span style=\" font-weight:600;\">5. Your Choices and Controls</span><br />    <span style=\" font-weight:600;\">5.1. Access and Update:</span> You can view and update your profile and account information at any time.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />    <span style=\" font-weight:600;\">5.2. Delete Account:</span> You may delete your account, and we will remove your data from our systems, except where retention is required by law.<br />    <span style=\" font-weight:600;\">5.3. Communication Preferences:</span> Opt out of promotional emails through your account settings.<br /><span style=\" font-weight:600;\"><br />6. Cookies and Tracking Technologies</span><br />    Penpal uses cookies and similar technologies to:<br />        <span style=\" font-weight:600;\">6.1. </span>Remember your preferences and settings.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />        <span style=\" font-weight:600;\">6.2. </span>Analyze site usage and improve our platform.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />        <span style=\" font-weight:600;\">6.3. </span>Provide personalized recommendations and advertisements.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />        <span style=\" font-weight:600;\">6.4. </span>You can manage your cookie preferences through your browser settings.<br /><br /><span style=\" font-weight:600;\">7. Children’s Privacy</span><br />    Penpal is not intended for users under 13 years of age. If we become aware that we have collected data from a child under 13, we will delete it immediately.<br /><br /><span style=\" font-weight:600;\">8. International Users</span><br />    By using Penpal, you consent to the transfer and processing of your information in the country where Penpal operates, which may have different data protection laws than your country of residence.<br /><br /><span style=\" font-weight:600;\">9. Changes to Privacy Policy</span><br />    We may update this Privacy Policy from time to time. Significant changes will be communicated through the platform. Continued use of Penpal after updates constitutes your agreement to the revised policy.<br /><br /><span style=\" font-weight:600;\">10. Contact Us</span><br />    If you have questions or concerns about this Privacy Policy, please contact us at privacy@penpal.com.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />By using Penpal, you acknowledge that you have read, understood, and agree to this Privacy Policy. Thank you for trusting us with your information!</p></body></html>"))
        self.PP_BackPB.setText(_translate("PrivacyPolicy", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PrivacyPolicy = QtWidgets.QDialog()
    ui = Ui_PrivacyPolicy()
    ui.setupUi(PrivacyPolicy)
    PrivacyPolicy.show()
    sys.exit(app.exec_())
