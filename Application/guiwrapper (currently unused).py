from tkinter import *

# -------guiwrapper------
# Xander Lewis - 21/07/14
# -----------------------

class Window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.title("Environment")
        self.pack(fill = BOTH, expand = 1)

        # Widgets: -------------------
        outputText = Text(self, width = 50, height = 27).place(x = 5, y = 5)
        inputText = Entry(self, width = 57).place(x = 5, y = 446)
        enterButton = Button(self, width = 6).place(x = 355, y = 444)


        self.pack()

def main():
    root = Tk()
    root.geometry("600x470+300+300")
    root.resizable(width=FALSE, height=FALSE)
    app = Window(root)
    root.mainloop()

if __name__ == "__main__":
    main()
