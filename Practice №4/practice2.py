class Vehicle:
    """
    Базовый класс для представления транспортного средства.
    
    Атрибуты:
        model (str): Модель транспортного средства
        year (int): Год выпуска
        max_speed (int): Максимальная скорость в км/ч
    """

    def __init__(self, model, year, max_speed):
        """
        Инициализирует объект транспортного средства.
        
        Параметры:
            model: Наименование модели
            year: Год производства
            max_speed: Предельная скорость
        """
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def description(self):
        """
        Формирует общее описание транспортного средства.
        
        Возвращает:
            str: Строка с основными характеристиками
        """
        return f"Модель: {self.model}, {self.year} год, Макс. скорость: {self.max_speed} км/ч"

    def start(self):
        """
        Имитирует запуск двигателя.
        
        Возвращает:
            str: Сообщение о запуске
        """
        return "Двигатель запущен"

    def stop(self):
        """
        Имитирует остановку двигателя.
        
        Возвращает:
            str: Сообщение об остановке
        """
        return "Двигатель остановлен"

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        
        Возвращает:
            str: Результат вызова метода description
        """
        return self.description()


class Car(Vehicle):
    """
    Класс для представления автомобиля.
    
    Наследует базовый класс Vehicle и добавляет специфические атрибуты.
    
    Атрибуты:
        fuel_type (str): Тип топлива (бензин, дизель и т.д.)
        doors (int): Количество дверей
    """

    def __init__(self, model, year, max_speed, fuel_type, doors):
        """
        Инициализирует объект автомобиля.
        
        Параметры:
            fuel_type: Вид используемого топлива
            doors: Число дверей (обычно 2 или 4)
        """
        super().__init__(model, year, max_speed)
        self.fuel_type = fuel_type
        self.doors = doors

    def description(self):
        """
        Расширяет базовое описание, добавляя информацию об автомобиле.
        
        Возвращает:
            str: Полное описание с указанием типа топлива и числа дверей
        """
        base_description = super().description()
        return f"{base_description} - {self.doors}-дверный автомобиль на {self.fuel_type}"


class Bicycle(Vehicle):
    """
    Класс для представления велосипеда.
    
    Наследует базовый класс Vehicle и добавляет велосипедные особенности.
    
    Атрибуты:
        bicycle_type (str): Тип велосипеда (городской, горный и т.д.)
        gears (int): Количество скоростей
    """

    def __init__(self, model, year, max_speed, bicycle_type, gears):
        """
        Инициализирует объект велосипеда.
        
        Параметры:
            bicycle_type: Вид велосипеда
            gears: Число скоростей
        """
        super().__init__(model, year, max_speed)
        self.bicycle_type = bicycle_type
        self.gears = gears

    def description(self):
        """
        Формирует описание велосипеда.
        
        Возвращает:
            str: Полное описание с указанием типа и количества скоростей
        """
        base_description = super().description()
        return f"{base_description} - {self.bicycle_type} велосипед с {self.gears} скоростями"

    def start(self):
        """
        Перекрывает метод start для велосипеда.
        
        Возвращает:
            str: Специфическое сообщение для велосипеда
        """
        return f"Крути педали!"

    def stop(self):
        """
        Перекрывает метод stop для велосипеда.
        
        Возвращает:
            str: Юмористическое сообщение об остановке
        """
        return f'Можешь отдохнуть, слабак!'


class Motorcycle(Vehicle):
    """
    Класс для представления мотоцикла.
    
    Наследует базовый класс Vehicle и добавляет мотоциклетные характеристики.
    
    Атрибуты:
        engine_volume (int): Объем двигателя в кубических сантиметрах (cc)
        motorcycle_type (str): Тип мотоцикла (круизер, спортбайк и т.д.)
    """

    def __init__(self, model, year, max_speed, engine_volume, motorcycle_type):
        """
        Инициализирует объект мотоцикла.
        
        Параметры:
            engine_volume: Рабочий объем двигателя
            motorcycle_type: Категория мотоцикла
        """
        super().__init__(model, year, max_speed)
        self.engine_volume = engine_volume
        self.motorcycle_type = motorcycle_type

    def description(self):
        """
        Формирует описание мотоцикла.
        
        Возвращает:
            str: Полное описание с указанием типа и объема двигателя
        """
        base_description = super().description()
        return f"{base_description} - {self.motorcycle_type} мотоцикл с двигателем {self.engine_volume}cc"

    def start(self):
        """
        Перекрывает метод start для мотоцикла.
        
        Возвращает:
            str: Звуковой эффект запуска двигателя
        """
        return "Врум-врум!"

    def stop(self):
        """
        Перекрывает метод stop для мотоцикла.
        
        Возвращает:
            str: Стандартное сообщение об остановке
        """
        return "Двигатель остановлен"


car = Car('Toyota Camry', 2022, 210, 'бензин', 4)
bicycle = Bicycle("Trek FX 2", 2023, 32, "городской", 21)
motorcycle = Motorcycle("Harley-Davidson Sportster", 2021, 170, 1200, "круизер")

print(car.description())
print(bicycle.description())
print(motorcycle.description())
