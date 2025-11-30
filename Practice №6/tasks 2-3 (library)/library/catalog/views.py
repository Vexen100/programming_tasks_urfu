from django.shortcuts import render


# Create your views here.
def post_list(request):
    """
    Отображает список книг на странице

    :param request: входящий HTTP-запрос от пользователя
    :return: HttpResponse с заполненным шаблоном
    """
    # Фиктивный набор книг для демонстрации интерфейса
    books = [
        {
            "title": "Пикник на обочине",
            "author": "Стругацкие",
            "content": "Притча о человеческих желаниях",
        },
        {
            "title": "Космические рейнджеры",
            "author": "А. Кларк",
            "content": "Приключения галактической полиции",
        },
    ]

    return render(request, "catalog/book_detail.html", {"books": books})
