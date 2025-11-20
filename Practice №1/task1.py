
celsius = float(input("Введите температуру в цельсиях: "))

fahrenheit = round((celsius * 9/5) + 32, 2)
kelvin = round(celsius + 273.15, 2)

print(f'{celsius} C = {fahrenheit} F')
print(f'{celsius} C = {kelvin} K')
