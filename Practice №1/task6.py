n = int(input())
current_length = 0
digit_length = 1

while True:
    numbers_count = 9 * (10 ** (digit_length - 1))
    total_digits = numbers_count * digit_length
    
    if n <= current_length + total_digits:
        break
    
    current_length += total_digits
    digit_length += 1

n -= current_length
number = 10 ** (digit_length - 1) + (n - 1) // digit_length
position = (n - 1) % digit_length
result = str(number)[position]
print(result)
