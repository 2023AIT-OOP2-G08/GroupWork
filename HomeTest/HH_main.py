import tkinter as tk

from BookSearchScreen import BookSearchScreen
from HH import HH

root = tk.Tk()

a = HH(root)

a.screen_show()

# イベントループの開始
root.mainloop()