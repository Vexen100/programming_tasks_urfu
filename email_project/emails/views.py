import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from .models import Email, Folder


def email_to_dict(email, include_body=True):
    """Преобразует объект Email в словарь для JSON-ответа.

    Args:
        email: Объект модели Email
        include_body: Включать ли текст письма в ответ

    Returns:
        dict: Данные письма
    """
    data = {
        'id': email.id,
        'sender': email.sender,
        'recipient': email.recipient,
        'subject': email.subject,
        'folder': email.folder,
        'folder_display': email.get_folder_display(),
        'is_read': email.is_read,
        'created_at': email.created_at.isoformat(),
        'updated_at': email.updated_at.isoformat(),
    }
    if include_body:
        data['body'] = email.body
    return data


@csrf_exempt
def email_list(request):
    """Список всех писем или создание нового.

    GET: Возвращает список писем с пагинацией.
         Параметры: page (номер страницы), folder (фильтр по папке)
    POST: Создаёт новое письмо (отправка).
    """
    if request.method == 'GET':
        queryset = Email.objects.all()

        folder = request.GET.get('folder')
        if folder in dict(Folder.choices):
            queryset = queryset.filter(folder=folder)

        paginator = Paginator(queryset, 20)
        page = paginator.get_page(request.GET.get('page', 1))

        return JsonResponse({
            'results': [email_to_dict(e, include_body=False) for e in page],
            'total': paginator.count,
            'page': page.number,
            'pages': paginator.num_pages,
        })

    # POST — отправка письма
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Некорректный JSON'}, status=400)

    # Валидация
    errors = {}

    sender = data.get('sender', '').strip().lower()
    if not sender or '@' not in sender:
        errors['sender'] = 'Некорректный email отправителя'

    recipient = data.get('recipient', '').strip().lower()
    if not recipient or '@' not in recipient:
        errors['recipient'] = 'Некорректный email получателя'

    subject = data.get('subject', '').strip()
    if not subject:
        errors['subject'] = 'Тема не может быть пустой'

    body = data.get('body', '').strip()
    if not body:
        errors['body'] = 'Текст письма не может быть пустым'

    if errors:
        return JsonResponse({'errors': errors}, status=400)

    # Создаём письмо
    email = Email.objects.create(
        sender=sender,
        recipient=recipient,
        subject=subject,
        body=body,
        folder=Folder.SENT,
        is_read=True
    )

    return JsonResponse(email_to_dict(email), status=201)



def inbox(request):
    """Возвращает список входящих писем."""
    emails = Email.objects.filter(folder=Folder.INBOX)
    paginator = Paginator(emails, 20)
    page = paginator.get_page(request.GET.get('page', 1))

    return JsonResponse({
        'results': [email_to_dict(e, include_body=False) for e in page],
        'total': paginator.count,
        'page': page.number,
        'pages': paginator.num_pages,
    })



def sent(request):
    """Возвращает список исходящих писем."""
    emails = Email.objects.filter(folder=Folder.SENT)
    paginator = Paginator(emails, 20)
    page = paginator.get_page(request.GET.get('page', 1))

    return JsonResponse({
        'results': [email_to_dict(e, include_body=False) for e in page],
        'total': paginator.count,
        'page': page.number,
        'pages': paginator.num_pages,
    })



def email_detail(request, pk):
    """Возвращает данные письма и отмечает его прочитанным.

    Args:
        pk: ID письма
    """
    email = get_object_or_404(Email, pk=pk)
    email.mark_as_read()
    return JsonResponse(email_to_dict(email))


@csrf_exempt
def move_email(request, pk):
    """Перемещает письмо в другую папку.

    Args:
        pk: ID письма

    Тело запроса:
        folder: Код папки (inbox, sent, trash, archive)
    """
    email = get_object_or_404(Email, pk=pk)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Некорректный JSON'}, status=400)

    folder = data.get('folder')
    if folder not in dict(Folder.choices):
        return JsonResponse(
            {'error': f'Недопустимая папка. Допустимые: inbox, sent, trash, archive'},
            status=400
        )

    email.move_to(folder)
    return JsonResponse(email_to_dict(email))


@csrf_exempt
def delete_email(request, pk):
    """Удаляет письмо (мягкое или окончательное).

    Если письмо не в корзине — перемещает в корзину.
    Если в корзине — удаляет окончательно.

    Args:
        pk: ID письма
    """
    email = get_object_or_404(Email, pk=pk)
    email.delete()
    return JsonResponse({}, status=204)