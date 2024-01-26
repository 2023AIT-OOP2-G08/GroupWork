import json


def get_bookshelf(json_file_path):
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

def append_to_json(path, new_data):
    """
    JSONファイルに新しいデータを追加する関数
    処理の流れ
    1. 'r+'モードでファイルを開く。これにより、ファイルの読み書きが可能になる。
    2. json.load関数を使用して、JSONファイルの内容をPythonのデータ構造（ここではリスト）に変換する。
    3. appendメソッドを使用して、新しいデータを既存のリストに追加する。
    4. seekメソッドを使用して、ファイルポインタをファイルの先頭に戻す。
    5. truncateメソッドを使用して、ファイルの内容をクリアする。
    6. json.dump関数を使用して、Pythonのデータ構造をJSON形式の文字列に変換し、ファイルに書き込む。
    Parameters:
        path (str): JSONファイルのパス。
        new_data (dict): 追加するデータ。JSONファイルの各要素に対応するキーと値を持つ辞書。
    Returns:
        None
    """
    # 'r+'モードでファイルを開く。これにより、ファイルの読み書きが可能になる。
    with open(path, 'r+', encoding='utf-8') as file:
        # json.load関数を使用して、JSONファイルの内容をPythonのデータ構造（ここではリスト）に変換する。
        #注意：読み込み先のファイルの内容が空の場合、json.load関数は例外を発生させる。→最低でも[](空のリスト)を入れておく
        data = json.load(file)
        # appendメソッドを使用して、新しいデータを既存のリストに追加する。
        data.append(new_data)
        # seekメソッドを使用して、ファイルポインタをファイルの先頭に戻す。
        file.seek(0)
        # truncateメソッドを使用して、ファイルの内容をクリアする。
        file.truncate()
        # json.dump関数を使用して、Pythonのデータ構造をJSON形式の文字列に変換し、ファイルに書き込む。
        json.dump(data, file, ensure_ascii=False, indent=4)

"""
def append_to_json(json_file_path, info_list):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

        #リスト形式で追加
    new_data = {
        'title': info_list['title'],
        'isbn_13': info_list['isbn_13'],
        'authors': info_list['authors'],
        'published_date': info_list['published_date'],
        'page_count': info_list['page_count'],
        'description': info_list['description'],
        'publisher': info_list['publisher'],
        'cover_image_url': info_list['cover_image_url']
    }

    data.update(new_data)

    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
"""

#-------------------------------------------------------------------------------#
# 例として、json_file_pathとinfo_listを適当に設定
# json_file_path = 'Bookshelf.json'
# info_list = ['test', '1234567', ['Author'], '2024-01-18', 200, 'New book description', 'Publisher', 'https://example.com/cover.jpg']

# # 関数を呼び出してJSONファイルに追加
# append_to_json(json_file_path, info_list)
        
# テスト用
if __name__ == '__main__':
    test_list = {
        'title': 'スラスラわかるPython 第2版', 
        'isbn_13': '9784798169361', 
        'authors': ['北川 慎治', '岩崎 圭'],
        'published_date': '2021-11-17', 
        'page_count': 330, 
        'description': 'Pythonの技術を基礎からやさしく解説した、入門書の決定版！ 本書は「はじめてプログラミングを学ぶ人」に向け、Pythonのスタンダードな知識を 習得することを目標としています。基本をしっかり理解し、身につけられるよう、 必要最低限の知識を丁寧に解説しています。 前版を見直し、プログラミング以前に初学者がつまずきやすかったCUIの操作解説を充実させ、 プログラムの動きを終えるよう、コードの入力内容と実行結果を一目でわかるようにしました。 また、前版刊行後に普及した「型ヒント」の章を新たに設けています。 ※本書の内容は、2021年10月にリリースされたPython 3.10に基づいています。 将来、機械学習に取り組もうと思っている方は、まずは本書でPythonプログラミングを はじめてみましょう。 【目次】 第1章 Pythonの紹介 第2章 Pythonを自分のPCで動かそう 第3章 Pythonでプログラムを動かそう 第4章 型とメソッド 第5章 条件分岐 第6章 リスト型と繰り返し処理 第7章 辞書型 第8章 関数 第9章 エラーと例外 第10章 型ヒント 第11章 スクリプト、モジュール、パッケージ 第12章 Webスクレイピング 第13章 ファイル操作', 
        'publisher': '翔泳社', 
        'cover_image_url': 'http://books.google.com/books/content?id=ABdfEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api'
        }
    append_to_json('../Bookshelf.json', test_list)
