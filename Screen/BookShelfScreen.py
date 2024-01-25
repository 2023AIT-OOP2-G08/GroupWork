import tkinter as tk
from tkinter import ttk

#削除ボタンを押したときにその行を一斉削除
def delete_item():
    selected_item = tbl.selection()
    if selected_item:
        tbl.delete(selected_item)

# Tkクラス生成
root = tk.Tk()

# 画面タイトル
root.title("書籍管理アプリ")

# 画面サイズ
root.geometry("800x500")

#タイトルの作成
label1 = tk.Label(root, text="書籍管理アプリ", font=("Helvetica", 15, "bold"))
label1.place(x=20, y=25)

label2 = tk.Label(root, text="本棚画面", font=("Helvetica", 20, "bold"))
label2.place(x=250, y=20)

# 表をインスタンス化
tbl = ttk.Treeview(root)
#表の配置
tbl.place(x=50, y=80)

# 列を作成
tbl['columns'] = ('cover', 'title', 'number', 'button')

# ヘッダーの設定
tbl['show'] = 'headings'
tbl.heading('cover', text='表紙')
tbl.heading('title', text='タイトル')
tbl.heading('number', text='ISBN-13')
tbl.heading('button', text='削除ボタン')

# 各列の幅を設定
tbl.column('cover', width=150)
tbl.column('title', width=100)
tbl.column('number', width=100)
tbl.column('button', width=100)

# データ設定
tbl.insert('', 'end', values=('本A', '本Aタイトル', '本Aコード', '削除'))

# ボタンクリック時の動作を設定
tbl.bind('<ButtonRelease-1>', lambda event: delete_item())

# メインループ実行
root.mainloop()
