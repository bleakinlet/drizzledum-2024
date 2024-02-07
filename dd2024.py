import os

# Creates a directory for finding the Goblin Saves
def findGoblins():
    absolute_path = os.path.dirname(__file__)
    relative_path = "goblins"
    return os.path.join(absolute_path, relative_path)

# Returns a list of all the goblins (.txt) found in /goblins
def returnGoblins():
    list = []
    # No idea how this works
    for (root, dirs, file) in os.walk(findGoblins()):
        for x in file:
            if '.txt' in x:
                # Put all goblins into a list
                list.append(x)
    return list


os.system('clear')
# Create a list of goblins
goblinList = returnGoblins()
for x in goblinList:
    print(x)



