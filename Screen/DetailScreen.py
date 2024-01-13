import tkinter as tk

root = tk.Tk()
root.title("書籍詳細画面")
root.geometry("600x600")

label1 = tk.Label(root, text="書籍管理アプリ", font=("Helvetica", 20, "bold"))
label1.place(x=20, y=25)

label2 = tk.Label(root, text="書籍詳細画面", font=("Helvetica", 30, "bold"))
label2.place(x=207, y=20)

label3 = tk.Label(root, text="タイトル : title", font=("Helvetica", 17, "bold"))
label3.place(x=180, y=140)

label_title = tk.Label(root, text="jsonから引用(タイトル)", font=("Helvetica", 12, "bold"))
label_title.place(x=180, y=180)

label4 = tk.Label(root, text="著者 : authors", font=("Helvetica", 17, "bold"))
label4.place(x=400, y=140)

# label_authors = tk.Label(root, text="jsonから引用(著者)", font=("Helvetica", 12, "bold"))
# label_authors.place(x=400, y=180)

label5 = tk.Label(root, text="ISBN-13 : isbn_13", font=("Helvetica", 17, "bold"))
label5.place(x=180, y=240)

# label_isbn_13 = tk.Label(root, text="jsonから引用(ISBN-13)", font=("Helvetica", 12, "bold"))
# label_isbn_13.place(x=180, y=280)

label6 = tk.Label(root, text="出版社 : publisher", font=("Helvetica", 17, "bold"))
label6.place(x=400, y=240)

# label_publisher = tk.Label(root, text="jsonから引用(出版社)", font=("Helvetica", 12, "bold"))
# label_publisher.place(x=400, y=280)

label7 = tk.Label(root, text="ページ数 : page_count", font=("Helvetica", 17, "bold"))
label7.place(x=180, y=340)

# label_page_count = tk.Label(root, text="jsonから引用(ページ数)", font=("Helvetica", 12, "bold"))
# label_page_count.place(x=180, y=380)

label8 = tk.Label(root, text="出版日 : published_date", font=("Helvetica", 17, "bold"))
label8.place(x=400, y=340)

# label_published_date = tk.Label(root, text="jsonから引用(出版日)", font=("Helvetica", 12, "bold"))
# label_published_date.place(x=400, y=380)

label9 = tk.Label(root, text="要約 : description", font=("Helvetica", 17, "bold"))
label9.place(x=50, y=440)

# label_description = tk.Label(root, text="jsonから引用(要約)", font=("Helvetica", 12, "bold"))
# label_description.place(x=50, y=480)

root.mainloop()
