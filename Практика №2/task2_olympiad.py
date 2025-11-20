def check_winners(scores, student_score):
    """
    Проверяет, попадает ли студент в тройку победителей
    
    Аргументы:
        scores: список баллов всех участников
        student_score: баллы конкретного студента (Стаса)
        
    Выводит сообщение о результате проверки на экран
    """
    ordered_scores = sorted(scores, reverse=True)
    if student_score in ordered_scores[:3]:
        print('Вы в тройке победителей!')
    else:
        print('Вы не попали в тройку победителей.')


# Получение данных от пользователя
scores_input = input(
    'Введите список баллов участников через запятую: '
)
scores_list = list(map(int, scores_input.split(',')))
score_stas = int(input('Введите баллы Стаса: '))

# Проверка результатов
check_winners(scores_list, score_stas)
