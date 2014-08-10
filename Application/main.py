import txtadvlib, os
from iowrapper import *

# ---------main----------
# Xander Lewis - 21/07/14
# -----------------------

def cls():
    """Clears the screen."""
    clearstr = ""
    for i in range(100):
        clearstr += "\n"
    strOut(clearstr)

def intro(name):
    """Welcomes and introduces the player to the game."""
    cls()
    strOut("Welcome, {0}, to [Text Adventure]!".format(name))
    strOut("--- How to play -----------------------------------------------------------")
    strOut("Type the direction you would like to travel, or just use the first letter.")
    strOut("There are four directions: left (l), right (r), forwards (f), and back (b).")
    strOut("To pick up an item, type 'take <item name>'.")
    strOut("To read about an item, type 'inspect <item name>'.")
    strOut("To use an item, type 'use <item name>'.")
    strOut("The '?' symbol indicates that you should type something.")
    strOut("---------------------------------------------------------------------------")
    strIn("Press enter to continue...")

def playerStatus(player, itemList):
    """Prints information about the player."""
    cls()
    strOut("----{0}----".format(player.getName()))
    strOut("HP: {0}".format(player.getHP()))
    if(player.getInv() == []):
        strOut("You are carrying nothing.")
    else:
        strOut("Inventory:")
        for each in player.getInv():
            strOut(itemList[each].getName())

def envDesc(envs, ID):
    strOut("\nYou look around...")
    # Print current envs description
    strOut(envs[ID].getDesc())

    # If there is an env in a given direction, print its description
    if(envs[ID].getLeft().strip() != "NULL"):
        strOut("\nTo your left, {0}".format(envs[int(envs[ID].getLeft())].getDesc()))
    if(envs[ID].getFront().strip() != "NULL"):
        strOut("\nIn front of you, {0}".format(envs[int(envs[ID].getFront())].getDesc()))
    if(envs[ID].getRight().strip() != "NULL"):
        strOut("\nTo your right, {0}".format(envs[int(envs[ID].getRight())].getDesc()))
    if(envs[ID].getBack().strip() != "NULL"):
        strOut("\nBehind you, {0}".format(envs[int(envs[ID].getBack())].getDesc()))

    if(envs[ID].getItems() != []):
        strOut("\nYou see the following items:")
        for item in envs[ID].getItems():
            strOut(item.getName())

def evalCmd(cmd, player, envs):
        # Moving left?
        if(cmd == "left" or cmd == "l"):
            if(envs[player.getLoc()].getLeft().strip() != "NULL"):
                strOut("You move left...")
                player.setLoc(envs[player.getLoc()].getLeft())
            else:
                strOut("You cannot move left.")
                
        # Moving forwards?
        elif(cmd == "forwards" or cmd == "f"):
            if(envs[player.getLoc()].getFront().strip() != "NULL"):
                strOut("You move forwards...")
                player.setLoc(envs[player.getLoc()].getFront())
            else:
                strOut("You cannot move forwards.")

        # Moving right?
        elif(cmd == "right" or cmd == "r"):
            if(envs[player.getLoc()].getRight().strip() != "NULL"):
                strOut("You move right...")
                player.setLoc(envs[player.getLoc()].getRight())
            else:
                strOut("You cannot move right.")

        # Moving back?
        elif(cmd == "back" or cmd == "b"):
            if(envs[player.getLoc()].getBack().strip() != "NULL"):
                strOut("You move back...")
                player.setLoc(envs[player.getLoc()].getBack())
            else:
                strOut("You cannot move back.")

        # Picking up an item?
        elif(cmd[0:4] == "take"):
            player.addToInv(envs[player.getLoc()].takeItem(cmd[5:]))

        # Something else?
        else:
            strIn("'{0}' doesn't make any sense.".format(cmd))

# MAIN PROGRAM ------------------------------------------
cls()

# Load data from files
itemList = txtadvlib.loadItems("data/items.dat")
envList = txtadvlib.loadEnvs("data/environments.dat", itemList)

# Create player
player = txtadvlib.createPlayer(strIn("Please tell me your name. "))

# Welcome and introduce player to game
intro(player.getName())

# --Main loop--
playing = True
while(playing):
    # Print player status
    playerStatus(player, itemList)

    # Print current and neighbouring env descriptions
    envDesc(envList, player.getLoc())

    # Evaluate command from user
    evalCmd(strIn("\n? ").lower(), player, envList)
