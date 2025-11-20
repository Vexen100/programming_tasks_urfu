def to_roman(arab_number):
    """
    Преобразует арабское число в римскую запись.
    
    Аргументы:
        arab_number: строка, содержащая целое число
    
    Возвращает:
        Строку с римским представлением числа
    
    Пример:
        to_roman("14") -> "XIV"
    """
    arab_number = int(arab_number)
    roman_dict = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
        40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
        400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }
    result_roman = ''
    for num in reversed(roman_dict.keys()):
        while arab_number >= num:
            result_roman += roman_dict[num]
            arab_number -= num
    return result_roman


def to_arab(roman_number):
    """
    Преобразует римское число в арабское представление.
    
    Аргументы:
        roman_number: строка с римским числом
    
    Возвращает:
        Целое число — арабское представление
    
    Пример:
        to_arab("XIV") -> 14
    """
    arab_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    result_arab = 0
    prev_char = 0
    for char in reversed(roman_number):
        current_char = arab_dict[char]
        if current_char < prev_char:
            result_arab -= current_char
        else:
            result_arab += current_char
        prev_char = current_char
    return result_arab


# Сбор данных от пользователя
operation = input(
    'Выберите операцию (1 - из римских в арабские, '
    '2 - из арабских в римские): '
)
while operation not in ('1', '2'):
    operation = input(
        'Неверно! Выберите операцию (1 - из римских в арабские, '
        '2 - из арабских в римские): '
    )

data_input = input(
    'Введите список чисел через запятую '
    '(если число одно, то просто введите его): '
)
data_list = [elem.strip() for elem in data_input.split(',')]

# Обработка и вывод результата
result = []
if operation == '1':
    for number in data_list:
        result.append(to_arab(number))
else:
    for number in data_list:
        result.append(to_roman(number))

print(result)