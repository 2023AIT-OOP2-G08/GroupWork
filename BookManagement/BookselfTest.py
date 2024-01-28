import tkinter as tk # pyenvのpythonを入れ直した
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


class BookshelfTest(BaseScreen):

    photos = [] # 本画像保存用リスト


    """

    TODO: case1
    なにもいらない

    TODO: case2
    更新されるリストをクラスに用意しなければいけない
    input_data = {} など

    """

    def create_widgets(self):
        """

        ウィジェットの作成
        (BaseScreenのオーバーライド)

        """
        
        """

        TODO: テストデータなので、最後は消してください。

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
            }
        ]



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
        bookself_table_canvas = tk.Canvas(book_self_screen_frame, bg='green') # スクロールバーの為のキャンバス
        bookself_table_frame = tk.Frame(bookself_table_canvas,bg='red', width=840, height=0) # 検索結果フレーム(初期設定)
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

            TODO: case1
            itemを受け取って、json内のデータを消す。
            検索画面と似たような実装ならば、ここではjson内のデータを消し、表を更新するだけ
            (重そう、update_table内でmoduleからリストを毎回受け取る。)

            TODO: case2
            item&何かを受け取って、listの中身と、json内のデータを消す。
            indexの取得がわからない...
            (こっちの方が軽そう、update_table内で、リストを更新するだけ)

            消す作業自体は同じくらいだが、case2だとjsonを読み込むという工程が一度で済む。
            (一つだけ消す時にmoduleで全部読み込んでたらおなじかも)

            """
            # # 指定されたインデックスの本を削除
            # Processor.remove_index_elements(item, index - 3)  # -3 は enumerate で start=3 を指定しているため

            # 削除後に再描画などの更新が必要な場合はここで行う
            update_table()  # 画面の更新を行う関数を呼び出す

        def update_table():
            """

            表の更新

            初期化して、再設定

            """

            """

            TODO: case1
            ここで、リストを受け取る
            moduleを利用し、リストを受け取る。
            bookself_data = bookself_data = Processor.get_bookshelf

            TODO: case2
            classに用意されているリストの中身は既に変わっているので、
            classのinput_dataをこの関数のbookself_dataにいれればいい。
            bookself_data = BookselfTest.input_data
            だけでいい

            ↓↓↓↓↓これはtest用
            """
            bookself_data = test_data # test用

            ### 初期化
            for widget in bookself_table_frame.winfo_children(): # table_frame内のすべての子ウィジェットを破棄
                widget.destroy()
            BookshelfTest.photos = [] # 検索結果の画像を初期化

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
                BookshelfTest.photos.append(photo)  # 画像をリストに追加

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
                register_button = tk.Button(bookself_table_frame, text="削除", command=lambda item=item: on_delete_button_click(item))
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

        update_buttonはtest用です。
        最後は消してください。

        """

        update_button = tk.Button(book_self_screen_frame, text="表の更新", command=update_table) # debug
        update_button.pack() # debug

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y) # スクロールバー
        bookself_table_canvas.pack(expand=True, fill=tk.BOTH) # キャンバス
        bookself_table_canvas.create_window((0, 0), window=bookself_table_frame, anchor="nw") # キャンバスにフレームを設置

        """

        TODO: case1
        なにもいらない

        TODO: case2
        jsonをここで読み込む
        (input_dataに)
        
        """

        update_table() # 最初に呼んでおく。





"""

test用

この辺は遷移前の画面などに記述

"""
if __name__ == '__main__':


    root = tk.Tk() # tkinterウィンドウを作成

    book_self_screen = BookshelfTest(root) # クラスをインスタンス化

    book_self_screen.screen_show() # 画面を設定

    root.mainloop() # イベントループ

