import psutil
from ctypes import *
from ctypes.wintypes import *


def size(byte):
    # this the function to convert bytes into more suitable reading format.

    # Suffixes for the size
    for x in ["B", "KB", "MB", "GB", "TB"]:
        if byte < 1024:
            return f"{byte:.2f} {x}"
        byte = byte / 1024


def usage():
    mem = psutil.virtual_memory()
    return {
        'total_available': size(mem.total),
        'available': size(mem.available),
        'used': size(mem.used),
        'percent': mem.percent
    }

def clear():
    for proc in psutil.process_iter():
        try:
            clear_pid(proc.pid)
            clear_pid(proc.pid)
        except:
            pass

def clear_pid(pid):
    handle = windll.kernel32.OpenProcess(DWORD(0x1F0FFF), False, DWORD(pid))
    if handle != 0:
        windll.kernel32.SetProcessWorkingSetSizeEx(handle, c_size_t(-1), c_size_t(-1), DWORD(0x1))
        windll.psapi.EmptyWorkingSet(handle)
        windll.kernel32.CloseHandle(handle)
