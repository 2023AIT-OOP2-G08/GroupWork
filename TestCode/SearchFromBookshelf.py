import json
import os


JSON_PATH = os.path.join('BookshelfTest.json') # jsonの相対パス

def is_list_in_json_file(list):
    """
    指定されたリストの'title'または'isbn_13'がJSONファイルに含まれているかを確認します。

    Parameters:
    list (list): 確認するリスト。各要素は'title'と'isbn_13'をキーとする辞書

    Returns:
    bool: リストの全ての要素の'title'または'isbn_13'がJSONファイルに含まれている場合はTrue、そうでない場合はFalse。
    """
    # try:
    # JSONファイルを読み込む、すでに作成されているBookshelfFunction.pyのget_bookshelf(json_file_path)でもいい
    with open(JSON_PATH, 'r', encoding='utf-8') as file:
        bookshelf_data = json.load(file)
        
        for book in bookshelf_data:
            if book.get("title") in list['title']:
                return True
            #titleがない場合はisbn_13で確認する
            elif book.get("isbn_13") in list['isbn_13']:
                return True
        return False
    
# テスト用
if __name__ == '__main__':
    # list = [
    #     {
    #     "title": "リーダブルコード",
    #     "isbn_13": "9784873115658",
    #     "authors": [
    #     "Dustin Boswell",
    #     "Trevor Foucher"
    #     ],
    #     "published_date": "2012-06",
    #     "page_count": 237,
    #     "description": "読んでわかるコードの重要性と方法について解説",
    #     "publisher": "O'Reilly Media, Inc.",
    #     "cover_image_url": "http://books.google.com/books/content?id=Wx1dLwEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
    #     }
    # ]
    test_list = {
    "title": "UIデザインの教科書［新版］ マルチデバイス時代のインターフェース設計",
    "isbn_13": "9784798155456",
    "authors": ["原田秀司"],
    "published_date": "2019-01-21",
    "page_count": 210,
    "description": "使いやすい理由とは何か 本書はUIにおけるデザインの定義から、 ハードおよびソフトによる制約、人間の心理による影響、 そして具体的にデザインを形にする方法までを、 図や画像を使いながら、わかりやすく体系的に解説していきます。 Webサイトの閲覧者やアプリのユーザーは、 いつのまにか迷ったり、わからなくなったり、 操作がしっくりこなかったりすることがあります。 本書を読むと「わかりやすさ」と「使いやすさ」の要点がわかるので、 ユーザーを迷わせない、最適なUIを見つけることができます。 デザイナーはもちろん、エンジニア、ディレクター、発注者など、 UI制作に関わる、あらゆる方におすすめの1冊です。 ＊本書は2013年刊行の『UIデザインの教科書』をもとにしていますが、 最新環境にあわせて、構成及び内容を全面的に書き直しています。 〈こんな人のための本です〉 ・UIデザインの基本的な考え方を学びたい ・わかりやすさや使いやすさの理由が知りたい ・最新のデバイスごとの違いやルールを知りたい ・UIデザインのチェック項目が知りたい ・UIデザインを説明するためのロジックが学びたい ...etc 〈目次〉 第1章 デザインの目的とUI/UX 第2章 物理的な制約 第3章 ソフトウェアの影響 第4章 人間の認知特性 第5章 階層と構造 第6章 ナビゲーションとインタラクション 第7章 デザインを形にする",
    "publisher": "翔泳社",
    "cover_image_url": "http://books.google.com/books/content?id=oH2GDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
    }
    print(is_list_in_json_file(test_list))




