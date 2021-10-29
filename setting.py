import winreg
import traceback

def load(key,type,default):
    value = None
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                      r'SOFTWARE\Memfy', 0,
                                      winreg.KEY_READ)
        value = winreg.QueryValueEx(registry_key, 'SETTING__'+key)[0]
        winreg.CloseKey(registry_key)
        if type is bool:
            value = int(value)
    except:
        pass
    if value == None:
        value = default
    globals()[key] = type(value)
    return globals()[key]

def set(key,type,value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Memfy')
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                      r'SOFTWARE\Memfy', 0,
                                      winreg.KEY_WRITE)
        if type is bool:
            value = int(value)
        winreg.SetValueEx(registry_key, 'SETTING__'+key, 0, winreg.REG_SZ, str(value))
        winreg.CloseKey(registry_key)
    except:
        traceback.print_exc()
    globals()[key] = type(value)

# WINDOW_HANDLE = load('WINDOW_HANDLE',int,123456)

CLEAN_EVERY_MIN__ENABLE = load('CLEAN_EVERY_MIN__ENABLE',bool,False)
CLEAN_EVERY_MIN__VALUE = load('CLEAN_EVERY_MIN__VALUE',int,120)

CLEAN_WHEN_ABOVE__ENABLE = load('CLEAN_WHEN_ABOVE__ENABLE',bool,True)
CLEAN_WHEN_ABOVE__VALUE = load('CLEAN_WHEN_ABOVE__VALUE',int,90)