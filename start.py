import zendocs
import sys

from tkinter import *

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QTimer

class Start(QMainWindow):
	def __init__(self, parent=None):
		super(Start, self).__init__(parent)

		self.layout = QVBoxLayout()

		self.setWindow()

		QTimer.singleShot(3000, self.close)

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

		self.setGeometry(startLeft, startTop, width//2, height//2);

		self.setWindowFlag(Qt.WindowFlags.FramelessWindowHint)

		#self.callNextInstance()

	def callNextInstance(self):

		zendocs.main()

def main():

	# Initialize application
	app = QApplication(sys.argv)

	# Initialize widget
	mainWindow = Start()

	# Show the window
	mainWindow.show()

	# Execute the application
	app.exec()

	zendocs.main()


if __name__ == "__main__":
	main()