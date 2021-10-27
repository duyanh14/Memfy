from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class generate_insert_frame(QThread):

    threadSignal = pyqtSignal(str)                             # <<---

    def __init__(self, num=1):
        super().__init__()
        self.num = num

    def run(self):
        self.threadSignal.emit("Test {}".format(self.num))     # <<---
        self.msleep(100)
        self.stop()

    def stop(self):
        self.quit()


class MyWindow(QWidget):   
    def __init__ (self):
        super().__init__ ()
        self.setWindowTitle("MyWindow")

        button = QPushButton("Start Thread")
        button.clicked.connect(self.click_insertproject)
        grid = QGridLayout(self)
        grid.addWidget(button)
        self.num = 1

    def click_insertproject(self):
        self.thread = generate_insert_frame(self.num) 
        self.thread.threadSignal.connect(self.setWindowTitle)    # <<---
        self.thread.start()
        self.num += 1

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.resize(400, 200)
    window.show()
    sys.exit(app.exec_())