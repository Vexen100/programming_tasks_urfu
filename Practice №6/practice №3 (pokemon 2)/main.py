import requests


class Pokemon:
    """Представляет существо покемона с его характеристиками и боевыми способностями"""

    def __init__(self, identifier):
        """
        Создает новый экземпляр покемона.

        :param identifier: уникальный идентификатор для поиска
        данных о покемоне в API
        """
        # Запрашиваем информацию о покемоне
        data_response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{identifier}")
        creature_info = data_response.json()
        
        # Заполняем характеристики
        self.name = creature_info["name"]
        self.types = [element["type"]["name"] for element in creature_info["types"]]
        self.weight = creature_info["weight"]
        self.height = creature_info["height"]
        self.abilities = [
            talent["ability"]["name"] for talent in creature_info["abilities"]
        ]
        self.moves = [technique["move"]["name"] for technique in creature_info["moves"]]
        
        # Обрабатываем боевые параметры
        for attribute in creature_info["stats"]:
            param_name = attribute["stat"]["name"]
            if param_name == "hp":
                self.hp = int(attribute["base_stat"])
            elif param_name == "attack":
                self.attack = int(attribute["base_stat"])
            elif param_name == "defense":
                self.defense = int(attribute["base_stat"])
        
        # Текущее здоровье в бою
        self.fight_hp = self.hp

    def __str__(self):
        """Возвращает текстовое описание покемона"""
        return (
            f"Покемон: {self.name}, "
            f"Типы: {', '.join(self.types)}, "
            f"Масса: {self.weight}, "
            f"Рост: {self.height}, "
            f"Таланты: {', '.join(self.abilities)} "
            f"Здоровье: {self.hp} "
            f"Сила атаки: {self.attack} "
            f"Защита: {self.defense}."
        )

    def attack_enemy(self, opponent):
        """
        Выполнить атаку на противника.

        :param opponent: покемон, который будет атакован
        """
        return opponent.take_hit(self.attack)

    def take_hit(self, incoming_attack):
        """
        Принять удар от атаки противника.

        :param incoming_attack: мощность атаки противника
        :return: фактический полученный урон
        """
        actual_damage = max(incoming_attack // 2, incoming_attack - self.defense)
        self.fight_hp -= actual_damage
        return actual_damage

    def rest(self):
        """Полностью восстановить здоровье покемона"""
        self.fight_hp = self.hp


class Team:
    """Управляет коллекцией покемонов, составляющих команду"""

    def __init__(self, *members):
        """
        Создает новую команду покемонов.

        :param *members: покемоны, которые будут добавлены
        в команду при создании
        """
        self.members = list(members)

    def add(self, new_member: Pokemon):
        """
        Включить нового покемона в команду.

        :param new_member: покемон для добавления
        """
        for existing_member in self.members:
            if existing_member.name == new_member.name:
                return
        self.members.append(new_member)

    def remove(self, member_name: str):
        """
        Исключить покемона из команды.

        :param member_name: имя покемона для удаления
        """
        for existing_member in self.members:
            if existing_member.name == member_name:
                self.members.remove(existing_member)

    def get_pokemon(self, member_name: str):
        """
        Найти покемона в команде по имени.

        :param member_name: имя искомого покемона
        :return: найденный покемон или None
        """
        for existing_member in self.members:
            if existing_member.name == member_name:
                return existing_member
        return None

    def print_info(self):
        """Отображает полные сведения о всех членах команды"""
        print("\n".join([str(member) for member in self.members]))


def battle_simulation(combatant1: Pokemon, combatant2: Pokemon):
    """
    Проводит учебное сражение между двумя покемонами.

    :param combatant1: первый участник сражения
    :param combatant2: второй участник сражения
    """
    if combatant1 is not None and combatant2 is not None:
        print("**************************************")
        print(f"Учебный бой начинается: {combatant1.name} против {combatant2.name}!")
        fighters = [combatant1, combatant2]
        
        while all([fighter.fight_hp > 0 for fighter in fighters]):
            print(
                f"Текущее состояние: {combatant1.name} ({combatant1.fight_hp} HP) "
                f"vs {combatant2.name} ({combatant2.fight_hp} HP)"
            )
            print(f"{fighters[0].name} атакует с силой {fighters[0].attack}")
            damage_dealt = fighters[0].attack_enemy(fighters[1])
            print(f"{fighters[1].name} получает {damage_dealt} урона")
            print("**************************************")
            fighters.reverse()
        else:
            winner = max(fighters, key=lambda x: x.fight_hp)
            print(f"Победитель: {winner.name}!")
    else:
        print("Для проведения боя требуются два покемона!")


# Создаем команду и проводим учебный бой
my_squad = Team(Pokemon("golduck"), Pokemon("caterpie"), Pokemon("charmeleon"))
my_squad.add(Pokemon("pikachu"))

pikachu_member = my_squad.get_pokemon("pikachu")
charmeleon_member = my_squad.get_pokemon("charmeleon")
battle_simulation(charmeleon_member, pikachu_member)

my_squad.remove("charmeleon")
my_squad.print_info()
