class Employee:
    """
    Базовый класс для представления сотрудника.
    
    Атрибуты:
        name (str): Имя сотрудника
        id (str): Уникальный идентификатор сотрудника
        hourly_rate (float): Почасовая ставка оплаты
        hours (int): Количество отработанных часов
    """

    def __init__(self, name, id, hourly_rate, hours):
        """
        Инициализирует объект сотрудника.
        
        Параметры:
            name: Имя сотрудника
            id: Уникальный идентификатор
            hourly_rate: Почасовая ставка
            hours: Количество отработанных часов
        """
        self.name = name
        self.id = id
        self.hourly_rate = hourly_rate
        self.hours = hours

    def salary(self):
        """
        Рассчитывает заработную плату сотрудника.
        
        Возвращает:
            float: Заработная плата за отработанные часы
        """
        return self.hours * self.hourly_rate

    def info(self):
        """
        Формирует информационную строку о сотруднике.
        
        Возвращает:
            str: Строка с именем и ID сотрудника
        """
        return f'Name: {self.name}, ID: {self.id}'


class Manager(Employee):
    """
    Класс для представления менеджера.
    
    Расширяет базовый класс Employee дополнительным бонусом
    за количество членов в команде.
    
    Атрибуты:
        team_bonus (int): Количество членов команды
    """

    def __init__(self, name, id, hourly_rate, hours, team_bonus):
        """
        Инициализирует объект менеджера.
        
        Параметры:
            team_bonus: Количество подчиненных в команде
        """
        super().__init__(name, id, hourly_rate, hours)
        self.team_bonus = team_bonus

    def salary(self):
        """
        Рассчитывает заработную плату менеджера с учетом командного бонуса.
        
        Возвращает:
            float: Общая заработная плата с бонусом
            (бонус = количество членов команды × 3000)
        """
        return self.hours * self.hourly_rate + (self.team_bonus * 3000)


class Developer(Employee):
    """
    Класс для представления разработчика.
    
    Расширяет базовый класс Employee дополнительным бонусом
    за уровень профессиональных навыков.
    
    Атрибуты:
        skill_bonus (int): Уровень навыков (1-5)
    """

    def __init__(self, name, id, hourly_rate, hours, skill_bonus):
        """
        Инициализирует объект разработчика.
        
        Параметры:
            skill_bonus: Уровень профессиональных навыков (1-5)
        """
        super().__init__(name, id, hourly_rate, hours)
        self.skill_bonus = skill_bonus

    def salary(self):
        """
        Рассчитывает заработную плату разработчика с учетом бонуса за навыки.
        
        Возвращает:
            float: Общая заработная плата с бонусом
            (бонус = уровень навыков × 50000)
        """
        return self.hours * self.hourly_rate + (self.skill_bonus * 50000)
