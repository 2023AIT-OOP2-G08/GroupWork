import tkinter
from tkinter import ttk  # ttkモジュールからTreeViewをインポート
# from PIL import Image, ImageTk # 画像表示ライブラリ


### 画面遷移用(簡易的)
def show_book_search_screen():
    book_search_screen.pack(fill="both",expand=True)
    screen_b.pack_forget()

def show_screen_b():
    book_search_screen.pack_forget()
    screen_b.pack()

### Tkクラス生成
root = tkinter.Tk()
# 画面サイズ
root.geometry('800x500')
# 画面タイトル
root.title('検索ページ')

# スクリーンのフレーム
book_search_screen = tkinter.Frame(root)
book_search_screen.pack(fill="both",expand=True)

# 画面遷移ボタン
trans_button = tkinter.Button(book_search_screen, text="本棚画面へ", command=show_screen_b)
trans_button.pack(anchor='ne')

# ラベル
lbl = tkinter.Label(book_search_screen,text='書籍検索')
lbl.pack(side="top")


### 検索欄
# 検索欄のフレーム
search_frame = tkinter.Frame(book_search_screen) 
search_frame.pack()

lbl = tkinter.Label(search_frame,text='検索ボックス:')
lbl.pack(side="left")

#　テキストボックス
book_search_textbox = tkinter.Entry(search_frame,width=20)
book_search_textbox.pack(side="left")

#ボタン
def add_button():
    # print(txt.get()) # debug
    search_result_table.insert(parent='',index='end',values=(4,'TEST4',book_search_textbox.get()))

book_search_button = tkinter.Button(search_frame, text="検索", command=add_button)
book_search_button.pack(side="left")


### 表
search_result_table = ttk.Treeview(book_search_screen, column=('COVER','TITLE','CODE','BUTTON'), show='headings')

# スクロールバー
scrollbar = ttk.Scrollbar(book_search_screen, orient="vertical", command=search_result_table.yview)
search_result_table.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# 表のヘッダー
search_result_table.heading('COVER',text='表紙')
search_result_table.heading('TITLE',text='タイトル')
search_result_table.heading('CODE',text='ISBN-13')
search_result_table.heading('BUTTON',text='登録ボタン')

# 表のデータ
search_result_table.insert(parent='',index='end',values=(1,'TEST1','テスト1'))
search_result_table.insert(parent='',index='end',values=(2,'TEST2','テスト2'))
search_result_table.insert(parent='',index='end',values=(3,'TEST3','テスト3'))
search_result_table.insert(parent='',index='end',values=(1,'TEST1','テスト1'))
search_result_table.insert(parent='',index='end',values=(2,'TEST2','テスト2'))
search_result_table.insert(parent='',index='end',values=(3,'TEST3','テスト3'))
search_result_table.insert(parent='',index='end',values=(1,'TEST1','テスト1'))
search_result_table.insert(parent='',index='end',values=(2,'TEST2','テスト2'))
search_result_table.insert(parent='',index='end',values=(3,'TEST3','テスト3'))
search_result_table.insert(parent='',index='end',values=(1,'TEST1','テスト1'))
search_result_table.insert(parent='',index='end',values=(2,'TEST2','テスト2'))
search_result_table.insert(parent='',index='end',values=(3,'TEST3','テスト3'))
search_result_table.insert(parent='',index='end',values=(1,'TEST1','テスト1'))
search_result_table.insert(parent='',index='end',values=(2,'TEST2','テスト2'))
search_result_table.insert(parent='',index='end',values=(3,'TEST3','テスト3'))
search_result_table.insert(parent='',index='end',values=(1,'TEST1','テスト1'))
search_result_table.insert(parent='',index='end',values=(2,'TEST2','テスト2'))
search_result_table.insert(parent='',index='end',values=(3,'TEST3','テスト3'))
search_result_table.insert(parent='',index='end',values=(1,'TEST1','テスト1'))
search_result_table.insert(parent='',index='end',values=(2,'TEST2','テスト2'))
search_result_table.insert(parent='',index='end',values=(3,'TEST3','テスト3'))
search_result_table.insert(parent='',index='end',values=(1,'TEST1','テスト1'))
search_result_table.insert(parent='',index='end',values=(2,'TEST2','テスト2'))
search_result_table.insert(parent='',index='end',values=(3,'TEST3','テスト3'))
search_result_table.insert(parent='',index='end',values=(1,'TEST1','テスト1'))
search_result_table.insert(parent='',index='end',values=(2,'TEST2','テスト2'))
search_result_table.insert(parent='',index='end',values=(3,'TEST3','テスト3'))
search_result_table.insert(parent='',index='end',values=(1,'TEST1','テスト1'))
search_result_table.insert(parent='',index='end',values=(2,'TEST2','テスト2'))
search_result_table.insert(parent='',index='end',values=(3,'TEST3','テスト3'))


search_result_table.pack(side="bottom",fill="both",expand=True)

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


# スクリーンBのフレーム
screen_b = tkinter.Frame(root)
screen_b.pack()

label_b = tkinter.Label(screen_b, text="ScreenB")
label_b.pack()

button_b = tkinter.Button(screen_b, text="To A", command=show_book_search_screen)
button_b.pack()

# 最初はスクリーンAを表示
show_book_search_screen()

# 表示
root.mainloop()

