from PyQt5.QtCore import QThread

class worker(QThread):

    def __init__(self):
        super().__init__()

    def run(self):
        self.stop()

    def stop(self):
        self.quit()
