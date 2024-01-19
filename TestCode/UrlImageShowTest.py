#url形式の画像を表示するプログラム


import tkinter as tk #pyenvのpythonを入れ直した
#pyenv uninstall 3.11.5
#pyenv install 3.11.5
#pyenvとpythonのバージョン確認

from PIL import Image, ImageTk
import urllib.request
import io

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
