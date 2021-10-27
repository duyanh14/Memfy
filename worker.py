import threading
import traceback
import urllib.request
import os
import config
from api import api
from hardware import hardware
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal)
import time

class worker(QRunnable):

    def __init__(self,widget):
        QRunnable.__init__(self)
        self.widget = widget
        self.widget.show()

    @staticmethod
    def run(widget):

        widget.setWindowTitle('abc')

        #
        # self.abc()
        #
        # # time.sleep(5)
        #
        # try:
        #     self.widget.setWindowTitle('abc')
        # except:
        #     traceback.print_exc()

    def abc(self):
        parameter = {
            'hardware': hardware.id()
        }
        result = api.request.make(['application'], parameter)

        if 'banner' in result:
            try:
                os.makedirs(config.TEMP_DIR + '\\Banner')
            except FileExistsError:
                pass

            banner_file = os.listdir(config.TEMP_DIR + '\\Banner')

            banner_list = {}

            for banner in result['banner']:
                try:
                    file_name = str(banner['id']) + '.jpg'
                    if not file_name in banner_file:
                        urllib.request.urlretrieve(banner['image'], config.TEMP_DIR + '\\Banner\\' + file_name)

                    banner_list[banner['id']] = {
                        'title': banner['title']
                    }
                except:
                    traceback.print_exc()

            banner_file = os.listdir(config.TEMP_DIR + '\\Banner')

            for file_name in banner_file:
                try:
                    if not int(file_name.replace('.jpg','')) in banner_list:
                        os.remove(config.TEMP_DIR + '\\Banner\\' + file_name)
                except:
                    os.remove(config.TEMP_DIR + '\\Banner\\' + file_name)
