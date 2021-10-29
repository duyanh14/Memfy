import tempfile
import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

for x in range(10):
    xx = ROOT_DIR.rsplit('\\', x)[0]
    if os.path.isfile(xx + "\\memfy.py") or os.path.isfile(xx + "\\memfy.exe"):
        ROOT_DIR = xx
        break

TEMP_DIR = tmppath = "C:\\User\\{}\\AppData\\Local\\Temp".format(os.getlogin()) + "\\Memfy"

CURRENT_FILE = sys.argv[0]

IS_COMPILE = CURRENT_FILE.endswith('.exe')