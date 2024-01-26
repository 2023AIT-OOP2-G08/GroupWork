import tkinter as tk # pyenvのpythonを入れ直した
import tkinter.ttk as ttk
import urllib.request # 元から入ってるはず
import io # 元から入ってるはず
import json # 元から入ってるはず

from tkinter import messagebox # アラート用のやつ
from PIL import Image, ImageTk # pip3 install Pillowでインストール

from BaseScreen import BaseScreen # 親クラス

"""

TODO: moduleのimport
なんかうまくいかない....

from ..Processor import * # module

"""
# from ..Processor import search_books_by_authors,search_books_by_isbn,search_books_by_title
# from ..Processor 
# from BookSearchFunction import BookSearchFunction

SCREEN_SIZE = '840x1000' # 画面サイズ
FONT_TYPE = 'Helvetica' # フォント
BORDER = tk.GROOVE # 枠線
JSON_PATH = 'Bookshelf.json' # jsonのパス

class BookSearchScreen(BaseScreen):

    search_book_data = []
    def get_data(self, data):
        BookSearchScreen.search_book_data = data
        # print(self.search_book_data)


    def create_widgets(self):
        print(BookSearchScreen.search_book_data)
        

        """

        TODO: この画面の設定
        ここで設定していいのでしょうか

        """
        ### 画面設定
        self.root.title('検索ページ') # 画面タイトル
        self.root.geometry(SCREEN_SIZE) # 画面サイズ
        self.root.option_add('*font', [FONT_TYPE, 16]) # フォント

        book_search_screen_frame = self.frame


        ### タイトルフレーム
        title_frame = tk.Frame(book_search_screen_frame) 
        title_frame.pack(fill='x',pady=20)


        def trans_home_button(): # ホーム画面遷移
            """
            TODO: 元の画面に戻る(ホーム画面？？)
            windowを生成せずに遷移
            ループしないように関数内でimport

            """
           # Search画面を非表示
            self.screen_hide()

            from HH import HH # ホーム画面

            print('go home!!') # debug
            
            # Home画面インスタンス化
            home_screen = HH(self.root)
            # 画面を表示
            home_screen.screen_show()
            


        trans_home_button = tk.Button(title_frame, text='元の画面へ', command=trans_home_button)
        trans_home_button.pack(side='left')

        screen_title_label = tk.Label(title_frame, text='書籍検索', font=("Helvetica", 30, "bold"))
        screen_title_label.pack(side="left", padx=245)

        def trans_shelf_button(): # 本棚画面遷移
            """

            TODO: 本棚画面へ遷移
            windowを生成せずに遷移
            ループを防ぐため、関数内でimport

            from BookShelfScreen import BookShelfScreen # 本棚画面

            # Search画面を非表示
            self.screen_hide()

            # Shelf画面インスタンス化
            shelf_screen = BookShelfScreen(self.root)
            # 画面を表示
            shelf_screen.screen_show()

            """
            # Search画面を非表示
            self.screen_hide()
            print('go shelf!!') # debug

        trans_shelf_button = tk.Button(title_frame, text='本棚画面へ', command=trans_shelf_button)
        trans_shelf_button.pack(side='left')


        ### 検索欄フレーム
        search_frame = tk.Frame(book_search_screen_frame) 
        search_frame.pack(pady=20)

        options = ['タイトル', 'ISBN-13', '著者名']
        search_combobox = ttk.Combobox(search_frame, justify="center", values=options, state='readonly', width=10)
        search_combobox.set('タイトル')
        search_combobox.pack(side='left')

        search_lbl = tk.Label(search_frame,text='検索：')
        search_lbl.pack(side='left')

        book_search_textbox = tk.Entry(search_frame,width=50) # テキストボックス
        book_search_textbox.pack(side='left', padx=5)


        ### 検索結果フレーム
        # search_book_data = [] # 検索結果を受け取るリスト
        photos = [] # ImageTk.PhotoImageオブジェクトを保持するリスト

        # debug用 bg付き
        search_book_canvas = tk.Canvas(book_search_screen_frame, bg='green') # スクロールバーの為のキャンバス
        search_book_frame = tk.Frame(search_book_canvas,bg='red', width=840, height=10000) # 検索結果フレーム(初期設定)
        scrollbar = tk.Scrollbar( # スクロールバー
                search_book_canvas, orient=tk.VERTICAL, command=search_book_canvas.yview
            )

        frame_height = search_book_frame.winfo_reqheight() # フレームの高さを取得
        # print(frame_height) # debug
        search_book_canvas.configure(scrollregion=(0, 0, 0, frame_height)) # スクロールの設定
        search_book_canvas.configure(yscrollcommand=scrollbar.set) # スクロールバーをキャンバスに設定


        """

        TODO: タッチパッドでスクロール

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


        def detail_button(item): # 詳細を表示
            """

            TODO: DtailScreenを表示

            DtailScreen側でself.root.destroy()でwindowを消してもらっている

            itemをここから渡してしえばいいのでは....?
            ただ、今機能側で必要最低限の情報だけ抜き取ってリストにして返してるから、それを変えないといけない？
            (今はテスト用リストで全部入ってる)

            """
            # from BookDetailsScreen import BookDetailsScreen # 詳細画面

            # print(item) # debug

            # book_details_screen_root = tk.Toplevel()
            # book_details_screen = BookDetailsScreen(book_details_screen_root)
            # # book_details_screen.get_data(item)
            # book_details_screen.screen_show()

        def add_button(item): # 登録した本をjsonに保存
            """

            登録した本をjsonに保存

            moduleを使おうと思います

            # 登録した本をjsonに追加
            append_to_json(JSON_PATH, item)

            
            """
            print(item) # debug


        def search_button(): # 検索実行&結果表示
            """

            TODO: ここで検索結果を受け取る

            moduleを利用

            ### moduleで検索結果を受け取る
            if search_combobox.get() == 'タイトル' :
                search_book_data = search_books_by_title(book_search_textbox.get())
            elif search_combobox.get() == 'ISBN-13' :
                search_book_data = search_books_by_isbn(book_search_textbox.get())
            elif search_combobox.get() == 'ISBN-13' :
                search_book_data = search_books_by_authors(book_search_textbox.get())
            else :
                messagebox.showinfo('エラー', '検索方法が選択されていません')

            """

            # if search_combobox.get() == 'タイトル' :
            #     search_book_data = module.search_books_by_title(book_search_textbox.get())
            # elif search_combobox.get() == 'ISBN-13' :
            #     search_book_data = module.search_books_by_isbn(book_search_textbox.get())
            # elif search_combobox.get() == 'ISBN-13' :
            #     search_book_data = module.search_books_by_authors(book_search_textbox.get())
            # else :
            #     messagebox.showinfo('エラー', '検索方法が選択されていません')


            # test用
            print(f"「{book_search_textbox.get()}」を「{search_combobox.get()}」で検索")
            search_book_data = test_data


            ### 表を作成(grid)
            headers = ['表紙', 'タイトル', 'ISBN-13', 'Action'] # 列名
            for j, header in enumerate(headers): # header配置
                header_label = tk.Label(search_book_frame, text=header, relief=BORDER)
                header_label.grid(row=2, column=j, sticky='ew')

            for i, item in enumerate(search_book_data, start=3):  # start=1 to skip header row
                # URLから画像データをダウンロード
                with urllib.request.urlopen(item['cover_image_url']) as u:
                    raw_data = u.read()

                # ダウンロードした画像データをPIL.Imageオブジェクトに変換
                im = Image.open(io.BytesIO(raw_data))

                # 画像のサイズを半分にする
                im = im.resize((im.width // 2, im.height // 2))
                

                # PIL.Imageオブジェクトをtkinterで使用可能なImageTk.PhotoImageオブジェクトに変換
                photo = ImageTk.PhotoImage(im)
                photos.append(photo)  # 画像をリストに追加

                border_label = tk.Label(search_book_frame, relief=BORDER) # 枠線

                # ボタンに画像を設定してウィンドウに追加
                book_button = tk.Button(search_book_frame, image=photo, command=lambda item=item: detail_button(item))
                border_label.grid(row=i, column=0, sticky=tk.NSEW) # 枠線
                book_button.grid(row=i, column=0)
                
                # タイトルとISBN-13を表示
                title_label = tk.Label(search_book_frame, text=item['title'], wraplength=565, relief=BORDER)
                title_label.grid(row=i, column=1, sticky=tk.NSEW)

                isbn_label = tk.Label(search_book_frame, text=item['isbn_13'], relief=BORDER)
                isbn_label.grid(row=i, column=2, sticky=tk.NSEW)

                # 登録ボタンを追加
                register_button = tk.Button(search_book_frame, text="登録", command=lambda item=item: add_button(item))
                border_label.grid(row=i, column=3, sticky=tk.NSEW) # 枠線
                register_button.grid(row=i, column=3)
            
            ### スクロールバー
            search_book_frame.update() # フレームをアップデート

            frame_height = search_book_frame.winfo_reqheight() # フレームの高さを取得
            # print(frame_height) # debug
            search_book_canvas.configure(scrollregion=(0, 0, 0, frame_height)) # スクロールの設定
            search_book_canvas.configure(yscrollcommand=scrollbar.set)

        ### 配置
        book_search_button = tk.Button(search_frame, text="検索", command=search_button) # 検索実行ボタン
        book_search_button.pack(side="left")

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y) # スクロールバー
        search_book_canvas.pack(expand=True, fill=tk.BOTH) # キャンバス
        search_book_canvas.create_window((0, 0), window=search_book_frame, anchor="nw") # キャンバスにフレームを設置





"""

test用

この辺は遷移前の画面などに記述

"""

# テストデータ
test_data = [
    {
        "title": "情熱プログラマー ソフトウェア開発者の幸せな生き方",
        "isbn_13": "9784274067938",
        "authors": [
            "Chad Fowler"
        ],
        "published_date": "2010-02",
        "page_count": 200,
        "description": "本書は、等身大のプログラマの一人がキャリア開発の重要性を説き、そのための心構えなどを示したもの。「プログラマはビジネス視点を持って意識的なキャリア開発をすべき」という視点から、その実践方法を著者独特の生き生きとした共感できる語り口で伝える。原書は\"The Passionate Programmer: Creating a Remarkable Career in Software Development\"(The Pragmatic Programmers,2009)",
        "publisher": "株式会社 オーム社",
        "cover_image_url": "http://books.google.com/books/content?id=oFrK2r8rQbEC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
    },
    {
        "title": "ハッカーと画家",
        "isbn_13": "9784274065972",
        "authors": "No authors available",
        "published_date": "2005",
        "page_count": 284,
        "description": "天才プログラマが語る創造のセンス",
        "publisher": "株式会社 オーム社",
        "cover_image_url": "http://books.google.com/books/content?id=SinFRfuTH7IC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
    },
    {
        "title": "読みやすいコードのガイドライン -持続可能なソフトウェア開発のために",
        "isbn_13": "9784297130367",
        "authors": [
            "石川宗寿"
        ],
        "published_date": "2022-10-22",
        "page_count": 0,
        "description": "開発が大規模化・長期化するほど、コードを「読む」コストは増大していきます。そのため「読みやすさ」の向上は、生産性を改善し、プロダクトの成長限界を引き上げる重要な手段と言えるでしょう。 本書は、読みやすさの本質を学び、実践するための考え方をマスターできる一冊です。体系的な理解を実現するため、あらゆる角度から、豊富な例を交えて解説しています。表面的なテクニックではなく、いま目の前にあるコードに最適な改良方法を選び取る力が身に付きます。",
        "publisher": "No publisher information available",
        "cover_image_url": "http://books.google.com/books/content?id=uyNgzwEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
    },
    {
        "title": "リーダブルコード",
        "isbn_13": "9784873115658",
        "authors": [
            "Dustin Boswell",
            "Trevor Foucher"
        ],
        "published_date": "2012-06",
        "page_count": 237,
        "description": "読んでわかるコードの重要性と方法について解説",
        "publisher": "O'Reilly Media, Inc.",
        "cover_image_url": "http://books.google.com/books/content?id=Wx1dLwEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
    },
    {
        "title": "エンジニアのためのドキュメントライティング",
        "isbn_13": "9784800590831",
        "authors": [
            "ジャレッド・バーディ",
            "ザッカリー・サラ・コーライセン",
            "ジェン・ランボーン",
            "デービッド・ヌーニェス",
            "ハイディ・ウォーターハウス"
        ],
        "published_date": "2023-03-11",
        "page_count": 0,
        "description": "経験に長けた執筆者たちが開発者向けドキュメントの作成方法をゼロから説明するフィールドガイド",
        "publisher": "No publisher information available",
        "cover_image_url": "http://books.google.com/books/content?id=Mi-rzwEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
    },
    {
        "title": "LaTeX2e 美文書作成入門",
        "isbn_13": "9784297117122",
        "authors": [
            "奥村晴彦",
            "黒木裕介"
        ],
        "published_date": "2020-11",
        "page_count": 448,
        "description": "No description available",
        "publisher": "No publisher information available",
        "cover_image_url": "http://books.google.com/books/content?id=zDsJzgEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
    },
    {
        "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
        "isbn_13": "9784798155456",
        "authors": [
            "原田秀司"
        ],
        "published_date": "2019-01-21",
        "page_count": 210,
        "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
        "publisher": "翔泳社",
        "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
    },
    {
        "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
        "isbn_13": "9784798155456",
        "authors": [
            "原田秀司"
        ],
        "published_date": "2019-01-21",
        "page_count": 210,
        "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
        "publisher": "翔泳社",
        "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
    },
    {
        "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
        "isbn_13": "9784798155456",
        "authors": [
            "原田秀司"
        ],
        "published_date": "2019-01-21",
        "page_count": 210,
        "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
        "publisher": "翔泳社",
        "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
    },
    {
        "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
        "isbn_13": "9784798155456",
        "authors": [
            "原田秀司"
        ],
        "published_date": "2019-01-21",
        "page_count": 210,
        "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
        "publisher": "翔泳社",
        "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
    },
    {
        "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
        "isbn_13": "9784798155456",
        "authors": [
            "原田秀司"
        ],
        "published_date": "2019-01-21",
        "page_count": 210,
        "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
        "publisher": "翔泳社",
        "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
    },
    {
        "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
        "isbn_13": "9784798155456",
        "authors": [
            "原田秀司"
        ],
        "published_date": "2019-01-21",
        "page_count": 210,
        "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
        "publisher": "翔泳社",
        "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
    },
    {
        "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
        "isbn_13": "9784798155456",
        "authors": [
            "原田秀司"
        ],
        "published_date": "2019-01-21",
        "page_count": 210,
        "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
        "publisher": "翔泳社",
        "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
    },
    {
        "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
        "isbn_13": "9784798155456",
        "authors": [
            "原田秀司"
        ],
        "published_date": "2019-01-21",
        "page_count": 210,
        "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
        "publisher": "翔泳社",
        "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
    },
    {
        "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計マルチデバイス時代のインターフェース設計マルチデバイス時代のインターフェース設計マルチデバイス時代のインターフェース設計マルチデバイス時代のインターフェース設計　",
        "isbn_13": "9784798155456",
        "authors": [
            "原田秀司"
        ],
        "published_date": "2019-01-21",
        "page_count": 210,
        "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
        "publisher": "翔泳社",
        "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
    }
]

# # tkinterウィンドウを作成
# root = tk.Tk()

# # クラスをインスタンス化
# book_search_screen = BookSearchScreen(root)

# book_search_screen.get_data(test_data)

# # 画面を表示
# book_search_screen.screen_show()

# ### ウィンドウを表示
# root.mainloop()

