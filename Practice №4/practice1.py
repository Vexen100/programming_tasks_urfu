class Employee:
    def __init__(self, name, id, hourly_rate, hours):
        self.name = name
        self.id = id
        self.hourly_rate = hourly_rate
        self.hours = hours

    def salary(self):
        return self.hours * self.hourly_rate

    def info(self):
        return f'Name: {self.name}, ID: {self.id}'


class Manager(Employee):
    def __init__(self, name, id, hourly_rate, hours, team_bonus):
        super().__init__(name, id, hourly_rate, hours)
        self.team_bonus = team_bonus

    def salary(self):
        return self.hours * self.hourly_rate + (self.team_bonus * 3000)


class Developer(Employee):
    def __init__(self, name, id, hourly_rate, hours, skill_bonus):
        super().__init__(name, id, hourly_rate, hours)
        self.skill_bonus = skill_bonus

    def salary(self):
        return self.hours * self.hourly_rate + (self.skill_bonus * 50000)
