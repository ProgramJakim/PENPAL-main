#annie
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, QGraphicsOpacityEffect
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, QTimer
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'FRONTEND')))
from SignUpPage import Ui_SignUp
from LogInPage import Ui_LogIn
from ForgotPass import Ui_ForgotPassword_Fullpage
from HomePage import Ui_Homepage
from WelcomePage import Ui_WelcomePage
from InterestPage import Ui_Dialog as Ui_InterestPage
from MAINPAGE import Ui_Main_Page
from AccountSettings import Ui_AccountSettings
<<<<<<< HEAD
from ContactUsPage import Ui_Dialog as Ui_ContactUsPage
from PrivacyPolicy import Ui_PrivacyPolicy
from TermsAndCondition import Ui_Dialog as Ui_TermsAndCondition
=======
from AboutUsPage import Ui_AboutUs
from ContactUpage import Ui_Dialog as Ui_ContactUsPage
from PrivacyPolicy import Ui_PrivacyPolicy
from TermsAndCondition import Ui_Dialog as Ui_TermsAndCondition

>>>>>>> origin/annie


class SplashScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 600)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        layout = QVBoxLayout(self)

        # Add a spacer item to push the content upward
        spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        # Add logo
        self.logo_label = QLabel(self)
        logo_path = os.path.join(os.path.dirname(__file__), 'resources', 'images', 'Icon.png')
        if os.path.exists(logo_path):
            self.logo_label.setPixmap(QPixmap(logo_path).scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(self.logo_label, alignment=Qt.AlignCenter)

        # Add system name
        self.label = QLabel("Penpal:\nA Social Media\n Friend Recommendation System", self)
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: white;")  # Set text color to white
        layout.addWidget(self.label)

        # Add a spacer item to push the content upward
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        # Create opacity effect
        self.opacity_effect = QGraphicsOpacityEffect()
        self.label.setGraphicsEffect(self.opacity_effect)

        # Create animation
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

        QTimer.singleShot(4000, self.close_splash)

    def close_splash(self):
        self.accept()

class MainApp:
    def __init__(self):
        # Create the application instance
        self.app = QApplication(sys.argv)

        # Create instances for all windows
        self.logInWindow = QMainWindow()
        self.signUpWindow = QMainWindow()
        self.homePageWindow = QWidget()
        self.interestPageWindow = QDialog()
        self.mainPageWindow = QDialog()
        self.accountSettingsWindow = QDialog()
        self.welcomePageWindow = QWidget()
        self.aboutUsWindow = QWidget()
        self.contactUsWindow = QDialog()
        self.privacyPolicyWindow = QDialog()
        self.termsConditionsWindow = QDialog()
<<<<<<< HEAD

        # Setup UI for all windows
        self.setup_ui()

<<<<<<< HEAD
        # Connect buttons to their respective methods
        self.connect_buttons()

=======

=======
        self.forgotPasswordWindow = QWidget()
>>>>>>> origin/annie

        # Setup UI for all windows
        self.setup_ui()

        # Connect buttons to their respective methods
        self.connect_buttons()


>>>>>>> origin/annie
    def setup_ui(self):
        # Setup UI for the WelcomePage window
        self.welcomePageUI = Ui_WelcomePage()
        self.welcomePageUI.setupUi(self.welcomePageWindow)

        # Setup UI for the login window
        self.logInUI = Ui_LogIn()
        self.logInUI.setupUi(self.logInWindow)

<<<<<<< HEAD
=======
        # Setup UI for the WelcomePage window
        self.forgotPassUi = Ui_ForgotPassword_Fullpage()
        self.forgotPassUi.setupUi(self.forgotPasswordWindow)


>>>>>>> origin/annie
        # Setup UI for the signup window
        self.signUpUI = Ui_SignUp()
        self.signUpUI.setupUi(self.signUpWindow)

        # Setup UI for the homepage window
        self.homePageUI = Ui_Homepage()
        self.homePageUI.setupUi(self.homePageWindow)

        # Setup UI for the interest page window
        self.interestPageUI = Ui_InterestPage()
        self.interestPageUI.setupUi(self.interestPageWindow)

        # Setup UI for the main page window
        self.mainPageUI = Ui_Main_Page()
        self.mainPageUI.setupUi(self.mainPageWindow)

        # Setup UI for the account settings window
        self.accountSettingsUI = Ui_AccountSettings()
        self.accountSettingsUI.setupUi(self.accountSettingsWindow)

      

<<<<<<< HEAD
=======
        # Setup UI for the AboutUS window
        self.aboutUsUI = Ui_AboutUs()
        self.aboutUsUI.setupUi(self.aboutUsWindow)

        # Setup UI for the Contact U Window
        self.contactUsUi =  Ui_ContactUsPage()
        self.contactUsUi.setupUi( self.contactUsWindow)

        # Setup Ui for the privacyPolicy
        self.privacyPolicyUI = Ui_PrivacyPolicy()
        self.privacyPolicyUI.setupUi(self.privacyPolicyWindow)

        # Setup Ui for termsConditionsWindow 
        self.termsConditionsUI = Ui_TermsAndCondition()
        self.termsConditionsUI.setupUi(self.termsConditionsWindow)

<<<<<<< HEAD



>>>>>>> origin/annie
=======
>>>>>>> origin/annie
    def connect_buttons(self):
        # WelcomePage buttons
        self.welcomePageUI.press_to_continue.clicked.connect(self.open_homepagefromwelcome)

        # LogInPage buttons
        self.logInUI.LI_SignUpPB.clicked.connect(self.openSignUpPage)
        self.logInUI.LI_LogInPB.clicked.connect(self.openInterestPage)
<<<<<<< HEAD
=======
        self.logInUI.LIbackButton.clicked.connect(self.openHomePageFromLogin)
<<<<<<< HEAD
>>>>>>> origin/annie
=======
        self.logInUI.LI_ForgotPasswordLBL.mousePressEvent = self.handleForgotPasswordClick
        
>>>>>>> origin/annie

        # SignUpPage buttons
        self.signUpUI.SU_LogInPB.clicked.connect(self.backtoLogInPage)

        # HomePage buttons
        self.homePageUI.LogIn_2.clicked.connect(self.openLogInPageFromHomepage)
        self.homePageUI.SignUp.clicked.connect(self.openSignupFromHomepage)
<<<<<<< HEAD

=======
        self.homePageUI.AboutUs.clicked.connect(self.openAboutUsPage)
>>>>>>> origin/annie
        # Connect the footer buttons to their respective pages
        self.homePageUI.about_us_button.clicked.connect(self.open_about_us_page)
        self.homePageUI.contact_us_button.clicked.connect(self.open_contact_us_page)
        self.homePageUI.privacy_policy_button.clicked.connect(self.open_privacy_policy_page)
        self.homePageUI.terms_conditions_button.clicked.connect(self.open_terms_conditions_page)

<<<<<<< HEAD
=======
        # About Us Buttons
        self.aboutUsUI.AUbackButton.clicked.connect(self.openHomePageFromAboutUs)

>>>>>>> origin/annie
        # InterestPage buttons
        self.interestPageUI.INTpushButton.clicked.connect(self.openMainPage)
        self.interestPageUI.INTpushButton.clicked.connect(self.on_continue_clicked)

        # MainPage buttons
        self.mainPageUI.MP_ProfilePB.clicked.connect(self.openAccountSettings)
        self.mainPageUI.MP_ProfilePB.clicked.connect(self.on_profile_button_click)

<<<<<<< HEAD
<<<<<<< HEAD
    def open_about_us_page(self):
        from AboutUsPage import Ui_Homepage as Ui_AboutUsPage
        self.aboutUsWindow = QDialog()
        self.ui = Ui_AboutUsPage()
        self.ui.setupUi(self.aboutUsWindow)
        self.aboutUsWindow.exec_()

    def open_contact_us_page(self):
        from ContactUpage import Ui_Dialog as Ui_ContactUsPage
        self.contactUsWindow = QDialog()
        self.ui = Ui_ContactUsPage()
        self.ui.setupUi(self.contactUsWindow)
        self.contactUsWindow.exec_()

    def open_privacy_policy_page(self):
        from PrivacyPolicy import Ui_PrivacyPolicy
        self.privacyPolicyWindow = QDialog()
        self.ui = Ui_PrivacyPolicy()
        self.ui.setupUi(self.privacyPolicyWindow)
        self.privacyPolicyWindow.exec_()

    def open_terms_conditions_page(self):
        from TermsAndCondition import Ui_Dialog as Ui_TermsAndCondition
        self.termsConditionsWindow = QDialog()
        self.ui = Ui_TermsAndCondition()
        self.ui.setupUi(self.termsConditionsWindow)
        self.termsConditionsWindow.exec_()

    def on_profile_button_click(self):
        self.mainPageWindow.close()
        self.accountSettingsWindow.show()

    def on_continue_clicked(self):
        self.interestPageWindow.close()
        self.mainPageWindow.show()

=======
=======
        # AccountSettingsButtons
        self.accountSettingsUI.AS_HomePB.clicked.connect(self.openMAINPAGEfromAccountSettings)

>>>>>>> origin/annie
    # WelcomePage methods
>>>>>>> origin/annie
    def open_homepagefromwelcome(self):
        self.welcomePageWindow.close()
        self.homePageWindow.show()

<<<<<<< HEAD
=======
    # HomePage methods
    def open_about_us_page(self):
        self.homePageWindow.close()
        self.aboutUsWindow.show()

    def open_contact_us_page(self):
        self.homePageWindow.close()
        self.contactUsWindow.show()

    def open_privacy_policy_page(self):
        self.homePageWindow.close()
        self.privacyPolicyWindow.show()

    def open_terms_conditions_page(self):
        self.homePageWindow.close()
        self.termsConditionsWindow.show()

>>>>>>> origin/annie
    def openSignupFromHomepage(self):
        self.homePageWindow.close()
        self.signUpWindow.show()

    def openLogInPageFromHomepage(self):
        self.homePageWindow.close()
        self.logInWindow.show()

<<<<<<< HEAD
=======
    # AboutUsPage methods
    def openAboutUsPage(self):
        self.homePageWindow.close()
        self.aboutUsWindow.show()

    def openHomePageFromAboutUs(self):
        self.aboutUsWindow.close()
        self.homePageWindow.show()


    # LogInPage methods
    def openHomePageFromLogin(self):
        self.logInWindow.close()
        self.homePageWindow.show()

>>>>>>> origin/annie
    def openSignUpPage(self):
        self.logInWindow.close()
        self.signUpWindow.show()

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
    def handleForgotPasswordClick(self, event):
        self.openForgotPassPageFromLogin()

    def openForgotPassPageFromLogin(self):
        self.logInWindow.close()
        self.forgotPasswordWindow.show()

>>>>>>> origin/annie
    # SignUpPage methods
>>>>>>> origin/annie
    def backtoLogInPage(self):
        self.signUpWindow.close()
        self.logInWindow.show()

<<<<<<< HEAD
=======
    # InterestPage methods
>>>>>>> origin/annie
    def openInterestPage(self):
        self.logInWindow.close()
        self.interestPageWindow.show()

<<<<<<< HEAD
    def openMainPage(self):
        self.interestPageWindow.close()
        self.mainPageWindow.show()

=======
    def on_continue_clicked(self):
        self.interestPageWindow.close()
        self.mainPageWindow.show()

    # MainPage methods
    def openMainPage(self):
        self.interestPageWindow.close()
        self.mainPageWindow.show()

    def on_profile_button_click(self):
        self.mainPageWindow.close()
        self.accountSettingsWindow.show()

<<<<<<< HEAD
    # AccountSettings methods
>>>>>>> origin/annie
=======
>>>>>>> origin/annie
    def openAccountSettings(self):
        self.mainPageWindow.close()
        self.accountSettingsWindow.show()

<<<<<<< HEAD
=======
    # AccountSettings methods
    def openMAINPAGEfromAccountSettings(self):
        self.accountSettingsWindow.close()
        self.mainPageWindow.show()


>>>>>>> origin/annie
    def run(self):
        # Show the splash screen
        splash = SplashScreen()
        if splash.exec_() == QDialog.Accepted:
            # Show the welcome page after the splash screen
            self.welcomePageWindow.show()
            sys.exit(self.app.exec_())

# Run the application
if __name__ == "__main__":
    mainApp = MainApp()
<<<<<<< HEAD
    mainApp.run()
=======
    mainApp.run()



>>>>>>> origin/annie
