import tkinter as tk
from tkinter import Scrollbar, Text
from PIL import Image, ImageTk
import urllib.request
import io
import textwrap
from BaseScreen import BaseScreen

SCREEN_SIZE = "600x600"  # 画面サイズ
FONT_TYPE = "Helvetica"  # フォント


class BookDetailsScreen(BaseScreen):
    outside_data = {}  # 書籍情報を受け取るリスト

    # print(data_list)

    def __init__(self, root: tk.Tk, data=None):
        """
        ウィンドウの基底クラスを初期化します。

        Parameters:
        - root: Tkinterウィンドウの親オブジェクト
        """
        BookDetailsScreen.outside_data = data
        self.root = root
        self.frame = tk.Frame(root)
        self.create_widgets()

    # def get_data(self, data):
    #     BookDetailsScreen.outside_data = data
    #     # print(BookDetailsScreen.outside_data)

    def create_widgets(self):
        data_list = BookDetailsScreen.outside_data

        # 著者名が表記されていて配列でリストに格納されている場合
        # 要素の間に改行を加えて一つの文に変換する
        if data_list["authors"] != "No publisher information available":
            data_list["authors"] = "\n".join(data_list["authors"])

        # 画面タイトル
        self.root.title("書籍詳細画面")
        # 画面サイズ
        self.root.geometry(SCREEN_SIZE)

        # タイトルの作成
        label2 = tk.Label(self.frame, text="書籍詳細画面", font=(FONT_TYPE, 30, "bold"))
        label2.place(x=207, y=20)

        # 表紙の画像表示
        url = data_list["cover_image_url"]

        # URLから画像データをダウンロード
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()

        # ダウンロードした画像データをPIL.Imageオブジェクトに変換
        im = Image.open(io.BytesIO(raw_data))

        # PIL.Imageオブジェクトをtkinterで使用可能なImageTk.PhotoImageオブジェクトに変換
        self.photo = ImageTk.PhotoImage(im)

        # ラベルに画像を設定してウィンドウに追加
        label_photo = tk.Label(self.frame, image=self.photo)
        label_photo.place(x=20, y=140)

        # 項目ごとのラベルの作成
        # タイトルの項目名、jsonから得た情報の表示ラベル
        label3 = tk.Label(self.frame, text="タイトル : ", font=(FONT_TYPE, 17, "bold"))
        label3.place(x=180, y=140)

        label_title = tk.Label(
            self.frame,
            text=("\n".join(data_list["title"].split())),
            font=(FONT_TYPE, 12, "bold"),
        )
        label_title.place(x=180, y=180)

        # 著者の項目名、jsonから得た情報の表示ラベル
        label4 = tk.Label(self.frame, text="著者 : ", font=(FONT_TYPE, 17, "bold"))
        label4.place(x=400, y=140)

        label_authors = tk.Label(
            self.frame, text=data_list["authors"], font=(FONT_TYPE, 12, "bold")
        )
        label_authors.place(x=400, y=180)

        # ISBN-13の項目名、jsonから得た情報の表示ラベル
        label5 = tk.Label(self.frame, text="ISBN-13 : ", font=(FONT_TYPE, 17, "bold"))
        label5.place(x=180, y=240)

        label_isbn_13 = tk.Label(
            self.frame, text=data_list["isbn_13"], font=(FONT_TYPE, 12, "bold")
        )
        label_isbn_13.place(x=180, y=280)

        # 出版社の項目名、jsonから得た情報の表示ラベル
        label6 = tk.Label(self.frame, text="出版社 : ", font=(FONT_TYPE, 17, "bold"))
        label6.place(x=400, y=240)

        label_publisher = tk.Label(
            self.frame, text=data_list["publisher"], font=(FONT_TYPE, 12, "bold")
        )
        label_publisher.place(x=400, y=280)

        # ページ数の項目名、jsonから得た情報の表示ラベル
        label7 = tk.Label(self.frame, text="ページ数 : ", font=(FONT_TYPE, 17, "bold"))
        label7.place(x=180, y=340)

        label_page_count = tk.Label(
            self.frame, text=data_list["page_count"], font=(FONT_TYPE, 12, "bold")
        )
        label_page_count.place(x=180, y=380)

        # 出版日の項目名、jsonから得た情報の表示ラベル
        label8 = tk.Label(self.frame, text="出版日 : ", font=(FONT_TYPE, 17, "bold"))
        label8.place(x=400, y=340)

        label_published_date = tk.Label(
            self.frame,
            text=data_list["published_date"],
            font=(FONT_TYPE, 12, "bold"),
        )
        label_published_date.place(x=400, y=380)

        # 要約の項目名、jsonから得た情報の表示ラベル
        label9 = tk.Label(self.frame, text="要約 : ", font=(FONT_TYPE, 17, "bold"))
        label9.place(x=50, y=440)

        # jsonから得た要約の情報を表示するTextウィジェットを作成
        description_text = tk.Text(self.frame, wrap="none", width=69, height=8)
        description_text.pack(side="left", fill="both", expand=True)
        description_text.place(x=50, y=480)

        # スクロール用
        # def on_scroll(*args):
        #     description_text.yview(*args)

        """# スクロールバーを作成
        scrollbar = tk.Scrollbar(root, command=on_scroll)
        scrollbar.pack(side="right", fill="y")

        # スクロールバーとTextウィジェットを関連付ける
        text.config(yscrollcommand=scrollbar.set)"""

        # 要約を40文字ごとで改行
        description_data = textwrap.fill(data_list["description"], 40)
        # print(type(data_list[5]))
        # テキストを追加
        for ch in description_data:
            description_text.insert("end", ch)

        # 画面遷移(書籍詳細画面のウィンドウを閉じる)
        def close_window():
            self.root.destroy()

        # 画面遷移用のボタン
        close_button = tk.Button(self.frame, text="前の画面へ", command=close_window)
        close_button.pack()
        close_button.place(x=20, y=80)


# test_list = {
#     "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
#     "isbn_13": "9784798155456",
#     "authors": ["原田秀司"],
#     "published_date": "2019-01-21",
#     "page_count": 210,
#     "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
#     "publisher": "翔泳社",
#     "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
# }

# # tkinterウィンドウを作成
# root = tk.Tk()

# # クラスをインスタンス化
# book_details_screen = BookDetailsScreen(root, data=outside_data)

# # 画面を表示
# book_details_screen.screen_show()

# ### ウィンドウを表示
# root.mainloop()