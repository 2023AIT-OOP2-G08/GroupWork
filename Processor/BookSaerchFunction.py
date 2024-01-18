import requests
# print(requests.__version__)  -> 2.31.0
import json
# print(json.__version__)  -> 2.0.9

#書籍検索機能_ISBN
def search_books_by_isbn(isbn):
    url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}'
    response = requests.get(url).json()

    if response['totalItems'] == 0:
        return 'No books found for this isbn'

    books_info = []
    for item in response['items']:
        book_info = parse_book_info(item)
        books_info.append(book_info)
    return books_info

#書籍検索機能_タイトル
def search_books_by_title(title):
    url = f'https://www.googleapis.com/books/v1/volumes?q=title:{title}'
    response = requests.get(url).json()

    if response['totalItems'] == 0:
        return 'No books found for this title'

    books_info = []
    for item in response['items']:
        book_info = parse_book_info(item)
        books_info.append(book_info)
    return books_info

#書籍検索機能_タイトル
def search_books_by_authors(authors):
    url = f'https://www.googleapis.com/books/v1/volumes?q=authors:{authors}'
    response = requests.get(url).json()

    if response['totalItems'] == 0:
        return 'No books found for this authors'

    books_info = []
    for item in response['items']:
        book_info = parse_book_info(item)
        books_info.append(book_info)
    return books_info

#検索結果を返す
def parse_book_info(item):
    volume_info = item.get('volumeInfo', {})
    title = volume_info.get('title', 'No title available')
    authors = volume_info.get('authors', ['No authors available'])
    image_links = volume_info.get('imageLinks', {})
    cover_image_url = image_links.get('thumbnail', 'No cover image available')
    isbn = volume_info.get('industryIdentifiers', [{'identifier': 'No ISBN'}])[0].get('identifier')

    return {
        'cover_image_url': cover_image_url,
        'title': title,
        'authors': authors,
        'isbn': isbn
    }

# 書籍情報を格納するリスト
books_info1 = []
books_info2 = []
books_info3 = []

# 各検索クエリに対して書籍情報を取得
book_info = search_books_by_isbn('9784873115658')
books_info1.extend(book_info)

book_info = search_books_by_title('リーダブルコード')
books_info2.extend(book_info)

book_info = search_books_by_authors('["Dustin Boswell","Trevor Foucher"]')
books_info3.extend(book_info)

# 取得した書籍情報を表示
for book in books_info1:
    print(book)
    print('------------------------')

print('------------------------')

for book in books_info2:
    print(book)
    print('------------------------')

print('------------------------')

for book in books_info3:
    print(book)
    print('------------------------')