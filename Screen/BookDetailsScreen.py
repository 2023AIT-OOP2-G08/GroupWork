import tkinter as tk
from PIL import Image, ImageTk
import urllib.request
import io
import textwrap

data_list = [
    "情熱プログラマー ソフトウェア開発者の幸せな生き方",
    "9784274067938",
    "No publisher information available",
    "2010-02",
    200,
    '本書は、等身大のプログラマの一人がキャリア開発の重要性を説き、そのための心構えなどを示したもの。「プログラマはビジネス視点を持って意識的なキャリア開発をすべき」という視点から、その実践方法を著者独特の生き生きとした共感できる語り口で伝える。原書は"The Passionate Programmer: Creating a Remarkable Career in Software Development"(The Pragmatic Programmers,2009)',
    "株式会社 オーム社",
    "http://books.google.com/books/content?id=oFrK2r8rQbEC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
]

if data_list[2] != "No publisher information available":
    data_list[2] = "\n".join(data_list[2])

# Tkクラス生成
root = tk.Tk()

# 画面タイトル
root.title("書籍詳細画面")

# 画面サイズ
root.geometry("600x600")

# タイトルの作成
label1 = tk.Label(root, text="書籍管理アプリ", font=("Helvetica", 20, "bold"))
label1.place(x=20, y=25)

label2 = tk.Label(root, text="書籍詳細画面", font=("Helvetica", 30, "bold"))
label2.place(x=207, y=20)


# 表紙の画像表示
url = data_list[7]

# URLから画像データをダウンロード
with urllib.request.urlopen(url) as u:
    raw_data = u.read()

# ダウンロードした画像データをPIL.Imageオブジェクトに変換
im = Image.open(io.BytesIO(raw_data))

# PIL.Imageオブジェクトをtkinterで使用可能なImageTk.PhotoImageオブジェクトに変換
photo = ImageTk.PhotoImage(im)

# ラベルに画像を設定してウィンドウに追加
label_photo = tk.Label(root, image=photo)
label_photo.pack()
label_photo.place(x=20, y=140)


# 項目ごとのラベルの作成
# (label3〜9までの下のメッセージに変換させたものは、jsonから得た情報を
# 出力する際のコード)

label3 = tk.Label(root, text="タイトル : title", font=("Helvetica", 17, "bold"))
label3.place(x=180, y=140)

label_title = tk.Label(
    root, text=("\n".join(data_list[0].split())), font=("Helvetica", 12, "bold")
)
label_title.place(x=180, y=180)

label4 = tk.Label(root, text="著者 : authors", font=("Helvetica", 17, "bold"))
label4.place(x=400, y=140)

label_authors = tk.Label(root, text=(data_list[2]), font=("Helvetica", 12, "bold"))
label_authors.place(x=400, y=180)

label5 = tk.Label(root, text="ISBN-13 : isbn_13", font=("Helvetica", 17, "bold"))
label5.place(x=180, y=240)

label_isbn_13 = tk.Label(root, text=data_list[1], font=("Helvetica", 12, "bold"))
label_isbn_13.place(x=180, y=280)

label6 = tk.Label(root, text="出版社 : publisher", font=("Helvetica", 17, "bold"))
label6.place(x=400, y=240)

label_publisher = tk.Label(root, text=data_list[6], font=("Helvetica", 12, "bold"))
label_publisher.place(x=400, y=280)

label7 = tk.Label(root, text="ページ数 : page_count", font=("Helvetica", 17, "bold"))
label7.place(x=180, y=340)

label_page_count = tk.Label(root, text=data_list[4], font=("Helvetica", 12, "bold"))
label_page_count.place(x=180, y=380)

label8 = tk.Label(root, text="出版日 : published_date", font=("Helvetica", 17, "bold"))
label8.place(x=400, y=340)

label_published_date = tk.Label(root, text=data_list[3], font=("Helvetica", 12, "bold"))
label_published_date.place(x=400, y=380)

label9 = tk.Label(root, text="要約 : description", font=("Helvetica", 17, "bold"))
label9.place(x=50, y=440)

label_description = tk.Label(
    root, text=(textwrap.fill(data_list[5], 40)), font=("Helvetica", 12, "bold")
)
label_description.place(x=50, y=480)

# メインループ実行
root.mainloop()
