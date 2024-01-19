#書籍の画像、タイトル、ISBN、登録ボタンの順にgridで表示するプログラム
#それぞれのセルを区切るグリッド線の表示が微妙セルのサイズを固定すれば綺麗に線画描画できるかも

import tkinter as tk #pyenvのpythonを入れ直した
#pyenv uninstall 3.11.5
#pyenv install 3.11.5
#pyenvとpythonのバージョン確認

from PIL import Image, ImageTk
import urllib.request
import io

"""
#tk._test()
print("tkinter:",tk.TkVersion)

print("Pillow version:", Image.__version__)

url = 'http://books.google.com/books/content?id=Wx1dLwEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api'

# URLから画像データをダウンロード
with urllib.request.urlopen(url) as u:
    raw_data = u.read()

# ダウンロードした画像データをPIL.Imageオブジェクトに変換
im = Image.open(io.BytesIO(raw_data))

# tkinterウィンドウを作成
root = tk.Tk()

# PIL.Imageオブジェクトをtkinterで使用可能なImageTk.PhotoImageオブジェクトに変換
photo = ImageTk.PhotoImage(im)

# ラベルに画像を設定してウィンドウに追加
label = tk.Label(root, image=photo)
label.pack()

# ウィンドウを表示
root.mainloop()
"""

# テストデータ
data = [
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
    }
]

# tkinterウィンドウを作成
root = tk.Tk()

# ImageTk.PhotoImageオブジェクトを保持するリスト
photos = []

# 列名を表示
headers = ['Image', 'Title', 'ISBN-13', 'Action']
for j, header in enumerate(headers):
    header_label = tk.Label(root, text=header, relief=tk.RIDGE)
    header_label.grid(row=0, column=j, sticky='ew')

for i, item in enumerate(data, start=1):  # start=1 to skip header row
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

    # ボタンに画像を設定してウィンドウに追加
    # 登録ボタンを押した時押した行のデータを出力
    button = tk.Button(root, image=photo, command=lambda item=item: print(item))
    button.grid(row=i, column=0)

    # タイトルとISBN-13を表示
    title_label = tk.Label(root, text=item['title'], relief=tk.RIDGE)
    title_label.grid(row=i, column=1)

    isbn_label = tk.Label(root, text=item['isbn_13'], relief=tk.RIDGE)
    isbn_label.grid(row=i, column=2)

    # 登録ボタンを追加
    # 登録ボタンを押した時押した行のデータを出力
    register_button = tk.Button(root, text="登録", command=lambda item=item: print(item))
    register_button.grid(row=i, column=3)

# ウィンドウを表示
root.mainloop()
