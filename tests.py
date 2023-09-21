from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('name, genre', [
        ['a', 'Фантастика'], ['a'*2,'Ужасы'], ['a'*39, 'Детективы'], ['a'*40, 'Мультфильмы']
    ]
                             )
    def test_set_book_genre_four_books_increased_dictionary(self, name, genre):

        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.books_genre[name] == genre

    def test_get_book_genre_one_book_received_genre(self):

        collector = BooksCollector()

        name = 'Гордость и предубеждение и зомби'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre', [
        ['Гордость и предубеждение и зомби', 'Фантастика'],
        ['Релиз вовремя', 'Фантастика']
    ]
                             )
    def test_get_books_with_specific_genre_two_books_name_book(self, name, genre):

        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_books_with_specific_genre(genre) == [name]

    def test_get_books_genre_one_book_received_dictionary(self):

        collector = BooksCollector()

        name = 'Гордость и предубеждение и зомби'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_books_genre() == {name : genre}

    def test_get_books_for_children_one_book_received_name_book(self):

        collector = BooksCollector()

        name = 'Гордость и предубеждение и зомби'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_books_for_children() == [name]

    def test_add_book_in_favorites_one_book_received_name_book(self):

        collector = BooksCollector()

        name = 'Убийца внутри меня'
        genre = 'Детективы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)

        assert collector.favorites == [name]

    def test_delete_book_from_favorites_one_book_decreased_dictionary(self):

        collector = BooksCollector()

        name = 'Убийца внутри меня'
        genre = 'Детективы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)

        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_one_book_received_name_book(self):

        collector = BooksCollector()

        name = 'Убийца внутри меня'
        genre = 'Детективы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)

        assert collector.get_list_of_favorites_books() == [name]
