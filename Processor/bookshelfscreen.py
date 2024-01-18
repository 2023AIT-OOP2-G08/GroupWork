import json


def bookshelfscreen(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:  #jsonファイルを開ける

        data = json.load(file) #dataにjsonファイルの情報を代入
        info_list = [ 
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

def remove_constant_elements(input_list, constant):
    #指定したindexのlistを削除する
    return [ input_list[:constant] + input_list[constant + 1:]]
