import json

def is_list_in_json_file(list):
    """
    指定されたリストの'title'または'isbn_13'がJSONファイルに含まれているかを確認します。

    Parameters:
    list (list): 確認するリスト。各要素は'title'と'isbn_13'をキーとする辞書

    Returns:
    bool: リストの全ての要素の'title'または'isbn_13'がJSONファイルに含まれている場合はTrue、そうでない場合はFalse。
    """
    try:
        # JSONファイルを読み込む、すでに作成されているBookshelfFunction.pyのget_bookshelf(json_file_path)でもいい
        with open('../Bookshelf.json', 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            
            for book in list:
                for data_item in json_data:
                    # リストの要素の'title'または'isbn_13'がJSONファイルに含まれている場合は次の要素を確認する
                    if book.get('title') in data_item.values():
                        return True
                    #titleがない場合はisbn_13で確認する
                    elif book.get('isbn_13') in data_item.values():
                        return True
                else:
                    return False
    except FileNotFoundError:
        return False
    
# テスト用
if __name__ == '__main__':
    list = [
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
        }
    ]
    print(is_list_in_json_file(list))