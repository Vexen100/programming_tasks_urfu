from datetime import datetime


class Book:
    """
    Класс для представления книги с дополнительными методами и свойствами.
    
    Атрибуты:
        title (str): Название книги
        author (str): Автор книги
        year (int): Год издания книги
    """

    def __init__(self, title, author, year):
        """
        Инициализирует объект книги.
        
        Параметры:
            title: Название книги
            author: Имя автора
            year: Год издания (целое число)
        """
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        """
        Формирует строку с информацией о книге.
        
        Возвращает:
            str: Строка в формате "Автор: [автор], Название: [название], Год: [год]"
        """
        return f'Автор: {self.author}, Название: {self.title}, Год: {self.year}'

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        
        Возвращает:
            str: Результат вызова метода info()
        """
        return self.info()

    def __eq__(self, other):
        """
        Проверяет равенство двух книг по названию.
        
        Параметры:
            other: Объект для сравнения
        
        Возвращает:
            bool: True если названия совпадают и other является экземпляром Book
        """
        return isinstance(other, Book) and self.title == other.title

    @property
    def age(self):
        """
        Вычисляет возраст книги в годах.
        
        Возвращает:
            int: Количество лет с момента издания до текущего года
        """
        return datetime.now().year - self.year

    @classmethod
    def from_string(cls, string):
        """
        Создает экземпляр книги из строки с разделителями-точками с запятой.
        
        Параметры:
            string: Строка в формате "название;автор;год"
        
        Возвращает:
            Book: Новый экземпляр класса Book
        
        Пример:
            Book.from_string("Война и мир;Л.Н. Толстой;1869")
        """
        title, author, year = string.split(';')
        return cls(title, author, int(year))
