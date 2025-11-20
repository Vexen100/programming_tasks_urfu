text = input().lower()
if not text:
    print("Ошибка: пустая строка")
    exit()

char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1 

sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

# если уникальных символов меньше 3
for i in range(min(3, len(sorted_chars))):
    print(sorted_chars[i][0])
