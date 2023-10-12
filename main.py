#main

import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

import random

from pathlib import Path 

import dialogs

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(300,170))

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        option_layout = QGridLayout()
        self.password_generated = QLineEdit()
        button_layout = QHBoxLayout()

        main_layout.addLayout(option_layout)
        main_layout.addWidget(self.password_generated)
        main_layout.addLayout(button_layout)

        #btn
        btn_quit = QPushButton("Quitter", self)
        btn_copy = QPushButton("Copy", self)
        btn_generate = QPushButton("Générer", self)
        button_layout.addWidget(btn_quit)
        button_layout.addWidget(btn_copy)
        button_layout.addWidget(btn_generate)

        self.txt_size = QLabel("Taille : 10")
        option_layout.addWidget(self.txt_size, 0, 0)

        #Slider
        self.option_size = QSlider(Qt.Horizontal)
        self.option_size.setMinimum(8)
        self.option_size.setMaximum(30)
        self.option_size.setValue(10)
        option_layout.addWidget(self.option_size, 1, 0)

        #params
        self.option_lowercase = QCheckBox("Minuscules")
        option_layout.addWidget(self.option_lowercase, 0,1)
        self.option_uppercase = QCheckBox("Majuscules")
        option_layout.addWidget(self.option_uppercase, 1, 1)
        self.option_numbers = QCheckBox("Chiffres")
        option_layout.addWidget(self.option_numbers, 0, 2)
        self.option_symbols = QCheckBox("Symboles")
        option_layout.addWidget(self.option_symbols, 1, 2)

        #checkbox check open application
        self.option_lowercase.setChecked(True)
        self.option_numbers.setChecked(True)

        #display pass at open
        self.generate()

        #Connect btn
        btn_quit.clicked.connect(self.quit)
        btn_copy.clicked.connect(self.copy)

        self.option_size.valueChanged.connect(self.change_size)

        btn_generate.clicked.connect(self.generate)

        #status bar
        self.setStatusBar(QStatusBar(self))
        self.status = self.statusBar()

    #Action btn
    def quit(self):
        if dialogs.confirm(self):
            QApplication.quit() 

    def copy(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.password_generated.text())
        self.status.showMessage("Mot de passe copié", 1000)

        #recupère la valeur => affiche
    def change_size(self):
        value = self.option_size.value()
        self.txt_size.setText("Taille : " + str(value))

        #add different options => generate password!
    def generate(self):
        size = self.option_size.value()
        has_lower = self.option_lowercase.isChecked()
        has_upper = self.option_uppercase.isChecked()
        has_numbers = self.option_numbers.isChecked()
        has_symbols = self.option_symbols.isChecked() 

        mdp = "azertyuiopqsdfghjklmwxcvbn"

        if has_upper: 
            mdp += "AZERTYUIOPQSDFGHJKLMWXCVBN"
        if has_numbers: 
            mdp += "0987654321"
        if has_symbols:
            mdp += "!@#$%^&*()_-+=<>?/"

        # mdp = ''.join(random.choice(mdp) for _ in range(size))
        # self.password_generated.setText(mdp)

        ## Correction
        password = ""
        for i in range(size):
            password += random.choice(mdp)
        self.password_generated.setText(password)

app = QApplication(sys.argv)

window = MainWindow()
window.setWindowTitle("TextEditor2000")
window.show()

app.exec()
