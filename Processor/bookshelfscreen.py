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

def remove_index_elements(input_list, index):
    #指定したindexのlistを削除する
    #input_list お気に入りした本を格納しているlist
    #constant 削除するデータのindexnumber
    input_list.pop(index)
    return input_list