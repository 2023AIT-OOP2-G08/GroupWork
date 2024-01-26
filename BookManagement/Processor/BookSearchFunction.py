import requests
# print(requests.__version__)  -> 2.31.0

#書籍検索機能_ISBN
def search_books_by_isbn(isbn):
    url = f'https://www.googleapis.com/books/v1/volumes?q=+inisbn:{isbn}&maxResults={20}'
    response = requests.get(url).json()

    # 検索結果なし
    if response['totalItems'] == 0:
        return 'No books found for this isbn'
        
    # print(response['totalItems'])

    books_info = []
    for item in response['items']:
        book_info = parse_book_info(item)
        books_info.append(book_info)
    return books_info

#書籍検索機能_タイトル
def search_books_by_title(title):
    url = f'https://www.googleapis.com/books/v1/volumes?q=+intitle:{title}&maxResults={20}'
    response = requests.get(url).json()

    # 検索結果なし
    if response['totalItems'] == 0:
        return 'No books found for this title'
    
    # print(response['totalItems'])

    books_info = []
    for item in response['items']:
        book_info = parse_book_info(item)
        books_info.append(book_info)
    return books_info

#書籍検索機能_著者名
def search_books_by_authors(authors):
    url = f'https://www.googleapis.com/books/v1/volumes?q=+inauthors:{authors}&maxResults={20}'
    response = requests.get(url).json()

    # 検索結果なし
    if response['totalItems'] == 0:
        return 'No books found for this authors'
    
    # print(response['totalItems'])

    books_info = []
    for item in response['items']:
        book_info = parse_book_info(item)
        books_info.append(book_info)
    return books_info

#検索結果を返す　ーー出力できる検索結果は最大20件にしてみてます。
def parse_book_info(item):
    volume_info = item.get('volumeInfo', {})
    title = volume_info.get('title', 'No title available')#タイトル
    authors = volume_info.get('authors', ['No authors available'])#著者名
    image_links = volume_info.get('imageLinks', {})#画像リンク
    cover_image_url = image_links.get('thumbnail', 'No cover image available')#画像
    isbn = volume_info.get('industryIdentifiers', [{'identifier': 'No ISBN'}])[0].get('identifier')#ISBN
    published_date = volume_info.get('publishedDate', 'No publishedDate available')#出版日
    description = volume_info.get('description', 'No description available')#あらすじ
    page_count = volume_info.get('pageCount', 'No pageCount available')#ページ数
    publisher = volume_info.get('publisher', 'No publisher available')#出版社

    return {
        'title': title,#タイトル
        'isbn_13': isbn,#ISBN
        'authors': authors,#著者名
        'published_date': published_date,#出版日
        'page_count': page_count,#ページ数
        'description': description,#あらすじ
        'publisher': publisher,#出版社
        'cover_image_url': cover_image_url#サムネイル画像
    }

# # 書籍情報を格納するリスト
# books_info1 = []
# books_info2 = []
# books_info3 = []

# # 各検索クエリに対して書籍情報を取得
#

# book_info = search_books_by_title('リーダブルコード')
# books_info2.extend(book_info)

# book_info = search_books_by_authors('["Dustin Boswell","Trevor Foucher"]')
# books_info3.extend(book_info)

# # 取得した書籍情報を表示
# for book in books_info1:
#     print(book)
#     print('------------------------')

# print('------------------------')

# for book in books_info2:
#     print(book)
#     print('------------------------')

# print('------------------------')

# for book in books_info3:
#     print(book)
#     print('------------------------')