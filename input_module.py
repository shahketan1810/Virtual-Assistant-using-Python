import speak_module
from database import speak_is_on
import sys
import os
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from first_of_VA2 import *
os.system('cls')

    
def take_input(self):
    if speak_is_on():
        i=speak_module.get_audio()
    else:
        text, okPressed = QInputDialog.getText(self, "Get text","enter your query:", QLineEdit.Normal, "")
        if okPressed and text != '':
            i=text 
        else:
            i="no query"
    return i