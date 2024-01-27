import tkinter as tk
import Processor
from Screen import HomeScreen
import json

def main () :
    root =  tk.Tk()
    processor = Processor()  
    starting_screen = HomeScreen(root, processor)
    #starting_screen = HomeScreen(root)
    root.mainloop()


if __name__ == '__main__':
    main()