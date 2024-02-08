import os
path_name = "saves"

from modules import systemcheck
clear = systemcheck.clearVal()

# Creates a directory for finding saves
def findSaves():
    absolute_path = os.path.dirname(__file__)
    absolute_path = absolute_path[:-7]
    relative_path = path_name
    return os.path.join(absolute_path, relative_path)

# Returns a list of all the saves (.txt) found in the path
def returnSaveList():
    list = []
    # No idea how this works
    for (root, dirs, files) in os.walk(findSaves()):
        for x in files:
            if '.txt' in x:
                # Edit string to only show the file name
                split_name = x.split('.txt')
                final_name = ''.join(split_name)
                list.append(final_name)
    return list

# Print the list of saves
def printSaves():
    # Create a list of saves
    saveList = returnSaveList()
    print("Files retrieved from %s" % findSaves())
    print("%d valid (.txt) files found!" % len(saveList))
    # Print on same line, and then print an extra new line after it is done
    for x in saveList:
        print(x, end=", ")
    print('\n')

# Return a selected file name through an input
def selectSave():
    loop = 1
    printSaves()
    while loop:
        selected_save = input("Load a file. EXIT to quit, LIST to display saves: ")
        if selected_save.lower() == 'exit':
            loop = 0
        elif selected_save.lower() == 'list':
            os.system(clear)
            printSaves()
        elif selected_save in returnSaveList():
            return selected_save
        else:
            print("File not found, check file name?")

# Returns a save as a list
def passSaveAsList(save_name):
    file_path = findSaves() + '/' + save_name + '.txt'
    file_list = []
    word = ''

    contents = ''
    with open(file_path, 'r') as file:
        contents = file.read(-1)

    for character in contents:
        if character == ' ':
            if not word == '': file_list.append(word)
            word = ''
            continue
        if character == '\n':
            if not word == '': file_list.append(word)
            file_list.append('\n')
            word = ''
            continue
        word += character
    
    return file_list
