import tkinter as tk # pyenvのpythonを入れ直した
from tkinter import messagebox # アラートなどを表示できる
import urllib.request # urlを読み込める
import io # いろんなI/Oを使える 
import os # パスを取得できる
import Processor.BookshelfFunction as BookshelfFunction

from BaseScreen import BaseScreen # 親クラス
from PIL import Image, ImageTk # pip3 install Pillowでインス
import Processor


"""

パスを取得

"""
# スクリプトのディレクトリパスを取得
current_directory = os.path.dirname(os.path.abspath(__file__))
NO_IMAGE_PATH = os.path.join(current_directory, 'Images/no_img.png')
SHELF_JSON_PATH = os.path.join(current_directory, 'Bookshelf.json')


"""

windowの設定値

画面サイズ、フォントは固定
ホームスクリーンで設定されてればいいのでは？

"""
SCREEN_SIZE = '840x1000' # 画面サイズ
FONT_TYPE = 'Helvetica' # フォント
BORDER = tk.GROOVE # 枠線


class BookshelfScreen(BaseScreen):

    photos = [] # 本画像保存用リスト
    input_data = {}  # 更新されるリストをクラスに用意

    def create_widgets(self):
        """

        ウィジェットの作成
        (BaseScreenのオーバーライド)

        """
        ### 画面設定
        self.root.geometry(SCREEN_SIZE) # 画面サイズ
        self.root.option_add('*font', [FONT_TYPE, 16]) # フォント

        book_self_screen_frame = self.frame # 全体のframeを設置


        ### タイトルフレーム
        title_frame = tk.Frame(book_self_screen_frame) 
        title_frame.pack(fill='x',pady=20)

        def on_trans_home_button_click(): # ホーム画面遷移
            """

            ホーム画面へ遷移

            windowを生成せずに遷移
            ループしないように関数内でimport

            """
            self.screen_hide() # Search画面を非表示

            from HomeScreen import HomeScreen # ホーム画面
            
            home_screen = HomeScreen(self.root) # Home画面インスタンス化
            home_screen.screen_show() # 画面を表示
            
        trans_home_button = tk.Button(title_frame, text='ホーム画面へ', command=on_trans_home_button_click)
        trans_home_button.pack(side='left') # ホーム画面遷移ボタン

        screen_title_label = tk.Label(title_frame, text='My本棚', font=("Helvetica", 30, "bold"))
        screen_title_label.pack(side="left", padx=236) # 真ん中の文字

        def on_trans_search_button_click(): # 検索画面遷移
            """

            検索画面へ遷移

            windowを生成せずに遷移
            ループを防ぐため、関数内でimport

            """
            self.screen_hide() # Search画面を非表示

            from BookSearchScreen import BookSearchScreen # 本棚画面
            
            search_screen = BookSearchScreen(self.root) # 本棚画面インスタンス化
            search_screen.screen_show() # 本棚画面を表示

        trans_shelf_button = tk.Button(title_frame, text='検索画面へ', command=on_trans_search_button_click)
        trans_shelf_button.pack(side='left') # 本棚画面遷移ボタン


        ### 表のフレーム
        # debug用bg付き
        bookself_table_canvas = tk.Canvas(book_self_screen_frame) # スクロールバーの為のキャンバス
        bookself_table_frame = tk.Frame(bookself_table_canvas, width=840, height=0) # 検索結果フレーム(初期設定)
        scrollbar = tk.Scrollbar(bookself_table_canvas, orient=tk.VERTICAL, command=bookself_table_canvas.yview) # スクロールバー

        """

        TODO: トラックパッドでスクロール

        優先度はだいぶ低いが、ないと操作しずらい

        
        ↓動かないやつ(残してあるだけ)
        def on_canvas_scroll(event): # タッチパッドでスクロール
            # macOS上でのマウスホイールスクロールイベントに対応
            if event.num == 5 or event.delta == -120:
                search_book_canvas.yview_scroll(1, "units")
            elif event.num == 4 or event.delta == 120:
                search_book_canvas.yview_scroll(-1, "units")

        # スクロールイベントをCanvasにバインドする
        search_book_canvas.bind("<MouseWheel>", on_canvas_scroll)
        search_book_canvas.bind("<Button-4>", on_canvas_scroll)  # Linux対応
        search_book_canvas.bind("<Button-5>", on_canvas_scroll)  # Linux対応

        """


        def on_detail_button_click(item): # 詳細を表示
            """

            DtailScreenを表示

            ループしないように関数内にimport
            DtailScreen側でself.root.destroy()でwindowを消してもらっている

            itemをここから渡す。

            """
            from BookDetailsScreen import BookDetailsScreen # 詳細画面

            # print(item) # debug

            book_details_screen_root = tk.Toplevel() # window作成
            book_details_screen = BookDetailsScreen(book_details_screen_root, item) # screenをwindowに設定
            book_details_screen.screen_show() # screenを表示

        """
        
        TODO: 追加機能(余裕があれば）
        
        お気に入りボタン

        お気に入りの本を実装する場合に、
        下の関数のpathを変えて、もう一つjsonを作ればもう一つお気に入りの本の本棚を作れると思います。
        これを実装する可能性見越し、pathはmoduleで作るのではなく、こちらで指定する形にすることをお勧めします。
        ↓↓↓↓↓↓
        """
        # def on_add_button_click(item): # 登録した本をjsonに保存
        #     """

        #     登録した本をjsonに保存
        #     (moduleを利用)

        #     """
        #     # print(item) # debug

        #     if Processor.is_list_in_json_file(SHELF_JSON_PATH, item) : # 既に登録されていたら
        #         messagebox.showinfo('エラー', 'すでに登録されています。')
        #     else : # 登録されていなければ追加
        #         Processor.append_to_json(SHELF_JSON_PATH, item)


        def on_delete_button_click(item, index): # 本棚から削除
            """

            本棚から削除
            
            listの中身と、json内のデータを消す。

            """

            yes_no_result = messagebox.askyesno("確認", "本棚から削除しますか？")
            if yes_no_result:  # yes が選択されたら削除
                # BookshelfFunction.remove_index_elements を呼び出し、削除後のデータを取得
                BookshelfScreen.input_data = Processor.remove_index_elements(
                    SHELF_JSON_PATH, BookshelfScreen.input_data, index - 1
                )

            update_table()  # 画面の更新を行う関数を呼び出す

        def update_table():
            """

            表の更新

            初期化して、再設定

            """
            # dataの受け取り
            bookself_data = BookshelfScreen.input_data 
            # print(bookself_data) # debug

            ### 初期化
            for widget in bookself_table_frame.winfo_children(): # table_frame内のすべての子ウィジェットを破棄
                widget.destroy()
            BookshelfScreen.photos = [] # 検索結果の画像を初期化

            headers = ['表紙', 'タイトル', 'ISBN-13', 'Action'] # 列名
            for j, header in enumerate(headers): # header配置
                header_label = tk.Label(bookself_table_frame, text=header, relief=BORDER)
                header_label.grid(row=0, column=j, sticky='ew')
            
            for i, item in enumerate(bookself_data, start=1): # 表の要素配置(row=3から)

                # 画像のダウンロード
                if item['cover_image_url'] != 'No cover image available': # 画像がある場合
                    with urllib.request.urlopen(item['cover_image_url']) as u:
                        raw_data = u.read() # urlから画像をダウンロード
                    im = Image.open(io.BytesIO(raw_data)) # ダウンロードした画像データをPIL.Imageオブジェクトに変換
                    im = im.resize((im.width // 2, im.height // 2)) # 画像サイズ変更
                
                else: # 画像がない場合
                    im = Image.open(NO_IMAGE_PATH) # no_imgをダウンロード
                    im = im
                
                photo = ImageTk.PhotoImage(im) # ImageTk.PhotoImageオブジェクトに変換
                BookshelfScreen.photos.append(photo)  # 画像をリストに追加

                # ボタンに画像を設定
                book_border_label = tk.Label(bookself_table_frame, relief=BORDER) # 枠線
                book_button = tk.Button(bookself_table_frame, image=photo, command=lambda item=item: on_detail_button_click(item))
                book_border_label.grid(row=i, column=0, sticky=tk.NSEW) # 枠線
                book_button.grid(row=i, column=0)
                
                # タイトル & ISBN-13
                table_title_label = tk.Label(bookself_table_frame, text=item['title'], relief=BORDER, wraplength=450, width=57)
                table_title_label.grid(row=i, column=1, sticky=tk.NSEW)

                isbn_label = tk.Label(bookself_table_frame, text=item['isbn_13'], relief=BORDER, wraplength=100, width=15)
                isbn_label.grid(row=i, column=2, sticky=tk.NSEW)

                # 削除ボタン
                button_border_label = tk.Label(bookself_table_frame, relief=BORDER, width=10) # 枠線
                register_button = tk.Button(bookself_table_frame, text="削除", command=lambda item=item, i=i: on_delete_button_click(item, i))
                button_border_label.grid(row=i, column=3, sticky=tk.NSEW) # 枠線
                register_button.grid(row=i, column=3)
            
            ### スクロールバー
            bookself_table_frame.update() # フレームの最新情報更新
            frame_height = bookself_table_frame.winfo_reqheight() # フレームの高さを取得
            # print(frame_height) # debug
            bookself_table_canvas.configure(scrollregion=(0, 0, 0, frame_height)) # スクロールの設定
            bookself_table_canvas.configure(yscrollcommand=scrollbar.set) # スクロールの設定

        """

        諸々の配置

        """

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y) # スクロールバー
        bookself_table_canvas.pack(expand=True, fill=tk.BOTH) # キャンバス
        bookself_table_canvas.create_window((0, 0), window=bookself_table_frame, anchor="nw") # キャンバスにフレームを設置

        # 最初に一度jsonを読み込む
        BookshelfScreen.input_data = BookshelfFunction.get_bookshelf(SHELF_JSON_PATH)
        update_table() # 最初に呼んでおく。





"""

test用

この辺は遷移前の画面などに記述

"""
if __name__ == '__main__':


    root = tk.Tk() # tkinterウィンドウを作成

    book_self_screen = BookshelfScreen(root) # クラスをインスタンス化

    book_self_screen.screen_show() # 画面を設定

    root.mainloop() # イベントループ