import hashlib
import os
import re
import uuid
import subprocess

class hardware:
    _id = None

    @staticmethod
    def id():
        if hardware._id:
            return hardware._id

        id_raw = [''] * 2

        id_raw[0] = hardware.get_windows_uuid()
        if not id_raw[0] or 'Default string' in id_raw[0] or 'None' in id_raw[0]:
            id_raw[0] = None

        id_raw[1] = hardware.wmic_diskdrive_get_serialnumber()
        if not id_raw[1] or 'Default string' in id_raw[1] or 'None' in id_raw[1]:
            id_raw[1] = None

        id_raw__join = '|'.join(x for x in id_raw if x).lower()

        if not id_raw__join:
            raise Exception('Can''t generate hardware id')

        print(id_raw)

        hardware._id = hashlib.md5(id_raw__join.encode('utf-8')).hexdigest()

        return hardware._id

    @staticmethod
    def get_windows_uuid():
        try:
            # Ask Windows for the device's permanent UUID. Throws if command missing/fails.
            txt = os.popen("wmic csproduct get uuid").read()

            # Attempt to extract the UUID from the command's result.
            match = re.search(r"\bUUID\b[\s\r\n]+([^\s\r\n]+)", txt)
            if match is not None:
                txt = match.group(1)
                if txt is not None:
                    # Remove the surrounding whitespace (newlines, space, etc)
                    # and useless dashes etc, by only keeping hex (0-9 A-F) chars.
                    txt = re.sub(r"[^0-9A-Fa-f]+", "", txt)

                    # Ensure we have exactly 32 characters (16 bytes).
                    if len(txt) == 32:
                        return str(uuid.UUID(txt))
        except:
            return None
        return None

    @staticmethod
    def wmic_diskdrive_get_serialnumber():
        try:
            return os.popen("wmic diskdrive get serialnumber").read().split()[-1].replace('\'', '').replace('.','')
        except:
            return None
