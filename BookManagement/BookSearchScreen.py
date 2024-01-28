import tkinter as tk # pyenvのpythonを入れ直した
import tkinter.ttk as ttk # GUI用のものを色々提供
from tkinter import messagebox # アラートなどを表示できる
import urllib.request # urlを読み込める
import io # いろんなI/Oを使える 
import os # パスを取得できる

from PIL import Image, ImageTk # pip3 install Pillowでインストール

from BaseScreen import BaseScreen # 親クラス
import Processor # module


"""

windowの設定値

画面サイズ、フォントは固定
ホームスクリーンで設定されてればいいのでは？

"""
SCREEN_SIZE = '840x1000' # 画面サイズ
FONT_TYPE = 'Helvetica' # フォント
BORDER = tk.GROOVE # 枠線


"""

パスを取得

"""
# カレントディレクトリを取得
current_directory = os.path.dirname(os.path.abspath(__file__))

# 絶対パスを作成
NO_IMAGE_PATH = os.path.join(current_directory, 'Images/no_img.png')
SHELF_JSON_PATH = os.path.join(current_directory, 'Bookshelf.json')


class BookSearchScreen(BaseScreen):

    photos = [] # 検索画像保存用リスト

    def create_widgets(self):
        """

        ウィジェットの作成
        (BaseScreenのオーバーライド)

        """
        ### 画面設定
        self.root.geometry(SCREEN_SIZE) # 画面サイズ
        self.root.option_add('*font', [FONT_TYPE, 16]) # フォント

        book_search_screen_frame = self.frame # 全体のframeを設置


        ### タイトルフレーム
        title_frame = tk.Frame(book_search_screen_frame) 
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

        screen_title_label = tk.Label(title_frame, text='書籍検索', font=("Helvetica", 30, "bold"))
        screen_title_label.pack(side="left", padx=236) # 真ん中の文字

        def on_trans_shelf_button_click(): # 本棚画面遷移
            """

            本棚画面へ遷移

            windowを生成せずに遷移
            ループを防ぐため、関数内でimport

            """
            self.screen_hide() # Search画面を非表示

            from BookshelfScreen import Bookshelfscreen # 本棚画面
            
            shelf_screen = Bookshelfscreen(self.root) # 本棚画面インスタンス化
            shelf_screen.screen_show() # 本棚画面を表示

        trans_shelf_button = tk.Button(title_frame, text='本棚画面へ', command=on_trans_shelf_button_click)
        trans_shelf_button.pack(side='left') # 本棚画面遷移ボタン


        ### 検索欄フレーム
        search_frame = tk.Frame(book_search_screen_frame) 
        search_frame.pack(pady=20)

        options = ['タイトル', 'ISBN-13', '著者名'] # 検索方法の選択肢
        search_combobox = ttk.Combobox(search_frame, justify="center", values=options, state='readonly', width=10)
        search_combobox.set('タイトル') # 初期設定
        search_combobox.pack(side='left')

        search_lbl = tk.Label(search_frame,text='検索：') # ラベル
        search_lbl.pack(side='left')

        book_search_textbox = tk.Entry(search_frame,width=50) # テキストボックス
        book_search_textbox.pack(side='left', padx=5)


        ### 検索結果の表フレーム
        search_result_table_canvas = tk.Canvas(book_search_screen_frame) # スクロールバーの為のキャンバス
        search_result_table_frame = tk.Frame(search_result_table_canvas, width=840, height=1200, bd=2, relief=BORDER) # 検索結果フレーム(初期設定)
        scrollbar = tk.Scrollbar(search_result_table_canvas, orient=tk.VERTICAL, command=search_result_table_canvas.yview) # スクロールバー
        # debug用 bg='green', bg='red'
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

            詳細画面を表示

            ループしないように関数内にimport
            DtailScreen側でself.root.destroy()でwindowを消してもらっている

            itemをここから渡す。

            """
            from BookDetailsScreen import BookDetailsScreen # 詳細画面

            # print(item) # debug

            book_details_screen_root = tk.Toplevel() # window作成
            book_details_screen = BookDetailsScreen(book_details_screen_root, item) # screenをwindowに設定
            book_details_screen.screen_show() # screenを表示

        def on_add_button_click(item): # 登録した本をjsonに保存
            """

            登録した本をjsonに保存
            (moduleを利用)

            """
            # print(item) # debug

            if not Processor.is_list_in_json_file(SHELF_JSON_PATH, item) : # 登録されていなければ

                yes_no_result = messagebox.askyesno("確認", "本棚に登録しますか？")
                if yes_no_result: # yes が選択されたら追加
                    Processor.append_to_json(SHELF_JSON_PATH, item)

            else : # 既に登録されていたら
                messagebox.showinfo('エラー', 'すでに登録されています。')

        def on_book_search_button_click(): # 検索実行&結果表示
            """
            
            検索を実行し、結果を表示する

            tableをまず、初期化する
            moduleを利用し、検索結果を受け取る
            その後、表として配置する

            """

            ### 初期化
            for widget in search_result_table_frame.winfo_children(): # table_frame内のすべての子ウィジェットを破棄
                widget.destroy()
            BookSearchScreen.photos = [] # 検索結果の画像を初期化


            ### 検索
            if search_combobox.get() == 'タイトル' : # タイトル検索
                search_book_data = Processor.search_books_by_title(book_search_textbox.get())
            elif search_combobox.get() == 'ISBN-13' : #ISBN-13検索
                search_book_data = Processor.search_books_by_isbn(book_search_textbox.get())
            elif search_combobox.get() == '著者名' : # 著者名検索
                search_book_data = Processor.search_books_by_authors(book_search_textbox.get())
            else :
                messagebox.showinfo('エラー', '検索方法が選択されていません')

             # print(f"「{book_search_textbox.get()}」を「{search_combobox.get()}」で検索") # debug


            if search_book_data != 'No books found': # 本が見つかった場合
                # print(search_book_data) # debug
                """

                表の作成

                gridで作成

                """
                headers = ['表紙', 'タイトル', 'ISBN-13', 'Action'] # 列名
                for j, header in enumerate(headers): # header配置
                    header_label = tk.Label(search_result_table_frame, text=header, relief=BORDER)
                    header_label.grid(row=0, column=j, sticky='ew')
                
                for i, item in enumerate(search_book_data, start=1): # 表の要素配置(row=3から)

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
                    BookSearchScreen.photos.append(photo)  # 画像をリストに追加

                    # ボタンに画像を設定
                    book_border_label = tk.Label(search_result_table_frame, relief=BORDER) # 枠線
                    book_button = tk.Button(search_result_table_frame, image=photo, command=lambda item=item: on_detail_button_click(item))
                    book_border_label.grid(row=i, column=0, sticky=tk.NSEW) # 枠線
                    book_button.grid(row=i, column=0)
                    
                    # タイトル & ISBN-13
                    table_title_label = tk.Label(search_result_table_frame, text=item['title'], relief=BORDER, wraplength=450, width=57)
                    table_title_label.grid(row=i, column=1, sticky=tk.NSEW)

                    isbn_label = tk.Label(search_result_table_frame, text=item['isbn_13'], relief=BORDER, wraplength=100, width=15)
                    isbn_label.grid(row=i, column=2, sticky=tk.NSEW)

                    # 登録ボタン
                    button_border_label = tk.Label(search_result_table_frame, relief=BORDER, width=10) # 枠線
                    register_button = tk.Button(search_result_table_frame, text="登録", command=lambda item=item: on_add_button_click(item))
                    button_border_label.grid(row=i, column=3, sticky=tk.NSEW) # 枠線
                    register_button.grid(row=i, column=3)
                
                ### スクロールバー
                search_result_table_frame.update() # フレームの最新情報更新
                frame_height = search_result_table_frame.winfo_reqheight() # フレームの高さを取得
                # print(frame_height) # debug
                search_result_table_canvas.configure(scrollregion=(0, 0, 0, frame_height)) # スクロールの設定
                search_result_table_canvas.configure(yscrollcommand=scrollbar.set) # スクロールの設定

            else : # 本が見つからなかった場合
                """

                No books foundを出す。

                """
                no_book_label = tk.Label(search_result_table_frame, text=search_book_data, font=("Helvetica", 20, "bold"))
                no_book_label.pack(ipadx=340, pady=20, anchor="center")


        ### 配置
        book_search_button = tk.Button(search_frame, text="検索", command=on_book_search_button_click) # 検索実行ボタン
        book_search_button.pack(side="left")
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y) # スクロールバー
        search_result_table_canvas.pack(expand=True, fill=tk.BOTH) # キャンバス
        search_result_table_canvas.create_window((0, 0), window=search_result_table_frame, anchor="nw") # キャンバスにフレームを設置

        frame_height = search_result_table_frame.winfo_reqheight() # フレームの高さを取得
        search_result_table_canvas.configure(scrollregion=(0, 0, 0, frame_height)) # スクロールの設定
        search_result_table_canvas.configure(yscrollcommand=scrollbar.set) # スクロールの設定





"""

test用

この辺は遷移前の画面などに記述

"""
if __name__ == '__main__':

    root = tk.Tk() # tkinterウィンドウを作成

    book_search_screen = BookSearchScreen(root) # クラスをインスタンス化

    book_search_screen.screen_show() # 画面を設定

    root.mainloop() # イベントループ

