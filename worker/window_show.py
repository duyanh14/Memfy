import threading
import traceback
import urllib.request
import os
import config
from api import api
from hardware import hardware
from PyQt5.QtCore import QThread, pyqtSignal
import time
import random

class window_show(QThread):

    set_banner = pyqtSignal(int)

    application_request = None

    banner_list = {}

    def __init__(self):
        super().__init__()

    def run(self):
        self.application()

        if window_show.banner_list:
            self.set_banner.emit(random.choice(list(window_show.banner_list)))

        self.stop()

    def stop(self):
        self.quit()

    def application(self):
        if window_show.application_request:
            today = time.localtime(window_show.application_request)
            end = time.struct_time((today.tm_year, today.tm_mon, today.tm_mday, 0, 0, 0, 0, 0, today.tm_isdst))
            if time.time() < (time.mktime(end) + 86400):
                return

        try:
            parameter = {
                'hardware': hardware.id()
            }
            result = api.request.make(['application'], parameter)
            window_show.application_request = time.time()
        except:
            return traceback.print_exc()

        if 'banner' in result:
            try:
                os.makedirs(config.TEMP_DIR + '\\Banner')
            except FileExistsError:
                pass

            banner_file = os.listdir(config.TEMP_DIR + '\\Banner')

            window_show.banner_list = {}

            for banner in result['banner']:
                try:
                    file_name = str(banner['id']) + '.jpg'
                    if not file_name in banner_file:
                        urllib.request.urlretrieve(banner['image'], config.TEMP_DIR + '\\Banner\\' + file_name)

                    window_show.banner_list[banner['id']] = {
                        'url': banner['url']
                    }
                except:
                    traceback.print_exc()

            print(window_show.banner_list)

            banner_file = os.listdir(config.TEMP_DIR + '\\Banner')

            for file_name in banner_file:
                try:
                    if not int(file_name.replace('.jpg','')) in window_show.banner_list:
                        os.remove(config.TEMP_DIR + '\\Banner\\' + file_name)
                except:
                    os.remove(config.TEMP_DIR + '\\Banner\\' + file_name)
