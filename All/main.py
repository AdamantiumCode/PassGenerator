import webbrowser
import pyperclip
import secrets
import sys

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow) -> None:
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon.fromTheme("dialog-password")
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(33, 33, 33);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.NameLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.NameLabel.setGeometry(QtCore.QRect(20, 10, 761, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.NameLabel.setFont(font)
        
        self.NameLabel.setStyleSheet(
                "font: 900 35pt \"Arial Black\";\n"
                "color: rgb(120, 120, 120);\n"
                "\n"
                "background-color: rgb(66, 66, 66);\n"
                "\n"
                "border-color: rgb(97, 97, 97);\n"
                "border-width: 0px;\n"
                "border-radius: 15px;\n"
                "border-style: solid;"
        )
        
        self.NameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.NameLabel.setWordWrap(False)
        self.NameLabel.setOpenExternalLinks(False)
        self.NameLabel.setObjectName("NameLabel")
        self.ByAuthorLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.ByAuthorLabel.setEnabled(True)
        self.ByAuthorLabel.setGeometry(QtCore.QRect(180, 90, 441, 41))
        self.ByAuthorLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        
        self.ByAuthorLabel.setStyleSheet(
                "font: 900 20pt \"Arial Black\";\n"
                "color: rgb(120, 120, 120);\n"
                "\n"
                "background-color: rgb(66, 66, 66);\n"
                "\n"
                "border-color: rgb(97, 97, 97);\n"
                "border-width: 0px;\n"
                "border-radius: 15px;\n"
                "border-style: solid;"
        )
        
        self.ByAuthorLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ByAuthorLabel.setObjectName("ByAuthorLabel")
        self.GitHubButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.GitHubButton.setGeometry(QtCore.QRect(570, 510, 211, 71))
        
        self.GitHubButton.setStyleSheet(
                "font: 900 20pt \"Arial Black\";\n"
                "color: rgb(120, 120, 120);\n"
                "\n"
                "background-color: rgb(66, 66, 66);\n"
                "\n"
                "border-color: rgb(97, 97, 97);\n"
                "border-width: 0px;\n"
                "border-radius: 15px;\n"
                "border-style: solid;"
        )
        
        self.GitHubButton.setObjectName("GitHubButton")
        self.OptionsButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.OptionsButton.setGeometry(QtCore.QRect(20, 160, 301, 71))
        
        self.OptionsButton.setStyleSheet(
                "font: 900 30pt \"Arial Black\";\n"
                "color: rgb(120, 120, 120);\n"
                "\n"
                "background-color: rgb(66, 66, 66);\n"
                "\n"
                "border-color: rgb(97, 97, 97);\n"
                "border-width: 0px;\n"
                "border-radius: 15px;\n"
                "border-style: solid;"
        )
        
        self.OptionsButton.setObjectName("OptionsButton")
        self.YourPasswordLabel = QtWidgets.QPushButton(parent=self.centralwidget)
        self.YourPasswordLabel.setGeometry(QtCore.QRect(340, 160, 441, 71))
        
        self.YourPasswordLabel.setStyleSheet(
                "font: 900 30pt \"Arial Black\";\n"
                "color: rgb(120, 120, 120);\n"
                "\n"
                "background-color: rgb(66, 66, 66);\n"
                "\n"
                "border-color: rgb(97, 97, 97);\n"
                "border-width: 0px;\n"
                "border-radius: 15px;\n"
                "border-style: solid;"
        )
        
        self.YourPasswordLabel.setObjectName("YourPasswordLabel")
        self.FrameOptionsLabel_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.FrameOptionsLabel_1.setGeometry(QtCore.QRect(20, 160, 301, 311))
        
        self.FrameOptionsLabel_1.setStyleSheet(
                "border-color: rgb(66, 66, 66);\n"
                "border-width: 5px;\n"
                "border-radius: 15px;\n"
                "border-style: solid;"
        )
        
        self.FrameOptionsLabel_1.setText("")
        self.FrameOptionsLabel_1.setObjectName("FrameOptionsLabel_1")
        self.FrameOptionsLabel_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.FrameOptionsLabel_2.setGeometry(QtCore.QRect(20, 220, 301, 281))
        
        self.FrameOptionsLabel_2.setStyleSheet(
                "border-color: rgb(66, 66, 66);\n"
                "border-width: 5px;\n"
                "border-radius: 15px;\n"
                "border-style: solid;"
        )
        
        self.FrameOptionsLabel_2.setText("")
        self.FrameOptionsLabel_2.setObjectName("FrameOptionsLabel_2")
        self.FramePasswordLabel_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.FramePasswordLabel_1.setGeometry(QtCore.QRect(340, 160, 441, 341))
        
        self.FramePasswordLabel_1.setStyleSheet(
                "border-color: rgb(66, 66, 66);\n"
                "border-width: 5px;\n"
                "border-radius: 15px;\n"
                "border-style: solid;"
        )
        
        self.FramePasswordLabel_1.setText("")
        self.FramePasswordLabel_1.setObjectName("FramePasswordLabel_1")
        self.FramePasswordLabel_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.FramePasswordLabel_2.setGeometry(QtCore.QRect(340, 220, 441, 281))
        
        self.FramePasswordLabel_2.setStyleSheet(
                "border-color: rgb(66, 66, 66);\n"
                "border-width: 5px;\n"
                "border-radius: 15px;\n"
                "border-style: solid;"
        )
        
        self.FramePasswordLabel_2.setText("")
        self.FramePasswordLabel_2.setObjectName("FramePasswordLabel_2")
        self.PasswordText = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.PasswordText.setGeometry(QtCore.QRect(355, 231, 411, 261))
        
        self.PasswordText.setStyleSheet(
                "font: 900 35pt \"Arial Black\";\n"
                "color: rgb(120, 120, 120);\n"
                "\n"
                "border-color: rgb(97, 97, 97);\n"
                "border-width: 0px;\n"
                "border-radius: 15px;\n"
                "border-style: solid;"
        )
        
        self.PasswordText.setObjectName("PasswordText")
        self.GenerateButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.GenerateButton.setGeometry(QtCore.QRect(20, 510, 301, 71))
        
        self.GenerateButton.setStyleSheet(
                "font: 900 20pt \"Arial Black\";\n"
                "color: rgb(120, 120, 120);\n"
                "\n"
                "background-color: rgb(66, 66, 66);\n"
                "\n"
                "border-color: rgb(97, 97, 97);\n"
                "border-width: 0px;\n"
                "border-radius: 15px;\n"
                "border-style: solid;"
        )
        
        self.GenerateButton.setObjectName("GenerateButton")
        self.CopyButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.CopyButton.setGeometry(QtCore.QRect(340, 510, 211, 71))
        
        self.CopyButton.setStyleSheet(
                "font: 900 20pt \"Arial Black\";\n"
                "color: rgb(120, 120, 120);\n"
                "\n"
                "background-color: rgb(66, 66, 66);\n"
                "\n"
                "border-color: rgb(97, 97, 97);\n"
                "border-width: 0px;\n"
                "border-radius: 15px;\n"
                "border-style: solid;"
        )
        
        self.CopyButton.setObjectName("CopyButton")
        self.LanguageLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.LanguageLabel.setGeometry(QtCore.QRect(40, 240, 261, 51))
        
        self.LanguageLabel.setStyleSheet(
                "font: 900 20pt \"Arial Black\";\n"
                "color: rgb(120, 120, 120);\n"
                "\n"
                "background-color: rgb(66, 66, 66);\n"
                "\n"
                "border-color: rgb(97, 97, 97);\n"
                "border-width: 0px;\n"
                "border-radius: 10px;\n"
                "border-style: solid;"
        )
        
        self.LanguageLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LanguageLabel.setObjectName("LanguageLabel")
        self.EnglishRadioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.EnglishRadioButton.setGeometry(QtCore.QRect(40, 299, 121, 41))
        
        self.EnglishRadioButton.setStyleSheet(
                "font: 900 15pt \"Arial Black\";\n"
                "color: rgb(120, 120, 120);\n"
                "\n"
                "background-color: rgb(66, 66, 66);\n"
                "\n"
                "border-color: rgb(97, 97, 97);\n"
                "border-width: 0px;\n"
                "border-radius: 5px;\n"
                "border-style: solid;"
        )
        
        self.EnglishRadioButton.setChecked(True)
        self.EnglishRadioButton.setObjectName("EnglishRadioButton")
        self.RussianRadioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.RussianRadioButton.setGeometry(QtCore.QRect(178, 300, 121, 41))
        self.RussianRadioButton.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        
        self.RussianRadioButton.setStyleSheet(
                "font: 900 15pt \"Arial Black\";\n"
                "color: rgb(120, 120, 120);\n"
                "\n"
                "background-color: rgb(66, 66, 66);\n"
                "\n"
                "border-color: rgb(97, 97, 97);\n"
                "border-width: 0px;\n"
                "border-radius: 5px;\n"
                "border-style: solid;"
        )
        
        self.RussianRadioButton.setObjectName("RussianRadioButton")
        self.PasswordLenghtLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.PasswordLenghtLabel.setGeometry(QtCore.QRect(40, 380, 261, 51))
        
        self.PasswordLenghtLabel.setStyleSheet(
                "font: 900 20pt \"Arial Black\";\n"
                "color: rgb(120, 120, 120);\n"
                "\n"
                "background-color: rgb(66, 66, 66);\n"
                "\n"
                "border-color: rgb(97, 97, 97);\n"
                "border-width: 0px;\n"
                "border-radius: 10px;\n"
                "border-style: solid;"
        )
        
        self.PasswordLenghtLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PasswordLenghtLabel.setObjectName("PasswordLenghtLabel")
        self.PasswordLengthSlider = QtWidgets.QSlider(parent=self.centralwidget)
        self.PasswordLengthSlider.setGeometry(QtCore.QRect(40, 440, 201, 41))
        self.PasswordLengthSlider.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.PasswordLengthSlider.setMinimum(5)
        self.PasswordLengthSlider.setMaximum(200)
        self.PasswordLengthSlider.setPageStep(1)
        self.PasswordLengthSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.PasswordLengthSlider.setObjectName("PasswordLengthSlider")
        self.PasswordLenValueLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.PasswordLenValueLabel.setGeometry(QtCore.QRect(250, 440, 51, 41))
        self.PasswordLenValueLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        
        self.PasswordLenValueLabel.setStyleSheet(
                "font: 900 15pt \"Arial Black\";\n"
                "color: rgb(120, 120, 120);\n"
                "\n"
                "background-color: rgb(66, 66, 66);\n"
                "\n"
                "border-color: rgb(97, 97, 97);\n"
                "border-width: 0px;\n"
                "border-radius: 10px;\n"
                "border-style: solid;"
        )
        
        self.PasswordLenValueLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PasswordLenValueLabel.setObjectName("PasswordLenValueLabel")
        self.FramePasswordLabel_1.raise_()
        self.FrameOptionsLabel_1.raise_()
        self.NameLabel.raise_()
        self.ByAuthorLabel.raise_()
        self.GitHubButton.raise_()
        self.OptionsButton.raise_()
        self.YourPasswordLabel.raise_()
        self.FrameOptionsLabel_2.raise_()
        self.FramePasswordLabel_2.raise_()
        self.PasswordText.raise_()
        self.GenerateButton.raise_()
        self.CopyButton.raise_()
        self.LanguageLabel.raise_()
        self.EnglishRadioButton.raise_()
        self.RussianRadioButton.raise_()
        self.PasswordLenghtLabel.raise_()
        self.PasswordLengthSlider.raise_()
        self.PasswordLenValueLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        pixmap = QtGui.QPixmap(255, 255)
        pixmap.fill(QtGui.QColor(0, 0, 0, 0))
        MainWindow.setWindowIcon(QtGui.QIcon(pixmap))
        
        self.enable_settings = False
        
        self.add_settings()

    def retranslateUi(self, MainWindow) -> None:
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.NameLabel.setText(_translate("MainWindow", "Password Generator"))
        self.ByAuthorLabel.setText(_translate("MainWindow", "By AdamantiumCode"))
        self.GitHubButton.setText(_translate("MainWindow", "My GitHub"))
        self.OptionsButton.setText(_translate("MainWindow", "Options"))
        self.YourPasswordLabel.setText(_translate("MainWindow", "Your password"))
        
        self.PasswordText.setHtml(
                _translate(
                        "MainWindow", 
                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                        "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                        "<html><head><meta name=\"qrichtext\" content=\"1\" "
                        "/><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                        "p, li { white-space: pre-wrap; }\n"
                        "hr { height: 1px; border-width: 0; }\n"
                        "li.unchecked::marker { content: \"\\2610\"; }\n"
                        "li.checked::marker { content: \"\\2612\"; }\n"
                        "</style></head><body style=\" font-family:\'Arial Black\'; "
                        "font-size:35pt; font-weight:900; font-style:normal;\">\n"
                        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                        "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                        "-qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"
                )
        )
        
        self.GenerateButton.setText(_translate("MainWindow", "Generate"))
        self.CopyButton.setText(_translate("MainWindow", "Copy"))
        self.LanguageLabel.setText(_translate("MainWindow", "Language"))
        self.EnglishRadioButton.setText(_translate("MainWindow", "English"))
        self.RussianRadioButton.setText(_translate("MainWindow", "Русский"))
        self.PasswordLenghtLabel.setText(_translate("MainWindow", "Password length"))
        self.PasswordLenValueLabel.setText(_translate("MainWindow", "5"))
        
    def add_settings(self) -> None:
        self.CopyButton.clicked.connect(self.copy_text)
        self.GitHubButton.clicked.connect(self.view_github)
        self.OptionsButton.clicked.connect(self.view_options)
        self.EnglishRadioButton.clicked.connect(self.change_lang)
        self.RussianRadioButton.clicked.connect(self.change_lang)
        self.GenerateButton.clicked.connect(self.generate_password)
        self.PasswordLengthSlider.valueChanged.connect(self.update_length)

    def copy_text(self) -> None:
        if (self.PasswordText.toPlainText()):
            if (self.EnglishRadioButton.isChecked()):
                self.YourPasswordLabel.setText("Password copied!")
                
            else:
                self.YourPasswordLabel.setText("Скопировано!")
                
            pyperclip.copy(self.PasswordText.toPlainText())

    def view_github(self) -> None:
        webbrowser.open("https://github.com/AdamantiumCode")

    def view_options(self) -> None:
        if (self.enable_settings):
            self.FrameOptionsLabel_1.show()
            self.FrameOptionsLabel_2.show()
            self.LanguageLabel.show()
            self.EnglishRadioButton.show()
            self.RussianRadioButton.show()
            self.PasswordLenghtLabel.show()
            self.PasswordLengthSlider.show()
            self.PasswordLenValueLabel.show()
            
            self.enable_settings = False
        else:
            self.FrameOptionsLabel_1.hide()
            self.FrameOptionsLabel_2.hide()
            self.LanguageLabel.hide()
            self.EnglishRadioButton.hide()
            self.RussianRadioButton.hide()
            self.PasswordLenghtLabel.hide()
            self.PasswordLengthSlider.hide()
            self.PasswordLenValueLabel.hide()
            
            self.enable_settings = True
            
    def change_lang(self) -> None:
        isRussian = self.RussianRadioButton.isChecked()
        
        if (isRussian and self.LanguageLabel.text() == "Скопировать"):
            return
        if (not isRussian and self.LanguageLabel.text() == "Copy"):
            return
        
        self.NameLabel.setText("Генератор паролей" if (isRussian) else "Password Generator")
        self.ByAuthorLabel.setText("От AdamantiumCode" if (isRussian) else "By AdamantiumCode")
        self.OptionsButton.setText("Настройки" if (isRussian) else "Options")
        self.YourPasswordLabel.setText("Твой пароль" if (isRussian) else "Your Password")
        self.GenerateButton.setText("Создать" if (isRussian) else "Generate")
        self.CopyButton.setText("Скопировать" if (isRussian) else "Copy")
        self.GitHubButton.setText("Мой GitHub" if (isRussian) else "My GitHub")
        self.LanguageLabel.setText("Язык" if (isRussian) else "Language")
        self.PasswordLenghtLabel.setText("Длина пароля" if (isRussian) else "Password length")

    def generate_password(self) -> None:
        self.YourPasswordLabel.setText("Твой пароль" 
                                       if (self.RussianRadioButton.isChecked())
                                       else "Your password"
                                       )
        
        length = self.PasswordLengthSlider.value()
        
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=;./?\|~[]{}"

        while True:
            password = ''.join(secrets.choice(alphabet) for _ in range(length))

            if (any(c.islower() for c in password) 
                and any(c.isupper() for c in password)
                and any(c in "!@#$%^&*()-_+=;./?\|~[]{}" for c in password)
                and sum(c.isdigit() for c in password) >= 3 if (length > 10) else 1):
                    
                break

        self.PasswordText.setText(password)

    def update_length(self) -> None:
        self.PasswordLenValueLabel.setText(str(self.PasswordLengthSlider.value()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    
    sys.exit(app.exec())
