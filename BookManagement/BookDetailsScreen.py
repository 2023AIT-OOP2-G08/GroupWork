import tkinter as tk
from tkinter import Scrollbar, Text
import tkinter.font as tkFont
from PIL import Image, ImageTk
import urllib.request
import io
import os
import textwrap
from BaseScreen import BaseScreen

SCREEN_SIZE = "600x600"  # 画面サイズ
FONT_TYPE = "Helvetica"  # フォント
NO_IMAGE_PATH = os.path.join("Images", "no_img.png")  # no_imgの相対パス


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

        if data_list["cover_image_url"] != "No cover image available":  # 画像がある場合
            with urllib.request.urlopen(data_list["cover_image_url"]) as u:
                raw_data = u.read()  # urlから画像をダウンロード
                im = Image.open(
                    io.BytesIO(raw_data)
                )  # ダウンロードした画像データをPIL.Imageオブジェクトに変換

        else:  # 画像がない場合
            im = Image.open(NO_IMAGE_PATH)  # no_imgをダウンロード
            im = im.resize((126, 126))  # 画像サイズ変更

        # PIL.Imageオブジェクトをtkinterで使用可能なImageTk.PhotoImageオブジェクトに変換
        self.photo = ImageTk.PhotoImage(im)

        # ラベルに画像を設定してウィンドウに追加
        photo_label = tk.Label(self.frame, image=self.photo)
        photo_label.place(x=20, y=140)

        # 項目ごとのラベルの作成
        # タイトルの項目名の表示ラベル
        title_label = tk.Label(self.frame, text="タイトル : ", font=(FONT_TYPE, 17, "bold"))
        title_label.place(x=180, y=140)

        # jsonから得たタイトルの情報を表示するTextウィジェットを作成
        title_text = tk.Text(self.frame, wrap="none", width=30, height=4)
        title_text.pack(side="left", fill="both", expand=True)
        # テキストを追加
        title_data = textwrap.fill(data_list["title"], 17)
        for ch in title_data:
            title_text.insert("end", ch)

        title_font = tkFont.Font(family=FONT_TYPE, size=10)
        title_text.configure(font=title_font)
        title_text.place(x=180, y=180)

        # 著者の項目名の表示ラベル
        authors_label = tk.Label(self.frame, text="著者 : ", font=(FONT_TYPE, 17, "bold"))
        authors_label.place(x=400, y=140)

        # jsonから得た著者名の情報を表示するTextウィジェットを作成
        authors_text = tk.Text(self.frame, wrap="none", width=30, height=4)
        authors_text.pack(side="left", fill="both", expand=True)
        # テキストを追加
        authors_data = textwrap.fill(data_list["authors"], 17)
        for ch in authors_data:
            authors_text.insert("end", ch)

        authors_font = tkFont.Font(family=FONT_TYPE, size=10)
        authors_text.configure(font=authors_font)
        authors_text.place(x=400, y=180)

        # ISBN-13の項目名の表示ラベル
        isbn_13_label = tk.Label(
            self.frame, text="ISBN-13 : ", font=(FONT_TYPE, 17, "bold")
        )
        isbn_13_label.place(x=180, y=240)

        # jsonから得たISBN-13の情報を表示するTextウィジェットを作成
        isbn_13_text = tk.Text(self.frame, wrap="none", width=30, height=4)
        isbn_13_text.pack(side="left", fill="both", expand=True)
        # テキストを追加
        isbn_13_data = textwrap.fill(data_list["isbn_13"], 17)
        for ch in isbn_13_data:
            isbn_13_text.insert("end", ch)

        isbn_13_font = tkFont.Font(family=FONT_TYPE, size=10)
        isbn_13_text.configure(font=isbn_13_font)
        isbn_13_text.place(x=180, y=280)

        # 出版社の項目名の表示ラベル
        publisher_label = tk.Label(
            self.frame, text="出版社 : ", font=(FONT_TYPE, 17, "bold")
        )
        publisher_label.place(x=400, y=240)

        # jsonから得た出版社の情報を表示するTextウィジェットを作成
        publisher_text = tk.Text(self.frame, wrap="none", width=30, height=4)
        publisher_text.pack(side="left", fill="both", expand=True)
        # テキストを追加
        publisher_data = textwrap.fill(data_list["publisher"], 17)
        for ch in publisher_data:
            publisher_text.insert("end", ch)

        publisher_font = tkFont.Font(family=FONT_TYPE, size=10)
        publisher_text.configure(font=publisher_font)
        publisher_text.place(x=400, y=280)

        # ページ数の項目名の表示ラベル
        page_count_label = tk.Label(
            self.frame, text="ページ数 : ", font=(FONT_TYPE, 17, "bold")
        )
        page_count_label.place(x=180, y=340)

        # jsonから得たページ数の情報を表示するTextウィジェットを作成
        page_count_text = tk.Text(self.frame, wrap="none", width=30, height=4)
        page_count_text.pack(side="left", fill="both", expand=True)
        # テキストを追加
        page_count_text.insert("end", data_list["page_count"])

        page_count_font = tkFont.Font(family=FONT_TYPE, size=10)
        page_count_text.configure(font=page_count_font)
        page_count_text.place(x=180, y=380)

        # 出版日の項目名の表示ラベル
        published_date_label = tk.Label(
            self.frame, text="出版日 : ", font=(FONT_TYPE, 17, "bold")
        )
        published_date_label.place(x=400, y=340)

        # jsonから得た出版日の情報を表示するTextウィジェットを作成
        published_date_text = tk.Text(self.frame, wrap="none", width=30, height=4)
        published_date_text.pack(side="left", fill="both", expand=True)
        # テキストを追加
        published_date_data = textwrap.fill(data_list["published_date"], 17)
        for ch in published_date_data:
            published_date_text.insert("end", ch)

        published_date_font = tkFont.Font(family=FONT_TYPE, size=10)
        published_date_text.configure(font=published_date_font)
        published_date_text.place(x=400, y=380)

        # 要約の項目名、jsonから得た情報の表示ラベル
        label_description = tk.Label(
            self.frame, text="要約 : ", font=(FONT_TYPE, 17, "bold")
        )
        label_description.place(x=50, y=440)

        # jsonから得た要約の情報を表示するTextウィジェットを作成
        description_text = tk.Text(self.frame, wrap="none", width=69, height=7)
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

        description_font = tkFont.Font(family=FONT_TYPE, size=12)
        description_text.configure(font=description_font)

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
#     "authors": [
#         "ジャレッド・バーディ",
#         "ザッカリー・サラ・コーライセン",
#         "ジェン・ランボーン",
#         "デービッド・ヌーニェス",
#         "ハイディ・ウォーターハウス",
#     ],
#     "published_date": "2019-01-21",
#     "page_count": 210,
#     "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
#     "publisher": "翔泳社",
#     "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
# }

# # tkinterウィンドウを作成
# root = tk.Tk()

# # クラスをインスタンス化
# book_details_screen = BookDetailsScreen(root, data=test_list)

# # 画面を表示
# book_details_screen.screen_show()

# ### ウィンドウを表示
# root.mainloop()
