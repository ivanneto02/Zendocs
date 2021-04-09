# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel


class ZenDocs(QWidget):
    def __init__(self):
        QWidget.__init__(self)


if __name__ == "__main__":
    app = QApplication([])
        
    # Label
    label = QLabel("zendocs")
    label.show()

    window = ZenDocs()
    window.show()
    sys.exit(app.exec_())
