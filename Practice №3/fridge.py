import datetime
from decimal import Decimal

# Формат даты для парсинга и обработки сроков годности
DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    """
    Добавляет продукт в холодильник.
    
    Args:
        items (dict): Словарь с продуктами холодильника
        title (str): Название продукта
        amount (str/int/float): Количество продукта
        expiration_date (str, optional): Срок годности в формате 'ГГГГ-ММ-ДД'. 
            Defaults to None.
    
    Returns:
        None
    """
    if expiration_date is not None:
        expiration_date = datetime.datetime.strptime(
            expiration_date, DATE_FORMAT
        ).date()
    
    new_item = {
        'amount': Decimal(amount), 
        'expiration_date': expiration_date
    }
    items[title] = items.get(title, []) + [new_item]


def add_by_note(items, note):
    """
    Добавляет продукт в холодильник на основе текстовой заметки.
    
    Args:
        items (dict): Словарь с продуктами холодильника
        note (str): Текстовая заметка с информацией о продукте
    
    Returns:
        None
    """
    # Разделяем заметку на слова и переворачиваем порядок для удобства парсинга
    note = note.split()[::-1]
    
    # Проверяем, есть ли срок годности (содержит ли первое слово дефис)
    if '-' not in note[0]:
        expiration_date = None
        amount = Decimal(note[0])
        # Восстанавливаем оригинальный порядок слов в названии
        title = ' '.join(note[1:][::-1])
    else:
        expiration_date = datetime.datetime.strptime(
            note[0], DATE_FORMAT
        ).date()
        amount = Decimal(note[1])
        # Восстанавливаем оригинальный порядок слов в названии
        title = ' '.join(note[2:][::-1])
    
    new_item = {
        'amount': Decimal(amount), 
        'expiration_date': expiration_date
    }
    items[title] = items.get(title, []) + [new_item]


def find(items, needle):
    """
    Находит продукты по частичному совпадению в названии.
    
    Args:
        items (dict): Словарь с продуктами холодильника
        needle (str): Строка для поиска в названиях продуктов
    
    Returns:
        list: Список названий продуктов, содержащих искомую строку 
            (без учета регистра)
    """
    return [
        key for key in items 
        if needle.lower() in key.lower()
    ]


def amount(items, needle):
    """
    Вычисляет общее количество продукта по частичному совпадению в названии.
    
    Args:
        items (dict): Словарь с продуктами холодильника
        needle (str): Строка для поиска в названиях продуктов
    
    Returns:
        Decimal: Суммарное количество всех найденных продуктов
    """
    titles = find(items, needle)  # Находим все подходящие продукты
    result = Decimal(0)
    
    for title in titles:
        # Суммируем количества из всех партий данного продукта
        amounts = [elem['amount'] for elem in items[title]]
        result += Decimal(sum(amounts))
        
    return result
