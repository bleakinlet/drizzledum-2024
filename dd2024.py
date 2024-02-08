import os

# Figure out if we're on mac or windows, no linux suport :faku:
from modules import systemcheck
clear = systemcheck.clearVal()

# Import loadtxt, set save path to goblins instead of saves
from modules import loadtxt
loadtxt.path_name = "goblins"    

# Returns a save list that has been unchanged.
def loadSave():
    os.system(clear)
    save_name = loadtxt.selectSave()

    if save_name:
        return loadtxt.passSaveAsList(save_name)

# Returns a dict of all the correct variables
def goblinAlgorithmEncode(save):

    save_int_data = []
    save_string_data = []

    save_int_data = list(filter(lambda s: s.isnumeric(), save))
    save_int_data = list(map(lambda i: int(i), save_int_data))
    
    print(save_int_data)
    print(save_string_data)

save_data = []
save_data = loadSave()
print(save_data)
# goblinAlgorithmEncode(save_data)

# go through list and scan for keywords
# append save data onto the bottom



