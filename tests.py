from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)

        assert collector.get_books_genre() == {name : ''}

    @pytest.mark.parametrize('name, genre', [
        ['a', 'Фантастика'], ['a'*2,'Ужасы'], ['a'*39, 'Детективы'], ['a'*40, 'Мультфильмы']
    ]
                             )
    def test_set_book_genre_four_books_increased_dictionary(self, name, genre):

        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

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

        assert collector.get_list_of_favorites_books() == [name]

    def test_delete_book_from_favorites_one_book_decreased_dictionary(self):

        collector = BooksCollector()

        name = 'Убийца внутри меня'
        genre = 'Детективы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)

        assert len(collector.favorites) == 0

    @pytest.mark.parametrize('name', ['', 'a' * 42]
                             )
    def test_add_new_book_name_0_and_42_symbols_empty_list(self, name):

        collector = BooksCollector()

        collector.add_new_book(name)

        assert collector.get_books_genre() == {}

    def test_get_genre_book_without_genre_empty_list(self):

        collector = BooksCollector()

        name = '45 татуировок менеджера'
        collector.add_new_book(name)

        assert collector.get_book_genre(name) == ''





