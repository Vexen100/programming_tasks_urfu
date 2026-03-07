from django.db import models


class Folder(models.TextChoices):
    """Папки для хранения писем."""
    INBOX = 'inbox', 'Входящие'
    SENT = 'sent', 'Исходящие'
    TRASH = 'trash', 'Корзина'
    ARCHIVE = 'archive', 'Архив'


class Email(models.Model):
    """Модель электронного письма."""
    sender = models.EmailField('Отправитель')
    recipient = models.EmailField('Получатель')
    subject = models.CharField('Тема', max_length=255)
    body = models.TextField('Текст письма')
    folder = models.CharField(
        'Папка',
        max_length=20,
        choices=Folder.choices,
        default=Folder.INBOX
    )
    is_read = models.BooleanField('Прочитано', default=False)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.subject} — {self.sender}'

    def move_to(self, folder):
        """Перемещает письмо в указанную папку.

        Args:
            folder: Код папки из Folder.choices
        """
        if folder in dict(Folder.choices):
            self.folder = folder
            self.save(update_fields=['folder', 'updated_at'])

    def mark_as_read(self):
        """Отмечает письмо как прочитанное."""
        if not self.is_read:
            self.is_read = True
            self.save(update_fields=['is_read', 'updated_at'])

    def delete(self, *args, **kwargs):
        """Мягкое удаление: в корзину или окончательно."""
        if self.folder == Folder.TRASH:
            super().delete(*args, **kwargs)
        else:
            self.folder = Folder.TRASH
            self.save(update_fields=['folder', 'updated_at'])
