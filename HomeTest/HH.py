import tkinter as tk
#from PIL import Image, ImageTk
from BaseScreen import BaseScreen


class HH(BaseScreen):

    def create_widgets(self):

        def on_book_search_screen_button_click():
            
            """

            hideの位置はここじゃないとちゃんと消えてくれない
            ループしないために、importはこの位置
            画面遷移するだけの時は、windowを作らないので、self.rootを直接書き換える
            
            """

            self.screen_hide()

            from BookSearchScreen import BookSearchScreen

            book_search_screen = BookSearchScreen(self.root)
            book_search_screen.screen_show()

        def on_book_shelf_screen_button_click():
            # メインウィンドウを非表示にする
            self.screen_hide()

            # from BookShelfScreen import BookShelfScreen

            # book_shelf_screen = BookShelfScreen(self.root)
            # book_shelf_screen.screen_show()


        # フォントの設定
        title_name = ("書籍管理アプリ")    # タイトル名指定
        title_font = ("Helvetica", 15, "bold")   # タイトルのフォントとサイズを指定
        button_font = ("Helvetica", 50, "bold")  # ボタンのフォントとサイズを指定

        self.root.geometry(
            "800x500" # アプリ画面のサイズ
        )
        self.root.title(
            title_name # アプリのタイトル
        )

        title_label = tk.Label(self.frame, text=title_name, font=title_font)
        title_label.pack(padx=10, pady=10, anchor=tk.NW)

        # ボタンの作成
        book_search_screen_button = tk.Button(self.frame, text="検索画面", command=on_book_search_screen_button_click,font=button_font)
        book_shelf_screen_button = tk.Button(self.frame, text="本棚画面", command=on_book_shelf_screen_button_click,font=button_font)


        # ボタンを配置
        book_search_screen_button.pack(side=tk.LEFT)
        book_shelf_screen_button.pack(side=tk.RIGHT)

# # メインウィンドウの作成
# root = tk.Tk()

# a = HH(root)

# a.screen_show()

# # イベントループの開始
# root.mainloop()