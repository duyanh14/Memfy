import time
import threading
import traceback
from PyQt5.QtCore import  QThread, pyqtSignal
import memory
import setting

class tracking_memory(QThread):

    callback = pyqtSignal(dict)

    usage = memory.usage()

    last_clean = time.time()

    clean_above = False

    thread__clear_condition = None

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            try:
                clear_condition = False

                self.usage = memory.usage()

                self.callback.emit(self.usage)

                if setting.CLEAN_WHEN_ABOVE__ENABLE:
                    if self.clean_above and \
                            self.usage['percent'] < setting.CLEAN_WHEN_ABOVE__VALUE:
                        self.clean_above = False

                    if not self.clean_above and  \
                        self.usage['percent'] >= setting.CLEAN_WHEN_ABOVE__VALUE:
                        self.clean_above = True
                        clear_condition = True

                if setting.CLEAN_EVERY_MIN__ENABLE and \
                    time.time() > self.last_clean + (setting.CLEAN_EVERY_MIN__VALUE*60):
                    self.last_clean = time.time()
                    clear_condition = True

                if clear_condition:
                    if not self.thread__clear_condition or not self.thread__clear_condition.is_alive():
                        self.thread__clear_condition = threading.Thread(target=self.clear_condition)
                        self.thread__clear_condition.start()
            except:
                traceback.print_exc()
            time.sleep(1)
        self.stop()

    def clear_condition(self):
        memory.clear()

    def stop(self):
        self.quit()
