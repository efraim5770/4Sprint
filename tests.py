import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    """Фикстура создает новый экземпляр BooksCollector для каждого теста"""
    return BooksCollector()


class TestBooksCollector:
    # Тесты для add_new_book
    @pytest.mark.parametrize("book_name, expected", [
        ("Книга", True),
        ("", False),
        ("Очень длинное название книги которое превышает максимально допустимую длину в сорок символов", False)
    ])
    def test_add_new_book(self, collector, book_name, expected):
        """
        Проверяет добавление книг с разными названиями:
        - Корректное название добавляется
        - Пустое название не добавляется
        - Слишком длинное название (>40 символов) не добавляется
        """
        collector.add_new_book(book_name)
        assert (book_name in collector.books_genre) == expected

    def test_add_new_book_duplicate(self, collector):
        """
        Проверяет невозможность добавления дубликата книги
        """
        book_name = "Дубль"
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)  # Попытка добавить дубликат
        assert len(collector.books_genre) == 1

    # Тесты для set_book_genre
    def test_set_book_genre_valid(self, collector):
        """
        Проверяет установку допустимого жанра для существующей книги
        """
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Фантастика")
        assert collector.get_book_genre("Книга") == "Фантастика"

    def test_set_book_genre_invalid_book(self, collector):
        """
        Проверяет невозможность установки жанра для несуществующей книги
        """
        collector.set_book_genre("Неизвестная книга", "Фантастика")
        assert "Неизвестная книга" not in collector.books_genre

    def test_set_book_genre_invalid_genre(self, collector):
        """
        Проверяет невозможность установки недопустимого жанра
        """
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Фэнтези")
        assert collector.get_book_genre("Книга") == ""

    # Тесты для get_book_genre
    def test_get_book_genre_existing(self, collector):
        """
        Проверяет получение жанра для существующей книги
        """
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Ужасы")
        assert collector.get_book_genre("Книга") == "Ужасы"

    def test_get_book_genre_non_existing(self, collector):
        """
        Проверяет получение None для несуществующей книги
        """
        assert collector.get_book_genre("Неизвестная книга") is None

    # Тесты для get_books_with_specific_genre
    def test_get_books_with_specific_genre(self, collector):
        """
        Проверяет получение книг по конкретному жанру
        """
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга1", "Детективы")
        collector.set_book_genre("Книга2", "Детективы")
        assert collector.get_books_with_specific_genre("Детективы") == ["Книга1", "Книга2"]

    def test_get_books_with_specific_genre_empty(self, collector):
        """
        Проверяет пустой результат при отсутствии книг с жанром
        """
        assert collector.get_books_with_specific_genre("Фантастика") == []

    # Тесты для get_books_genre
    def test_get_books_genre(self, collector):
        """
        Проверяет получение полного словаря книг с жанрами
        """
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга1", "Мультфильмы")
        collector.set_book_genre("Книга2", "Комедии")
        assert collector.get_books_genre() == {"Книга1": "Мультфильмы", "Книга2": "Комедии"}

    # Тесты для get_books_for_children
    def test_get_books_for_children(self, collector):
        """
        Проверяет фильтрацию книг для детей:
        - Книги без возрастного рейтинга включаются
        - Книги с возрастным рейтингом исключаются
        """
        collector.add_new_book("Детская книга")
        collector.add_new_book("Взрослая книга")
        collector.set_book_genre("Детская книга", "Мультфильмы")
        collector.set_book_genre("Взрослая книга", "Ужасы")
        assert collector.get_books_for_children() == ["Детская книга"]

    # Тесты для add_book_in_favorites
    def test_add_book_in_favorites(self, collector):
        """
        Проверяет добавление существующей книги в избранное
        """
        collector.add_new_book("Любимая книга")
        collector.add_book_in_favorites("Любимая книга")
        assert "Любимая книга" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate(self, collector):
        """
        Проверяет невозможность добавления дубликата в избранное
        """
        collector.add_new_book("Любимая книга")
        collector.add_book_in_favorites("Любимая книга")
        collector.add_book_in_favorites("Любимая книга")
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_non_existing(self, collector):
        """
        Проверяет невозможность добавления несуществующей книги в избранное
        """
        collector.add_book_in_favorites("Неизвестная книга")
        assert "Неизвестная книга" not in collector.get_list_of_favorites_books()

    # Тесты для delete_book_from_favorites
    def test_delete_book_from_favorites(self, collector):
        """
        Проверяет удаление книги из избранного
        """
        collector.add_new_book("Любимая книга")
        collector.add_book_in_favorites("Любимая книга")
        collector.delete_book_from_favorites("Любимая книга")
        assert "Любимая книга" not in collector.get_list_of_favorites_books()

    # Тесты для get_list_of_favorites_books
    def test_get_list_of_favorites_books(self, collector):
        """
        Проверяет получение полного списка избранных книг
        """
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.add_book_in_favorites("Книга1")
        collector.add_book_in_favorites("Книга2")
        assert collector.get_list_of_favorites_books() == ["Книга1", "Книга2"]

    # Тест для работы с пустой коллекцией
    def test_empty_collection(self, collector):
        """
        Проверяет методы при пустой коллекции:
        - Получение жанров возвращает пустой словарь
        - Поиск по жанру возвращает пустой список
        - Список для детей возвращает пустой список
        - Избранное возвращает пустой список
        """
        assert collector.get_books_genre() == {}
        assert collector.get_books_with_specific_genre("Фантастика") == []
        assert collector.get_books_for_children() == []
        assert collector.get_list_of_favorites_books() == []
