import string

RUSSIAN_ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ENGLISH_ALPHABET = string.ascii_lowercase


def detect_language(text: str) -> str:
    """
    Определяет язык текста по первому алфавитному символу.
    
    Аргументы:
        text: Текст для анализа
        
    Возвращает:
        'ru' если первый алфавитный символ русский, 'en' в противном случае
        
    Примечание:
        По умолчанию возвращает 'en', если в тексте нет алфавитных символов
    """
    for char in text:
        lower_char = char.lower()
        if lower_char in RUSSIAN_ALPHABET:
            return "ru"
        if lower_char in ENGLISH_ALPHABET:
            return "en"
    return "en"  # По умолчанию - английский язык


def caesar_cipher(text: str, shift: int, alphabet: str) -> str:
    """
    Применяет шифр Цезаря к входному тексту.
    
    Аргументы:
        text: Исходный текст для преобразования
        shift: Величина сдвига (положительная для сдвига вправо, отрицательная - влево)
        alphabet: Алфавит для подстановки
        
    Возвращает:
        Преобразованный текст с сохранением:
        - регистра символов
        - всех неалфавитных знаков (пробелы, знаки пунктуации и т.д.)
    """
    alphabet_length = len(alphabet)
    result = []
    
    for char in text:
        lower_char = char.lower()
        # Пропускаем символы, не входящие в алфавит
        if lower_char not in alphabet:
            result.append(char)
            continue
            
        # Рассчитываем новую позицию символа с учетом циклического сдвига
        original_index = alphabet.index(lower_char)
        new_index = (original_index + shift) % alphabet_length
        new_char = alphabet[new_index]
        
        # Сохраняем оригинальный регистр символа
        result.append(new_char.upper() if char.isupper() else new_char)
        
    return "".join(result)


# Получение входных данных от пользователя
text_orig = input("Введите текст для обработки: ")
operation = input(
    "Выберите операцию:\n"
    "1 - зашифровать текст\n"
    "2 - расшифровать текст\n"
    "Ваш выбор: "
).strip()
shift = int(input(
    "Введите величину сдвига (рекомендуется не превышать длину алфавита: "
    "26 для англ., 33 для рус.): "
))
shift_direction = input(
    "Укажите направление сдвига:\n"
    "left - сдвиг влево\n"
    "right - сдвиг вправо\n"
    "Ваш выбор: "
).lower().strip()

# Валидация введенных данных
if operation not in ("1", "2"):
    raise ValueError("Некорректный выбор операции. Допустимы только значения 1 или 2")
if shift_direction not in ("left", "right"):
    raise ValueError("Некорректное направление сдвига. Используйте 'left' или 'right'")

# Определение языка и алфавита
language = detect_language(text_orig)
alphabet = RUSSIAN_ALPHABET if language == "ru" else ENGLISH_ALPHABET

# Расчет эффективного сдвига с учетом операции и направления
if operation == "1":  # Шифрование
    effective_shift = shift if shift_direction == "right" else -shift
else:  # Расшифровка
    effective_shift = -shift if shift_direction == "right" else shift

# Обработка текста и вывод результата
result_text = caesar_cipher(text_orig, effective_shift, alphabet)
print("\nОперация успешно завершена! Результат:")
print(result_text)
