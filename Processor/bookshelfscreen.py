import json

__all__ = ['bookshelfscreen']

def bookshelfscreen(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:  #jsonファイルを開ける

        data = json.load(file) #dataにjsonファイルの情報を代入
        info_list = [ #listに画像、タイトル、JSBNの順に情報を代入
            data['title'],
            data['isbn_13'],
            data['authors'],
            data['published_date'],
            data['page_count'],
            data['description'],
            data['publisher'],
            data['cover_image_url']
            ]

    return info_list #リストを返す

