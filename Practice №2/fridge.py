import datetime
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    if expiration_date is not None:
        expiration_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()
    items[title] = items.get(title, []) + [{'amount': Decimal(amount), 'expiration_date': expiration_date}]


def add_by_note(items, note):
    note = note.split()[::-1]
    if '-' not in note[0]:
        expiration_date = None
        amount = Decimal(note[0])
        title = ' '.join(note[1:][::-1])
    else:
        expiration_date = datetime.datetime.strptime(note[0], DATE_FORMAT).date()
        amount = Decimal(note[1])
        title = ' '.join(note[2:][::-1])
    items[title] = items.get(title, []) + [{'amount': Decimal(amount), 'expiration_date': expiration_date}]


def find(items, needle):
    return [key for key in items if needle.lower() in key.lower()]


def amount(items, needle):
    titles = find(items, needle)
    result = Decimal(0)
    for title in titles:
        result += Decimal(sum([elem['amount'] for elem in items[title]]))
    return result
