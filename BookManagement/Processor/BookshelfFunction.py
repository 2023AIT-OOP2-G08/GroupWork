import json
import os

def get_bookshelf(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:  #jsonファイルを開ける
        data = json.load(file)  #dataにjsonファイルの情報を代入
    return data  # 辞書型のデータを返す

def remove_index_elements(json_file_path,input_list, index):
    """
    指定したindexのlistを削除する
    Parameters:
        json_file_path (str): JSONファイルのパス
        input_list (list): お気に入りした本を格納しているlist 既存のlist
        index (int): 削除するデータのindexnumber
    Returns:
        input_list (list): 削除後のlist
    """
    print(index)
    # インデックスが範囲内にあることを確認
    if 0 <= index < len(input_list):
        # 指定したインデックスの要素を削除
        input_list.pop(index)
    else:
        raise IndexError(f"Index out of range: {index}")

    # スクリプトのあるディレクトリを取得
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # ベースディレクトリを基準にした相対パスを指定
    json_file_path = os.path.join(base_dir, json_file_path)

    # JSONファイルに書き込む
    try:
        with open(json_file_path, 'w', encoding='utf-8') as file:
            json.dump(input_list, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"IOError: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        raise

    return input_list

def add_information(input_list, new_list):
    #データを追加するプログラム
    #input_list お気に入りした本を格納しているlist 既存のlist
    #新しく追加するデータnew_list(list)
    input_list.append(new_list)
    return input_list

def append_to_json(json_file_path, new_data):
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
        new_data (dict): 追加するデータ。JSONファイルの各要素に対応するキーと値を持つ辞書。
    Returns:
        None
    """
    try:
        with open(json_file_path, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            data.append(new_data)
            file.seek(0)
            file.truncate()
            json.dump(data, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"IOError: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        raise

def is_list_in_json_file(json_file_path, list):
    """
    指定されたリストの'title'または'isbn_13'がJSONファイルに含まれているかを確認します。

    Parameters:
    list (list): 確認するリスト。各要素は'title'と'isbn_13'をキーとする辞書

    Returns:
    bool: リストの全ての要素の'title'または'isbn_13'がJSONファイルに含まれている場合はTrue、そうでない場合はFalse。
    """
    # try:
    # JSONファイルを読み込む、すでに作成されているBookshelfFunction.pyのget_bookshelf(json_file_path)でもいい
    with open(json_file_path, 'r', encoding='utf-8') as file:
        bookshelf_data = json.load(file)
        
        for book in bookshelf_data:
            if book.get("title") in list['title']:
                return True
            #titleがない場合はisbn_13で確認する
            elif book.get("isbn_13") in list['isbn_13']:
                return True
        return False

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
    append_to_json(test_list)
    print(is_list_in_json_file(test_list))
