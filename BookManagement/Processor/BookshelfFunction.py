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

""" 
# テスト用
if __name__ == '__main__':
    test_list = [
            {
                "title": "情熱プログラマー ソフトウェア開発者の幸せな生き方",
                "isbn_13": "9784274067938",
                "authors": [
                    "Chad Fowler"
                ],
                "published_date": "2010-02",
                "page_count": 200,
                "description": "本書は、等身大のプログラマの一人がキャリア開発の重要性を説き、そのための心構えなどを示したもの。「プログラマはビジネス視点を持って意識的なキャリア開発をすべき」という視点から、その実践方法を著者独特の生き生きとした共感できる語り口で伝える。原書は\"The Passionate Programmer: Creating a Remarkable Career in Software Development\"(The Pragmatic Programmers,2009)",
                "publisher": "株式会社 オーム社",
                "cover_image_url": "http://books.google.com/books/content?id=oFrK2r8rQbEC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
            },
            {
                "title": "ハッカーと画家",
                "isbn_13": "9784274065972",
                "authors": "No authors available",
                "published_date": "2005",
                "page_count": 284,
                "description": "天才プログラマが語る創造のセンス",
                "publisher": "株式会社 オーム社",
                "cover_image_url": "http://books.google.com/books/content?id=SinFRfuTH7IC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
            },
            {
                "title": "読みやすいコードのガイドライン -持続可能なソフトウェア開発のために",
                "isbn_13": "9784297130367",
                "authors": [
                    "石川宗寿"
                ],
                "published_date": "2022-10-22",
                "page_count": 0,
                "description": "開発が大規模化・長期化するほど、コードを「読む」コストは増大していきます。そのため「読みやすさ」の向上は、生産性を改善し、プロダクトの成長限界を引き上げる重要な手段と言えるでしょう。 本書は、読みやすさの本質を学び、実践するための考え方をマスターできる一冊です。体系的な理解を実現するため、あらゆる角度から、豊富な例を交えて解説しています。表面的なテクニックではなく、いま目の前にあるコードに最適な改良方法を選び取る力が身に付きます。",
                "publisher": "No publisher information available",
                "cover_image_url": "http://books.google.com/books/content?id=uyNgzwEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
            },
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
            },
            {
                "title": "エンジニアのためのドキュメントライティング",
                "isbn_13": "9784800590831",
                "authors": [
                    "ジャレッド・バーディ",
                    "ザッカリー・サラ・コーライセン",
                    "ジェン・ランボーン",
                    "デービッド・ヌーニェス",
                    "ハイディ・ウォーターハウス"
                ],
                "published_date": "2023-03-11",
                "page_count": 0,
                "description": "経験に長けた執筆者たちが開発者向けドキュメントの作成方法をゼロから説明するフィールドガイド",
                "publisher": "No publisher information available",
                "cover_image_url": "http://books.google.com/books/content?id=Mi-rzwEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
            },
            {
                "title": "LaTeX2e 美文書作成入門",
                "isbn_13": "9784297117122",
                "authors": [
                    "奥村晴彦",
                    "黒木裕介"
                ],
                "published_date": "2020-11",
                "page_count": 448,
                "description": "No description available",
                "publisher": "No publisher information available",
                "cover_image_url": "http://books.google.com/books/content?id=zDsJzgEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
            },
            {
                "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
                "isbn_13": "9784798155456",
                "authors": [
                    "原田秀司"
                ],
                "published_date": "2019-01-21",
                "page_count": 210,
                "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
                "publisher": "翔泳社",
                "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
            },
            {
                "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
                "isbn_13": "9784798155456",
                "authors": [
                    "原田秀司"
                ],
                "published_date": "2019-01-21",
                "page_count": 210,
                "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
                "publisher": "翔泳社",
                "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
            },
            {
                "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
                "isbn_13": "9784798155456",

                "authors": [
                    "原田秀司"
                ],
                "published_date": "2019-01-21",
                "page_count": 210,
                "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
                "publisher": "翔泳社",
                "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
            },
            {
                "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
                "isbn_13": "9784798155456",
                "authors": [
                    "原田秀司"
                ],
                "published_date": "2019-01-21",
                "page_count": 210,
                "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
                "publisher": "翔泳社",
                "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
            },
            {
                "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
                "isbn_13": "9784798155456",
                "authors": [
                    "原田秀司"
                ],
                "published_date": "2019-01-21",
                "page_count": 210,
                "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
                "publisher": "翔泳社",
                "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
            },
            {
                "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
                "isbn_13": "9784798155456",
                "authors": [
                    "原田秀司"
                ],
                "published_date": "2019-01-21",
                "page_count": 210,
                "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
                "publisher": "翔泳社",
                "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
            },
            {
                "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
                "isbn_13": "9784798155456",
                "authors": [
                    "原田秀司"
                ],
                "published_date": "2019-01-21",
                "page_count": 210,
                "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
                "publisher": "翔泳社",
                "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
            },
            {
                "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
                "isbn_13": "9784798155456",
                "authors": [
                    "原田秀司"
                ],
                "published_date": "2019-01-21",
                "page_count": 210,
                "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
                "publisher": "翔泳社",
                "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
            }
            # {
            #     "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計マルチデバイス時代のインターフェース設計マルチデバイス時代のインターフェース設計マルチデバイス時代のインターフェース設計マルチデバイス時代のインターフェース設計　",
            #     "isbn_13": "9784798155456",
            #     "authors": [
            #         "原田秀司"
            #     ],
            #     "published_date": "2019-01-21",
            #     "page_count": 210,
            #     "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
            #     "publisher": "翔泳社",
            #     "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
            # }
        ]
    # append_to_json(test_list)
    # print(is_list_in_json_file(test_list))
    # カレントディレクトリを取得
    current_directory = os.path.dirname(os.path.abspath(__file__))
    SHELF_JSON_PATH = os.path.join(current_directory, '../Bookshelf.json')
    print(remove_index_elements(SHELF_JSON_PATH,test_list,0))
"""
