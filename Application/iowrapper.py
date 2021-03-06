# ------iowrapper--------
# Xander Lewis - 09/08/14
# -----------------------
# This is a temporary placeholder for the tkinter GUI wrapper which will be capable of
# text input, text output, and maybe some other stuff like showing a visual inventory.
# Eventually this will be overwritten with the GUI wrapper, but the same strOut and
# strIn functions will exist. (But they will control a graphical window)

def strOut(pString):
    """Prints passed string to console."""
    # Print passed string
    print(pString)

def strIn(prompt):
    """Prints passed string and takes user input from console."""
    # Print prompt and return user input
    return input(prompt)
