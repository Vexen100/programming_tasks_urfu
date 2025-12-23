"""
Модели для работы с вакансиями HeadHunter.
"""
from django.db import models


class Category(models.Model):
    """Категория (профессиональная роль) вакансии."""
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class City(models.Model):
    """Город размещения вакансии."""
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Employer(models.Model):
    """Работодатель (компания)."""
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Работодатель"
        verbose_name_plural = "Работодатели"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Vacancy(models.Model):
    """
    Вакансия с HeadHunter.
    
    Хранит основную информацию: название, описание, зарплату,
    а также связи с категорией, городом и работодателем.
    """
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, default="")
    salary_lower = models.IntegerField(default=0, null=True)
    salary_upper = models.IntegerField(default=0, null=True)
    
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='vacancies'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='vacancies'
    )
    employer = models.ForeignKey(
        Employer,
        on_delete=models.CASCADE,
        related_name='vacancies'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ['-id']
    
    def __str__(self):
        return self.name
    
    def get_salary_display(self):
        """Возвращает отформатированную строку с зарплатой."""
        if self.salary_lower and self.salary_upper:
            if self.salary_lower == self.salary_upper:
                return f"{self.salary_lower:,} руб."
            return f"{self.salary_lower:,} - {self.salary_upper:,} руб."
        elif self.salary_lower:
            return f"от {self.salary_lower:,} руб."
        elif self.salary_upper:
            return f"до {self.salary_upper:,} руб."
        return "Не указана"
