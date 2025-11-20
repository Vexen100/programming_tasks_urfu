class Book:
    """
    Базовый класс для представления книги.
    
    Атрибуты:
        title (str): Название книги
        author (str): Автор книги
        year (int): Год издания книги
    """

    def __init__(self, title, author, year):
        """
        Инициализирует объект книги с указанными параметрами.
        
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


class Ebook(Book):
    """
    Дочерний класс для представления электронной книги.
    
    Наследует от Book и добавляет атрибут формата файла.
    
    Атрибуты:
        format (str): Формат электронного файла (например, PDF, EPUB)
    """

    def __init__(self, title, author, year, format):
        """
        Инициализирует объект электронной книги.
        
        Параметры:
            format: Формат электронного файла
        """
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        """
        Расширяет базовое описание, добавляя информацию о формате.
        
        Возвращает:
            str: Строка с дополнительной информацией о формате файла
        """
        base_info = super().info()
        return f"{base_info}, Формат: {self.format}"
