num = int(input("Введите целое число: "))

print('Чётное') if num%2==0 else print('Нечётное')

if num < 0:
    print("Отрицательное")
elif num == 0:
    print("Является нулём")
else:
    print("Положительное")

print("Принадлежит диапозону [10, 50]") if n in range(10, 51) else print("Не принадлежит диапозону [10, 50]")
