import os
from sys import platform

# Import loadtxt, set save path to goblins instead of saves
from modules import loadtxt
loadtxt.path_name = "goblins"    

def platformVariables():
    if platform == "win32":
        return 'clr'
    elif platform == 'darwin':
        return 'clear'

def selectGoblin(name):
    pass

clear = platformVariables()
os.system(clear)
save_name = loadtxt.selectSave()

# select correct save
# read save and put it all into a list
# go through list and scan for keywords
# append save data onto the bottom



