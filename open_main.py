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
    def __init__(self, parent=None):
        super(Start, self).__init__(parent)

        self.layout = QVBoxLayout()
        self.setWindow()

    '''Sets the layout of the window'''
    def setWindow(self):
        pass

'''Goes to the next iteration of the program - the ZenDocs file'''
def show_next_instance():
    nextw = start_main.ZenDocs()
    nextw.show()
    print('test10')

def main():
    # Initialize application
    app = QApplication([])

    print('test1')

    # Initialize widget
    mainWindow = Start()

    print('test2')

    # Show the window
    mainWindow.show()

    QTimer.singleShot(3000, app)
    mainWindow.close()

    print('test3')

    # Call next instance of the program
    show_next_instance()

    print('test0')

    # Execute the application
    sys.exit(app.exec())


if __name__ == "__main__":
	main()