from random import choice, shuffle

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
        '(рекомендуется от 8 до 32 символов, максимум 100): '
    ))
    while password_length <= 0 or password_length > 100:
        print('Ошибка: длина пароля должна быть от 1 до 100 символов.')
        password_length = int(input(
            'Какой длины должен быть пароль? '
            '(рекомендуется от 8 до 32 символов, максимум 100): '
        ))

    # Проверка, что выбран хотя бы один тип символов
    if (
        password_lower_case == 'нет' and
        password_upper_case == 'нет' and
        password_special_characters == 'нет' and
        password_numbers == 'нет'
    ):
        print(
            'Предупреждение: пароль не может быть пустым. '
            'Пожалуйста, включите хотя бы один тип символов.'
        )
    else:
        break

# Генерация пароля с гарантией завершения
result = []
selected_char_types = []

if password_lower_case == 'да':
    selected_char_types.append(LOWERCASE)
if password_upper_case == 'да':
    selected_char_types.append(UPPERCASE)
if password_special_characters == 'да':
    selected_char_types.append(SPECIAL)
if password_numbers == 'да':
    selected_char_types.append(DIGITS)

# Гарантированное распределение символов
while len(result) < password_length:
    for char_type in selected_char_types:
        if len(result) >= password_length:
            break
        result.append(choice(char_type))

# Перемешивание для безопасности
shuffle(result)
final_password = ''.join(result[:password_length])

print(f'Вот ваш пароль: {final_password}', 'Удачи!', sep='\n')