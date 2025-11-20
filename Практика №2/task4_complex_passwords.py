from random import choices, shuffle, randint

result = list()
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL = r'!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

# Приветственное сообщение с описанием программы
print(
    'Добро пожаловать в сервис паролей — ваш надёжный помощник в создании безопасных паролей! 🛡️',
    'Давайте настроим идеальный пароль под ваши нужды.',
    sep='\n'
)

# Сбор пользовательских предпочтений для генерации пароля
while True:
    password_lower_case = input(
        'Включить строчные буквы (a–z)? [Да/Нет]: '
    ).lower()
    while password_lower_case not in ('да', 'нет'):
        print('Ошибка: пожалуйста, введите корректное значение.')
        password_lower_case = input(
            'Включить строчные буквы (a–z)? [Да/Нет]: '
        ).lower()

    password_upper_case = input(
        'Включить заглавные буквы (A–Z)? [Да/Нет]: '
    ).lower()
    while password_upper_case not in ('да', 'нет'):
        print('Ошибка: пожалуйста, введите корректное значение.')
        password_upper_case = input(
            'Включить заглавные буквы (A–Z)? [Да/Нет]: '
        ).lower()

    password_special_characters = input(
        'Использовать специальные символы (!@#$%^&* и др.)? [Да/Нет]: '
    ).lower()
    while password_special_characters not in ('да', 'нет'):
        print('Ошибка: пожалуйста, введите корректное значение.')
        password_special_characters = input(
            'Использовать специальные символы (!@#$%^&* и др.)? [Да/Нет]: '
        ).lower()

    password_numbers = input(
        'Добавить цифры (0–9)? [Да/Нет]: '
    ).lower()
    while password_numbers not in ('да', 'нет'):
        print('Ошибка: пожалуйста, введите корректное значение.')
        password_numbers = input(
            'Добавить цифры (0–9)? [Да/Нет]: '
        ).lower()

    password_length = int(input(
        'Какой длины должен быть пароль? '
        '(рекомендуется от 8 до 32 символов): '
    ))
    while password_length <= 0:
        print('Ошибка: пожалуйста, введите корректное значение длины. (больше 0)')
        password_length = int(input(
            'Какой длины должен быть пароль? '
            '(рекомендуется от 8 до 32 символов): '
        ))

    # Проверка, что выбран хотя бы один тип символов
    if (
        password_lower_case == 'нет'
        and password_upper_case == 'нет'
        and password_special_characters == 'нет'
        and password_numbers == 'нет'
    ):
        print(
            'Предупреждение: пароль не может быть пустым. '
            'Пожалуйста, включите хотя бы один тип символов. Перезапускаю выбор...'
        )
    else:
        break

# Генерация пароля с учетом выбранных параметров
while True:
    if password_lower_case == 'да':
        result += choices(LOWERCASE, k=randint(1, password_length // 2))
    if password_upper_case == 'да':
        result += choices(UPPERCASE, k=randint(1, password_length // 2))
    if password_special_characters == 'да':
        result += choices(SPECIAL, k=randint(1, password_length // 2))
    if password_numbers == 'да':
        result += choices(DIGITS, k=randint(1, password_length // 2))
    
    if len(result) == password_length:
        break
    result = list()

shuffle(result)
print(f'Вот ваш пароль: {"".join(result)}', 'Удачи!', sep='\n')