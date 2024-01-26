import tkinter as tk
from HomeScreen import HomeScreen # ホーム画面

def main () :

    root =  tk.Tk() # 最初のroot window作成

    starting_screen = HomeScreen(root) # HomeScreenをインスタンス化

    starting_screen.screen_show() # HomeScreenの画面を設定

    root.mainloop() # イベントループ


if __name__ == '__main__':
    main()