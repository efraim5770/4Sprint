# qa_python
BooksCollector

1. Добавление книг
test_add_new_book: Добавление книг с валидными и невалидными названиями

test_add_new_book_duplicate: Невозможность добавления дубликата

2. Установка жанров
test_set_book_genre_valid: Установка допустимого жанра

test_set_book_genre_invalid_book: Попытка установки для несуществующей книги

test_set_book_genre_invalid_genre: Попытка установки недопустимого жанра

3. Получение информации о книгах
test_get_book_genre_existing: Получение жанра существующей книги

test_get_book_genre_non_existing: Получение None для несуществующей книги

test_get_books_genre: Получение полного словаря книг

4. Фильтрация по жанрам
test_get_books_with_specific_genre: Поиск книг по конкретному жанру

test_get_books_with_specific_genre_empty: Пустой результат при отсутствии книг

5. Работа с детскими книгами
test_get_books_for_children: Фильтрация книг без возрастного рейтинга

6. Управление избранным
test_add_book_in_favorites: Добавление в избранное

test_add_book_in_favorites_duplicate: Защита от дубликатов

test_add_book_in_favorites_non_existing: Попытка добавления несуществующей книги

test_delete_book_from_favorites: Удаление из избранного

test_get_list_of_favorites_books: Получение списка избранных книг

7. Граничные случаи
test_empty_collection: Работа методов с пустой коллекцией
