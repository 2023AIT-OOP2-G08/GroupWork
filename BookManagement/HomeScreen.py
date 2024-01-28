# -*- coding:utf-8 -*-
import tkinter as tk # pyenvでpythonを入れ直した
import os # パスを作れる

from PIL import Image, ImageTk # pip3 install Pillowでインストール
from BaseScreen import BaseScreen # 親クラス

"""

windowの設定値

画面サイズ、フォント、タイトルは固定

"""
TITLE_NAME = '書籍管理アプリ' # windowタイトル
SCREEN_SIZE = '840x1000' # 画面サイズ
FONT_TYPE = 'Helvetica' # フォント

"""

パスを取得

"""
# カレントディレクトリを取得
current_directory = os.path.dirname(os.path.abspath(__file__))

# 絶対パスを作成
BOOK_SEARCH_IMAGE_PATH = os.path.join(current_directory, 'Images/book_search_img.png')
BOOK_SHELF_IMAGE_PATH = os.path.join(current_directory, 'Images/book_shelf_img.png')


class HomeScreen(BaseScreen):

    photos = [] # 検索画像保存用リスト

    def create_widgets(self):
        """
        
        ウィジェットの作成
        (BaseScreenのオーバーライド)
        
        """

        def on_book_search_screen_button_click():
            
            """

            検索画面へ遷移

            hideの位置はここじゃないとちゃんと消えてくれない
            ループしないために、importはこの位置
            画面遷移するだけの時は、windowを作らないので、self.rootを直接書き換える
            
            """

            self.screen_hide()

            from BookSearchScreen import BookSearchScreen

            book_search_screen = BookSearchScreen(self.root)
            book_search_screen.screen_show()

        def on_book_shelf_screen_button_click():
            """

            本棚画面へ遷移

            hideの位置はここじゃないとちゃんと消えてくれない
            ループしないために、importはこの位置
            画面遷移するだけの時は、windowを作らないので、self.rootを直接書き換える
            
            """

            self.screen_hide()

            from BookshelfScreen import BookshelfScreen

            book_shelf_screen = BookshelfScreen(self.root)
            book_shelf_screen.screen_show()


        ### 画面設定
        self.root.geometry(SCREEN_SIZE) # window size
        self.root.title(TITLE_NAME) # window title name

        title_font = ("Helvetica", 50, "bold")   # タイトルのフォントとサイズを指定
        button_font = ("Helvetica", 50, "bold")  # ボタンのフォントとサイズを指定


        # 画面上のタイトル
        title_label = tk.Label(self.frame, text='ホーム', font=title_font)
        title_label.pack(padx=10, pady=100, anchor=tk.N)
        
        # 画像のダウンロード
        img_1 = Image.open(BOOK_SEARCH_IMAGE_PATH)
        img_2 = Image.open(BOOK_SHELF_IMAGE_PATH)

        # 画像サイズ変更
        img_1 = img_1.resize((img_1.width // 4, img_1.height // 4))
        img_2 = img_2.resize((img_2.width // 4, img_2.height // 4))
        
        # ImageTk.PhotoImageオブジェクトに変換
        search_photo = ImageTk.PhotoImage(img_1) 
        self_photo = ImageTk.PhotoImage(img_2) 

        # 画像をリストに追加
        HomeScreen.photos.append(search_photo) 
        HomeScreen.photos.append(self_photo) 

        # ボタンの作成
        book_search_screen_button = tk.Button(self.frame, text="検索画面", compound=tk.TOP, image=search_photo, command=on_book_search_screen_button_click, font=button_font)
        book_shelf_screen_button = tk.Button(self.frame, text="本棚画面", compound=tk.TOP, image=self_photo, command=on_book_shelf_screen_button_click, font=button_font)

        # ボタンを配置
        book_search_screen_button.pack(side=tk.LEFT, padx=30)
        book_shelf_screen_button.pack(side=tk.RIGHT, padx=30)

        """

        過去のやつ

        ウィンドウサイズは固定が仕様なので、リサイズに対応しなくても大丈夫です！
        (対応してもいいです)


        def on_resize(event): # ウィンドウのサイズが変更された時の処理

            book_search_screen_button.place(x=self.root.winfo_width()/3-book_search_screen_button.winfo_reqwidth()/2, y=root.winfo_height()/2+image_label1.winfo_reqheight()/2)
            book_shelf_screen_button.place(x=self.root.winfo_width()*2/3-book_shelf_screen_button.winfo_reqwidth()/2, y=root.winfo_height()/2+image_label2.winfo_reqheight()/2)
            image_label1.place(x=self.root.winfo_width()/3-image_label1.winfo_reqwidth()/2, y=self.root.winfo_height()/2-image_label1.winfo_reqheight()/2)
            image_label2.place(x=self.root.winfo_width()*2/3-image_label2.winfo_reqwidth()/2, y=self.root.winfo_height()/2-image_label2.winfo_reqheight()/2)

        # 画像1の読み込みと表示
        image_path1 = "book_search_img.png"
        original_image1 = Image.open(image_path1)
        resized_image1 = original_image1.resize((250, 250), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.LANCZOS)
        tk_image1 = ImageTk.PhotoImage(resized_image1)
        image_label1 = tk.Label(self.root, image=tk_image1)
        image_label1.place(x=self.root.winfo_width()/3-image_label1.winfo_reqwidth()/2, y=root.winfo_height()/2-image_label1.winfo_reqheight()/2)

        # 画像2の読み込みと表示
        image_path2 = "book_shelf_img.png"
        original_image2 = Image.open(image_path2)
        resized_image2 = original_image2.resize((250, 250), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.LANCZOS)
        tk_image2 = ImageTk.PhotoImage(resized_image2)
        image_label2 = tk.Label(self.root, image=tk_image2)
        image_label2.place(x=self.root.winfo_width()*2/3-image_label2.winfo_reqwidth()/2, y=root.winfo_height()/2-image_label2.winfo_reqheight()/2)

        # 画像がクリックされたときの処理を設定
        image_label1.bind("<Button-1>", lambda event: on_book_search_screen_button_click())
        image_label2.bind("<Button-1>", lambda event: on_book_shelf_screen_button_click())


        # ウィンドウのサイズ変更イベントを監視
        self.root.bind("<Configure>", on_resize)

        # ボタンを配置
        book_search_screen_button.pack(side=tk.LEFT, padx=root.winfo_width()/4)
        book_shelf_screen_button.pack(side=tk.RIGHT, padx=root.winfo_width()/4)
        book_search_screen_button.place(x=self.root.winfo_width()/3-book_search_screen_button.winfo_reqwidth()/2, y=root.winfo_height()/2+image_label1.winfo_reqheight()/2)
        book_shelf_screen_button.place(x=self.root.winfo_width()*2/3-book_shelf_screen_button.winfo_reqwidth()/2, y=root.winfo_height()/2+image_label2.winfo_reqheight()/2)

        """



"""

test用

"""
if __name__ == '__main__':
    root = tk.Tk() # window作成

    screen = HomeScreen(root) # インスタンス化

    screen.screen_show() # screenを設定

    root.mainloop() # イベントループ