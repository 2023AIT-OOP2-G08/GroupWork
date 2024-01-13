import tkinter
from tkinter import ttk  # ttkモジュールからTreeViewをインポート
# from PIL import Image, ImageTk # 画像表示ライブラリ


# Tkクラス生成
root = tkinter.Tk()
# 画面サイズ
root.geometry('500x300')
# 画面タイトル
root.title('検索ページ')

# ラベル
lbl = tkinter.Label(text='検索')
lbl.pack()

### テキストボックス
txt = tkinter.Entry(width=20)
txt.pack()

###ボタン
# クリックしたときに実行する関数
def button_click():
    # print(txt.get()) # debug
    tree.insert(parent='',index='end',values=(4,'TEST4',txt.get(),button))

# ボタン
button = tkinter.Button(root, text="ボタン", command=button_click)
button.pack()

### 表
tree = ttk.Treeview(root, column=('COVER','TITLE','CODE','BUTTON'), show='headings')

# 表のヘッダー
tree.heading('COVER',text='表紙')
tree.heading('TITLE',text='タイトル')
tree.heading('CODE',text='ISBN-13')
tree.heading('BUTTON',text='登録ボタン')

# 表のデータ
tree.insert(parent='',index='end',values=(1,'TEST1','テスト1',button.pack()))
tree.insert(parent='',index='end',values=(2,'TEST2','テスト2',button.pack()))
tree.insert(parent='',index='end',values=(3,'TEST3','テスト3',button.pack()))

tree.pack()

### 画像
# # 画像の読み込み
# image_path = "https://ja.pngtree.com/freepng/small-url-icon-opened-on-the-computer_4424025.html"  # 画像のパスを指定してください
# original_image = Image.open(image_path)

# # 画像をリサイズ（適宜、ウィンドウサイズに合わせるなど）
# resized_image = original_image.resize((300, 200), Image.ANTIALIAS)

# # 画像をTkinter PhotoImageオブジェクトに変換
# tk_image = ImageTk.PhotoImage(resized_image)

# # 画像をラベルに表示
# image_label = tkinter.Label(root, image=tk_image)
# image_label.pack()



# 表示
root.mainloop()

