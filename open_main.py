import start_main
import sys
import time

from tkinter import *

from PySide6.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QWidget, QPushButton, QLabel
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QTimer, Slot

class Start(QMainWindow):
    '''
    This is the main window that appears when we start the application. This window
    serves no utility purpose and is only for the display of the program's logo.
    '''
    def __init__(self):
        super().__init__()

        self.w = None # No external window yet.

        QTimer.singleShot(2000, self.show_next_instance)

        self.setWindow()
        self.setWindowTitle("oof")

    def show_next_instance(self):
        if self.w is None:
            self.w = start_main.ZenDocs()
            self.close()
        self.w.showMaximized()

    '''Sets the layout of the window'''
    def setWindow(self):
        title = "Zendocs"
        icon = "img/icon2.png"

        stylesheet = "background-image: url(./img/intrologo.jpg);" \
                        "background-repeat: no-repeat;" \
                        "background-position: center"

        root = Tk()
        height = root.winfo_screenheight()
        width = root.winfo_screenwidth()

        startTop, startLeft = height//4, width//4

        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))
        self.setStyleSheet(stylesheet)

        self.setGeometry(startLeft, startTop, width//2, height//2)

        self.setWindowFlag(Qt.FramelessWindowHint)

def main():
    # Initialize application
    app = QApplication([])

    # Initialize widget
    mainWindow = Start()

    # Show the window
    mainWindow.show()

    # Exit
    sys.exit(app.exec())

if __name__ == "__main__":
	main()