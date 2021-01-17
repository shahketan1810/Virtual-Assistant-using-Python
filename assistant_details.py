from database import get_name
import os
import platform

name = get_name()


def is_windows():
    if "windows" in (str(platform.platform())).lower():
        return True
    else:
        return False