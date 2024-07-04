import pickle, json


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def read_the_book(self):
        '''Читаем книгу'''
        return f'The book "{self.title}" has been read'

    def rename_the_book(self, new_title=None):
        '''Следуя повесточки, переименовываем книгу'''
        if new_title is None:
            return f'The book is not renamed'
        self.title = new_title
        return f'The book rename to "{self.title}"'


class BookEncoder(json.JSONEncoder):

    def default(self, o):
        return {
            "ClassName": o.__class__.__name__,
            "Title": o.title,
            "Author": o.author,
            "Genre": o.genre,
            "Methods": {
                "read_the_book": o.read_the_book(),
                "rename_the_book": o.rename_the_book()
            }
        }


my_book = Book('Ten Little Niggers', 'Agatha Christie', 'crime')
print(my_book.__dict__)
print(my_book.read_the_book())
print(my_book.rename_the_book('Ten Little Indians'))
print(my_book.rename_the_book('And Then There Were None'))
print()

with open('book.json', 'w', encoding='utf-8') as fh:
    json.dump(my_book, fh, cls=BookEncoder, ensure_ascii=False, indent=2)

with open('book.json', encoding='utf-8') as fh:
    python_data_from_file = json.load(fh)

print(python_data_from_file)
print()

with open('book.pickle', 'wb') as f:
    pickle.dump(my_book, f)

with open('book.pickle', 'rb') as f:
    python_data_from_file = pickle.load(f)

print(python_data_from_file.__dict__)



