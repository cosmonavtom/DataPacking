'''В данной программе я использовал следующие паттерны:
Singleton, Factory Method, Command, Observer и ещё Repository(sic!)
В первой части задания нужно было реализовать метод Command, я его
сюда запихал. Надеюсь это считается'''
import json


class Librarian:
    '''Используем паттерн Singleton для сущности библиотекаря'''
    _instance = None

    def __new__(cls, *args, **kwargs):
        '''Метод __new__ проверяет есть ли у нас уже библиотекарь и создаём его
        если ещё нет. Если есть, то оставляем "старого" библиотекаря. Возвращаем'''
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class Book:
    '''Создаём класс Book для сущности "Книга"'''

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class Reader:
    '''Создайм класс Reader для сущности "Читатель". book_rental - список, который
    хранит книги взятые читателем(пока не реализовано)'''

    def __init__(self, name: str, book_rental: list = None):
        self.name = name
        self.book_rental = book_rental or []


class AddFactory:
    '''Используем фабричный метод для создания объектов сущностей "книга" и "читатель"
    '''

    @staticmethod
    def add_book(title, author):
        return Book(title, author)

    @staticmethod
    def add_reader(name):
        return Reader(name)


class Command:
    '''Паттерн Command. Делаем из запросов объекты. Создал ради первой части задания и
    ради "использования наибольшего числа паттернов".
    '''

    def execute(self):
        pass


class AddBookCommand(Command):
    '''Добавляем книги'''

    def __init__(self, library, book):
        self.library = library
        self.book = book

    def execute(self):
        self.library.add_book(self.book)


class AddReaderCommand(Command):
    '''Добавляем читателей'''

    def __init__(self, library, reader):
        self.library = library
        self.reader = reader

    def execute(self):
        self.library.add_reader(self.reader)


class RemoveBookCommand(Command):
    '''Удаляем книги из библиотеки.'''

    def __init__(self, library, book):
        self.library = library
        self.book = book

    def execute(self):
        self.library.remove_book(self.book)


class RemoveReaderCommand(Command):
    '''Удаляем читателей.'''

    def __init__(self, library, reader):
        self.library = library
        self.reader = reader

    def execute(self):
        self.library.remove_reader(self.reader)


class RenameBookCommand(Command):
    """Переименовываем книгу в библиотеке."""
    def __init__(self, library, book, new_title: str):
        self.library = library
        self.book = book
        self.new_title = new_title

    def execute(self):
        self.library.rename_book(self.book, self.new_title)


class Observer:
    '''Паттерн Observer. Библиотекарь наблюдает за действиями читателей'''

    def observ(self, message):
        pass


class LibrarianObserver(Observer):
    def observ(self, message: str):
        print(f"Библиотекарь наблюдает, что {message}")


class LibraryRepository:
    '''Хранилище Библиотеки'''

    def __init__(self, books: list = None, readers: list = None):
        self.books = books or []
        self.readers = readers or []

    def add_book(self, book: Book):
        self.books.append(book)

    def add_reader(self, reader: Reader):
        self.readers.append(reader)

    def remove_book(self, book: Book):
        self.books = [b for b in self.books if (b.title != book.title and b.author != book.author)]

    def remove_reader(self, reader: Reader):
        self.readers = [r for r in self.readers if r.name != reader.name]

    def rename_book(self, book: Book, new_title: str):
        for b in self.books:
            if b.title == book.title and b.author == book.author:
                b.title = new_title
                break

    def get_all_books(self):
        return self.books

    def get_all_readers(self):
        return self.readers

    # def save_to_file(self, filename):
    #     '''Несложно было бы и в *.json писать, но в задании просто сохранить'''
    #     with open(filename, 'w') as f:
    #         for book in self.books:
    #             f.write(f"{book.title}, {book.author}\n")
    def save_to_file(self, filename):
        '''Сохраняем книги и читателей в JSON файл'''
        data = {
            'books': [{'title': book.title, 'author': book.author} for book in self.books],
            'readers': [{'name': reader.name, 'book_rental': reader.book_rental} for reader in self.readers]
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        '''Получаем книги и читателей из JSON файла'''
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.books = [Book(book['title'], book['author']) for book in data.get('books', [])]
            self.readers = [Reader(reader['name'], reader.get('book_rental', [])) for reader in data.get('readers', [])]


class Library:
    '''Непосредственно сама библиотека, где мы делаем всякое. Main code'''

    def __init__(self):
        self.repository = LibraryRepository()
        self.librarian = Librarian()
        self.observer = LibrarianObserver()

    def add_book(self, book):
        command = AddBookCommand(self.repository, book)
        command.execute()
        message = f'книга "{book.title}" ({book.author}) добавлена в библиотеку'
        self.observer.observ(message)

    def add_reader(self, reader: Reader):
        command = AddReaderCommand(self.repository, reader)
        command.execute()
        message = f'читатель "{reader.name}" добавлен в картотеку библиотеки'
        self.observer.observ(message)

    def remove_book(self, book: Book):
        command = RemoveBookCommand(self.repository, book)
        command.execute()
        message = f'книга "{book.title}" удалена из библиотеки'
        self.observer.observ(message)

    def remove_reader(self, reader: Reader):
        command = RemoveReaderCommand(self.repository, reader)
        command.execute()
        message = f'читатель "{reader.name}" удалён из картотеки библиотеки'
        self.observer.observ(message)

    def rename_book(self, book: Book, new_title: str):
        command = RenameBookCommand(self.repository, book, new_title)
        command.execute()
        message = f'книга "{book.title}" переименована в "{new_title}"'
        self.observer.observ(message)

    def get_all_books(self):
        print('Список книг в библиотеке:')
        for book in self.repository.get_all_books():
            print(f'{book.title} - {book.author}')

    def get_all_readers(self):
        print("Список читателей в библиотеке:")
        for reader in self.repository.get_all_readers():
            print(reader.name)

    def save_to_file(self, filename):
        self.repository.save_to_file(filename)

    def load_from_file(self, filename):
        self.repository.load_from_file(filename)


library = Library()
# С помощью фабричного метода создаём три книги и трёх читателей
book1 = AddFactory.add_book('Land of Oz', 'L. Frank Baum')
book2 = AddFactory.add_book('War and Peace', 'Leo Tolstoy')
book3 = AddFactory.add_book('Bible', 'Unknown')
reader1 = AddFactory.add_reader('Max')
reader2 = AddFactory.add_reader('Alex')
reader3 = AddFactory.add_reader('Serg')
# Добавляем их поочередно в нашу библиотеку. Библиотекарь пристально наблюдает
library.add_book(book1)
library.add_reader(reader1)
library.add_book(book2)
library.add_reader(reader2)
library.add_book(book3)
library.add_reader(reader3)
print()
# Смотрим, что у нас есть из книг и из читателей
library.get_all_books()
library.get_all_readers()
print()
# Добавляем ещё одну книгу и сохраняем всё в json файл
book4 = AddFactory.add_book('Kolobok', 'Slavic Folk')
library.add_book(book4)
library.save_to_file("library_data.json")
print()
# Читаем из файла и проверяем ничего ли не потерялось
library.load_from_file("library_data.json")
library.get_all_books()
library.get_all_readers()
print()
# Удаляем третью книгу(прости Господи) и переименовывем "Колобка"
library.remove_book(book3)
library.remove_reader(reader1)
library.rename_book(book4, "DoughBall")
print()
# Проверка, что изменения прошли успешно
library.get_all_books()
library.get_all_readers()