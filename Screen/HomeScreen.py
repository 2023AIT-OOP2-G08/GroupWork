import tkinter as tk
#from PIL import Image, ImageTk
from BookSearchScreen import BookSearchScreen
from BookShelfScreen import BookShelfScreen


def on_book_search_screen_button_click():
    # メインウィンドウを非表示にする
    root.withdraw()

    # 新しいウィンドウを作成
    book_search_screen_root = tk.Toplevel()
    book_search_screen = BookSearchScreen(book_search_screen_root, root)

def on_book_shelf_screen_button_click():
    # メインウィンドウを非表示にする
    root.withdraw()

    # 新しいウィンドウを作成
    book_shelf_screen_root = tk.Toplevel()
    book_shelf_screen = BookShelfScreen(book_shelf_screen_root, root)
    
# フォントの設定
title_name = ("書籍管理アプリ")    # タイトル名指定
title_font = ("Helvetica", 15, "bold")   # タイトルのフォントとサイズを指定
button_font = ("Helvetica", 50, "bold")  # ボタンのフォントとサイズを指定

# メインウィンドウの作成
root = tk.Tk()
root.geometry(
    "800x500" # アプリ画面のサイズ
)
root.title(
    title_name # アプリのタイトル
)

title_label = tk.Label(root, text=title_name, font=title_font)
title_label.pack(padx=10, pady=10, anchor=tk.NW)

# ボタンの作成
book_search_screen_button = tk.Button(root, text="検索", command=on_book_search_screen_button_click,font=button_font)
book_shelf_screen_button = tk.Button(root, text="本棚", command=on_book_shelf_screen_button_click,font=button_font)


# ボタンを配置
book_search_screen_button.pack(side=tk.LEFT, padx=root.winfo_width()/4)
book_shelf_screen_button.pack(side=tk.RIGHT, padx=root.winfo_width()/4)


# イベントループの開始
root.mainloop()
