from datetime import datetime


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f'Автор: {self.author}, Название: {self.title}, Год: {self.year}'

    def __str__(self):
        return self.info()

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title

    @property
    def age(self):
        return datetime.now().year - self.year

    @classmethod
    def from_string(cls, string):
        title, author, year = string.split(';')
        return cls(title, author, int(year))
