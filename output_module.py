import assistant_details
from speak_module import speak
from database import speak_is_on
import os
from first_of_VA2 import *


def give_output(o):

    if speak_is_on():
        if o=="signing off sir":
            speak(o)
            os._exit(0)
        else:
            speak(o)
    msg = QMessageBox()
    msg.setWindowTitle(f"{assistant_details.name}")
    msg.setText(f'{assistant_details.name}: {o}')
    x = msg.exec_()

    print(f'{assistant_details.name}: {o}')
    print()