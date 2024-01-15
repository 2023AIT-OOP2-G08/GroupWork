import json

def bookshelfscreen(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:  #jsonファイルを開ける

        data = json.load(file) #dataにjsonファイルの情報を代入
        info_list = [ #listに画像、タイトル、JSBNの順に情報を代入
            data.get("cover_image_url", ""),
            data.get("title", ""),
            data.get("isbn_13", "")
        ]

    return info_list #リストを返す

