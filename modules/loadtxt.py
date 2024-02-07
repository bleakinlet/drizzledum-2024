import os
path_name = "saves"

# Creates a directory for finding saves
def findSaves():
    absolute_path = os.path.dirname(__file__)
    absolute_path = absolute_path[:-7]
    relative_path = path_name
    return os.path.join(absolute_path, relative_path)

# Returns a list of all the saves (.txt) found in the path
def returnSaves():
    list = []
    # No idea how this works
    for (root, dirs, file) in os.walk(findSaves()):
        for x in file:
            if '.txt' in x:
                # Edit string to only show the file name
                split_name = x.split('.txt')
                final_name = ''.join(split_name)
                list.append(final_name)
    return list

# Print the list of saves
def printSaves():
    # Create a list of saves
    saveList = returnSaves()
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
            printSaves()
        elif selected_save in returnSaves():
            return selected_save
        else:
            print("File not found, check file name?")

def returnSave():
    pass