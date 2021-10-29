from PyQt5.QtCore import  QThread, pyqtSignal
import memory

class clean_memory(QThread):

    callback = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

    def run(self):
        self.callback.emit(True)
        memory.clear()
        self.callback.emit(False)
        self.stop()

    def stop(self):
        self.quit()
