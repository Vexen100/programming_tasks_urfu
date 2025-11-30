import requests


def print_pokemons_list(limit: int):
    """
    Выполняет запрос для получения списка покемонов

    :param limit: ограничение на количество выводимых покемонов
    """
    # Формируем параметры запроса
    query_params = {'limit': limit}
    api_response = requests.get('https://pokeapi.co/api/v2/pokemon/', query_params)
    if api_response.status_code == 200:
        # Парсим и выводим полученные данные
        pokemon_data = api_response.json()["results"]
        print(f'Список первых {limit} покемонов')
        for num, creature in enumerate(pokemon_data):
            print(f'{num+1}. {creature["name"]}')


def print_pokemon(index: str):
    """
    Отображает детальную информацию о конкретном покемоне

    :param index: идентификатор или имя покемона
    для получения детальной информации
    """
    # Выполняем запрос к API для получения данных покемона
    pokemon_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{index}')
    pokemon_info = pokemon_response.json()

    if pokemon_response.status_code == 200:
    # Форматируем и выводим полученную информацию
        print('Результат поиска:')
        print(f'Имя: {pokemon_info["name"]}')
        type_list = [type_entry["type"]["name"] for type_entry in pokemon_info['types']]
        print(f'Тип: {", ".join(type_list)}')
        print(f'Вес: {pokemon_info["weight"]}')
        print(f'Рост: {pokemon_info["height"]}')
        ability_list = [
            ability_entry['ability']['name'] for ability_entry in pokemon_info['abilities']
        ]
        print(f'Способности: {", ".join(ability_list)}')
        move_list = [move_entry['move']['name'] for move_entry in pokemon_info['moves']]
        print(f'Ходы: {", ".join(move_list)}')


print_pokemons_list(5)
print_pokemon(input('Введите номер или имя покемона для подробной информации: '))
