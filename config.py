import tempfile
import sys

TEMP_DIR = tempfile.gettempdir() + "\\Memfy"

CURRENT_FILE = sys.argv[0]

IS_COMPILE = CURRENT_FILE.endswith('.exe')