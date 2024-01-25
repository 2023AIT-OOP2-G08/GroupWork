# -*- coding:utf-8 -*-
import tkinter as tk
from PIL import Image, ImageTk
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

def on_resize(event):
    # ウィンドウのサイズが変更された時の処理
    book_search_screen_button.place(x=root.winfo_width()/3-book_search_screen_button.winfo_reqwidth()/2, y=root.winfo_height()/2+image_label1.winfo_reqheight()/2)
    book_shelf_screen_button.place(x=root.winfo_width()*2/3-book_shelf_screen_button.winfo_reqwidth()/2, y=root.winfo_height()/2+image_label2.winfo_reqheight()/2)
    image_label1.place(x=root.winfo_width()/3-image_label1.winfo_reqwidth()/2, y=root.winfo_height()/2-image_label1.winfo_reqheight()/2)
    image_label2.place(x=root.winfo_width()*2/3-image_label2.winfo_reqwidth()/2, y=root.winfo_height()/2-image_label2.winfo_reqheight()/2)

    

# フォントの設定
title_name = ("書籍管理アプリ")    # タイトル名指定
title_font = ("Helvetica", 15, "bold")   # タイトルのフォントとサイズを指定
button_font = ("Helvetica", 50)  # ボタンのフォントとサイズを指定

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


# 画像1の読み込みと表示
image_path1 = "booksearch_image.png"
original_image1 = Image.open(image_path1)
resized_image1 = original_image1.resize((250, 250), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.LANCZOS)
tk_image1 = ImageTk.PhotoImage(resized_image1)
image_label1 = tk.Label(root, image=tk_image1)
image_label1.place(x=root.winfo_width()/3-image_label1.winfo_reqwidth()/2, y=root.winfo_height()/2-image_label1.winfo_reqheight()/2)

# 画像2の読み込みと表示
image_path2 = "bookshelf_image.png"
original_image2 = Image.open(image_path2)
resized_image2 = original_image2.resize((250, 250), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.LANCZOS)
tk_image2 = ImageTk.PhotoImage(resized_image2)
image_label2 = tk.Label(root, image=tk_image2)
image_label2.place(x=root.winfo_width()*2/3-image_label2.winfo_reqwidth()/2, y=root.winfo_height()/2-image_label2.winfo_reqheight()/2)

# 画像がクリックされたときの処理を設定
image_label1.bind("<Button-1>", lambda event: on_book_search_screen_button_click())
image_label2.bind("<Button-1>", lambda event: on_book_shelf_screen_button_click())


# ウィンドウのサイズ変更イベントを監視
root.bind("<Configure>", on_resize)


# ボタンの作成
book_search_screen_button = tk.Button(root, text="検索", command=on_book_search_screen_button_click,font=button_font)
book_shelf_screen_button = tk.Button(root, text="本棚", command=on_book_shelf_screen_button_click,font=button_font)

# ボタンを配置
#book_search_screen_button.pack(side=tk.LEFT, padx=root.winfo_width()/4)
#book_shelf_screen_button.pack(side=tk.RIGHT, padx=root.winfo_width()/4)
book_search_screen_button.place(x=root.winfo_width()/3-book_search_screen_button.winfo_reqwidth()/2, y=root.winfo_height()/2+image_label1.winfo_reqheight()/2)
book_shelf_screen_button.place(x=root.winfo_width()*2/3-book_shelf_screen_button.winfo_reqwidth()/2, y=root.winfo_height()/2+image_label2.winfo_reqheight()/2)


# イベントループの開始
root.mainloop()
