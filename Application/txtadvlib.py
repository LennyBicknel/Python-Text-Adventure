# -------txtadvlib-------
# Xander Lewis - 08/08/14
# -----------------------

class Env():
    """An environment with an ID, a description, a list of item IDs, and neighbouring environments."""
    def __init__(self, ID, desc, items, left, front, right, back):
        self.ID = ID
        self.desc = desc
        self.items = items
        self.left = left
        self.front = front
        self.right = right
        self.back = back

    def getID(self):
        return self.ID
    
    def getDesc(self):
        return self.desc
    
    def getItems(self):
        return self.items
    
    def getNeighbour(self, loc):
        if(loc == "left"): return self.left
        elif(loc == "front"): return self.front
        elif(loc == "right"): return self.right
        elif(loc == "back"): return self.back
        
    def takeItem(self, itemName):
        # Remove item from envs items list
        for i in range(len(self.items)):
            if(self.items[i].getName() == itemName):
                itemSelected = self.items.pop(i)
                
        # Return selected Item instance
        return itemSelected

    def getLeft(self):
        return self.left
    
    def getFront(self):
        return self.front

    def getRight(self):
        return self.right

    def getBack(self):
        return self.back

class Item():
    """An item with a name, a description and an action. It can be 'used' by calling the use() method."""
    def __init__(self, name, desc, action):
        self.name = name
        self.desc = desc

    def getName(self):
        return self.name

    def getDesc(self):
        return self.desc

    def use(self):
        # [Will contain code executed when item is used (related to its action)]
        pass

class Player():
    """A player with a name, a location, an hp (health points) value and a list of items called an 'inventory'."""
    def __init__(self, name):
        self.name = name
        self.loc = 0
        self.hp = 500
        self.inv = []

    def getName(self):
        return self.name

    def getLoc(self):
        return int(self.loc)
    
    def setLoc(self, newLoc):
        self.loc = newLoc

    def getHP(self):
        return self.hp

    def setHP(self, newHP):
        self.hp == newHP

    def changeHP(self, change):
        self.hp += change

    def getInv(self):
        return self.inv
    
    def addToInv(self, item):
        self.inv.append(item)

# FUNCTIONS ---------------------------------------------------------------

def loadEnvs(path, itemList):
    """Loads a set of envs from a file and returns a list of Env objects."""
    # Load list of lines in file
    with open(path, "r") as file:
        fileList = file.readlines()

    # Iterate through the file two lines at a time, extracting env data
    envList = []
    for i in range(0, len(fileList), 2):
        
        # Create item list
        if(fileList[i+1] != "NULL"):
            items = [itemList[int(index)] for index in fileList[i+1].split("\t")]
        else:
            items = []
            
        # Create Envs
        envList.append(Env(fileList[i].split("\t")[0], fileList[i].split("\t")[1], items, fileList[i].split("\t")[2], fileList[i].split("\t")[3], fileList[i].split("\t")[4], fileList[i].split("\t")[5]))

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

def createPlayer(name):
    return Player(name)
