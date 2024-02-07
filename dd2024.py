import os

# Figure out if we're on mac or windows, no linux suport :faku:
from modules import systemcheck
clear = systemcheck.clearVal()

# Import loadtxt, set save path to goblins instead of saves
from modules import loadtxt
loadtxt.path_name = "goblins"    

def loadSave():
    os.system(clear)
    save_name = loadtxt.selectSave()
    save_data = []

    if save_name:
        save_data = loadtxt.passSaveAsList(save_name)
        print(save_data)


loadSave()

# go through list and scan for keywords
# append save data onto the bottom



