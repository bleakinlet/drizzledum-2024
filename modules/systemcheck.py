import platform

def clearVal():
    if platform == "win32":
        return 'clr'
    else:
        return 'clear'