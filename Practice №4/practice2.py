class Vehicle:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def description(self):
        return f"Модель: {self.model}, {self.year} год, Макс. скорость: {self.max_speed} км/ч"

    def start(self):
        return "Двигатель запущен"

    def stop(self):
        return "Двигатель остановлен"

    def __str__(self):
        return self.description()


class Car(Vehicle):
    def __init__(self, model, year, max_speed, fuel_type, doors):
        super().__init__(model, year, max_speed)
        self.fuel_type = fuel_type
        self.doors = doors

    def description(self):
        base_description = super().description()
        return f"{base_description} - {self.doors}-дверный автомобиль на {self.fuel_type}"


class Bicycle(Vehicle):
    def __init__(self, model, year, max_speed, bicycle_type, gears):
        super().__init__(model, year, max_speed)
        self.bicycle_type = bicycle_type
        self.gears = gears

    def description(self):
        base_description = super().description()
        return f"{base_description} - {self.bicycle_type} велосипед с {self.gears} скоростями"

    def start(self):
        return f"Крути педали!"

    def stop(self):
        return f'Можешь отдохнуть, слабак!'


class Motorcycle(Vehicle):
    def __init__(self, model, year, max_speed, engine_volume, motorcycle_type):
        super().__init__(model, year, max_speed)
        self.engine_volume = engine_volume
        self.motorcycle_type = motorcycle_type

    def description(self):
        base_description = super().description()
        return f"{base_description} - {self.motorcycle_type} мотоцикл с двигателем {self.engine_volume}cc"

    def start(self):
        return "Врум-врум!"

    def stop(self):
        return "Двигатель остановлен"


car = Car('Toyota Camry', 2022, 210, 'бензин', 4)
bicycle = Bicycle("Trek FX 2", 2023, 32, "городской", 21)
motorcycle = Motorcycle("Harley-Davidson Sportster", 2021, 170, 1200, "круизер")

print(car.description())
print(bicycle.description())
print(motorcycle.description())
