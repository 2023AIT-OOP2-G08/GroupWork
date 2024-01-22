import tkinter
from tkinter import ttk  # ttkモジュールからTreeViewをインポート
# from PIL import Image, ImageTk # 画像表示ライブラリ

class BookShelfScreen(BaseScreen):
    def __init__(self, root: tk.Tk):
        # BaseScreenクラスのコンストラクタを呼び出す
        super().__init__(root)

    def create_widgets(self):
        # create_widgetsメソッドをオーバーライドしてBookShelfScreenのウィジェットを定義する
        label2 = tk.Label(self.frame, text="本棚画面", font=("Helvetica", 20, "bold"))
        label2.place(x=250, y=20)

        tbl = ttk.Treeview(self.frame)
        tbl.place(x=50, y=80)

        tbl['columns'] = ('cover', 'title', 'number', 'button')
        tbl['show'] = 'headings'
        tbl.heading('cover', text='表紙')
        tbl.heading('title', text='タイトル')
        tbl.heading('number', text='ISBN-13')
        tbl.heading('button', text='削除ボタン')

        tbl.column('cover', width=150)
        tbl.column('title', width=100)
        tbl.column('number', width=100)
        tbl.column('button', width=100)

        tbl.insert('', 'end', values=('本A', '本Aタイトル', '本Aコード', '削除'))

        tbl.bind('<ButtonRelease-1>', lambda event: self.delete_item(tbl))  # tblを引数にしてdelete_itemメソッドを呼び出す

    def delete_item(self, tbl):
        selected_item = tbl.selection()
        if selected_item:
            tbl.delete(selected_item)

# Tkクラス生成
root = tk.Tk()

# 画面タイトル
root.title("書籍管理アプリ")

# 画面サイズ
root.geometry("800x500")

# BookShelfScreenクラスのインスタンスを作成
bookshelf_screen = BookShelfScreen(root)

# BookShelfScreenを表示
bookshelf_screen.screen_show()

# メインループ実行
root.mainloop()
