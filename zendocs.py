# This Python file uses the following encoding: utf-8
import sys

from PyQt6.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon, QTextBlock, QTextItem

class ZenDocs(QWidget):
    def __init__(self):
        super().__init__()

        self.window = QWidget()

        self.setWindowsLayout()

    '''Set the layout of the entire program'''
    def setWindowsLayout(self):

        # Make main layout
        main_layout = QVBoxLayout(self.window)
    
        # Make main two widgets
        top_widget = QWidget()
        bottom_widget = QWidget()

        # Make nested bottom widgets
        bottom_left_widget = QWidget()
        bottom_right_widget = QWidget()

        # Add top and bottom widgets to the main layout
        main_layout.addWidget(top_widget)
        main_layout.addWidget(bottom_widget)

        # Create top and bottom layouts
        top_layout = QHBoxLayout(top_widget)
        bottom_layout = QHBoxLayout(bottom_widget)

        # Add item to top layout
        top_layout.addWidget(QPushButton('TOP'))
        
        # Add two nested widgets to bottom layout
        bottom_layout.addWidget(bottom_left_widget)
        bottom_layout.addWidget(bottom_right_widget)

        # Create layouts for bottom left and right
        bottom_left_layout = QVBoxLayout(bottom_left_widget)
        bottom_right_layout = QVBoxLayout(bottom_right_widget)

        bottom_left_layout.addWidget(QPushButton('BOTTOM LEFT 0'))
        bottom_left_layout.addWidget(QPushButton('BOTTOM LEFT 1'))
        bottom_left_layout.addWidget(QPushButton('BOTTOM LEFT 2'))
        bottom_left_layout.addWidget(QPushButton('BOTTOM LEFT 3'))
        bottom_left_layout.addWidget(QPushButton('BOTTOM LEFT 4'))

        # Set the text window
        self.setMainTextWindow(bottom_right_layout)

        # Set the window parameters
        self.setWindow(main_layout)

    ''' Set the text widget '''
    def setMainTextWindow(self, bottom_right_layout):

        # Set the parameters for the text window
        backgroundColor = "#1f1f1f"
        textColor = "white"
        fontSize = "40px"
        fontStyle = "Arial"
        margin_left = "100px"
        margin_top = "100px"

        # Make new text editor and set its style
        mainTextWindow = QTextEdit(self)
        mainTextWindow.setStyleSheet("background-color: {};"
                                     "color: {};"
                                     "font: {} {};"
                                     "border: 0px;"
                                     "margin-left: {};"
                                     "margin-top: {};".format(backgroundColor, textColor, fontSize, fontStyle, margin_left, margin_top))

        # Add the text editor to the main window
        bottom_right_layout.addWidget(mainTextWindow)

    ''' Set the main window to desired colors'''
    def setWindow(self, main_layout):

        # Set the parameters for the main window
        title = "Zendocs"
        icon = "img/icon2.png"
        backgroundColor = "#1c1c1c"

        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))
        self.setStyleSheet("background-color: {}".format(backgroundColor))

        # Set the main window Geometry
        self.setGeometry(0, 0, 800, 600)

        # Set the layout to the layour previosuly defined
        self.setLayout(main_layout)

def main():

    # Instantiate application
    app = QApplication(sys.argv)

    # Instantiate main widget (main window)
    mainWindow = ZenDocs()

    # Initialize fully maximized
    mainWindow.showMaximized()

    # Execute application and close
    sys.exit(app.exec())

if __name__ == "__main__":
    main()