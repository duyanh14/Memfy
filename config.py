import tempfile
import sys
import os

TEMP_DIR = tmppath = "C:\\User\\{}\\AppData\\Local\\Temp".format(os.getlogin()) + "\\Memfy"

CURRENT_FILE = sys.argv[0]

IS_COMPILE = CURRENT_FILE.endswith('.exe')