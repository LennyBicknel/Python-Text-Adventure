# -----txtadvclasses-----
# Xander Lewis - 21/07/14
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
                
        return itemSelected

class Item():
    """An item with a name, a description. It can be 'used' by calling the use() method."""
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def getName():
        return self.name

    def getDesc():
        return self.desc

    def use():
        # Will contain code executed when item is used
        pass

class Player():
    """A player with a name and a list of items called an 'inventory'."""
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def getName():
        return self.name

    def getInv():
        return self.inventory
