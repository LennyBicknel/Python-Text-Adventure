# -----txtadvclasses-----
# Xander Lewis - 08/08/14
# -----------------------

class Env():
    """An environment with an ID, a description, a list of items, and neighbouring environments."""
    def __init__(self, ID, desc, items, left, front, right, back):
        self.ID = ID
        self.desc = desc
        self.items = items
        self.left = left
        self.front = front
        self.right = right
        self.back = back

    def getID():
        return self.ID
    
    def getDesc():
        return self.desc
    
    def getItems():
        return self.items
    
    def getNeighbour(loc):
        if(loc == left): return left
        elif(loc == front): return front
        elif(loc == right): return right
        elif(loc == back): return back
        
    def takeItem(itemName):
        # Remove item from envs items list
        for i in range(len(items)):
            if(items[i].getName() == itemName):
                itemSelected = items[i]
                items[i].pop()
                
        # Return selected Item instance
        return itemSelected

class Item():
    """An item with a name, a description and an action. It can be 'used' by calling the use() method."""
    def __init__(self, name, desc, action):
        self.name = name
        self.desc = desc

    def getName():
        return self.name

    def getDesc():
        return self.desc

    def use():
        # [Will contain code executed when item is used (related to its action)]
        pass

class Player():
    """A player with a name, a location and a list of items called an 'inventory'."""
    def __init__(self, name):
        self.name = name
        self.location = 0
        self.inventory = []

    def getName():
        return self.name

    def getInv():
        return self.inventory

# FUNCTIONS ---------------------------------------------------------------

def loadEnvs(path):
    """Loads a set of envs from a file and returns a list of Env objects."""
    # Load list of lines in file
    with open(path, "r") as file:
        fileList = file.readlines()

    # Split each line and create an instance of Env accordingly. Append that instance to envList.
    envList = [Env(line.split("\t")[0], line.split("\t")[1], line.split("\t")[2], line.split("\t")[3], line.split("\t")[4], line.split("\t")[5], line.split("\t")[6]) for line in fileList]

    # Return list of Env instances.
    return envList

def loadItems(path):
    """Loads a set of items from a file and returns a list of Item objects."""
    # Load list of lines in file
    with open(path, "r") as file:
        fileList = file.readlines()

    # Split each line and create an instance of Item accordingly. Append that instance to itemList.
    itemList = [Item(line.split("\t")[0], line.split("\t")[1], line.split("\t")[2]) for line in fileList]

    # Return list of Item instances
    return itemList
