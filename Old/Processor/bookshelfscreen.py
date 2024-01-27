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
    #input_list お気に入りした本を格納しているlist 既存のlist
    #index 削除するデータのindexnumber
    #削除機能の時使える
    input_list.pop(index)

    return input_list

def add_information(input_list, new_list):
    #データを追加するプログラム
    #input_list お気に入りした本を格納しているlist 既存のlist
    #新しく追加するデータnew_list(list)
    input_list.append(new_list)
    return input_list



def append_to_json(json_file_path, info_list):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

        #リスト形式で追加
    new_data = {
        'title': info_list[0],
        'isbn_13': info_list[1],
        'authors': info_list[2],
        'published_date': info_list[3],
        'page_count': info_list[4],
        'description': info_list[5],
        'publisher': info_list[6],
        'cover_image_url': info_list[7]
    }

    data.update(new_data)

    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

#-------------------------------------------------------------------------------#
# 例として、json_file_pathとinfo_listを適当に設定
json_file_path = 'Bookshelf.json'
info_list = ['test', '1234567', ['Author'], '2024-01-18', 200, 'New book description', 'Publisher', 'https://example.com/cover.jpg']

# 関数を呼び出してJSONファイルに追加
append_to_json(json_file_path, info_list)
