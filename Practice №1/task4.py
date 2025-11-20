text = input().lower()
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
for i in range(3):
    print(sorted_chars[i][0])
