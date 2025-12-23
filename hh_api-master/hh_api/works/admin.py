from django.contrib import admin
from .models import Vacancy, Category, City, Employer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'employer', 'city', 'category', 'salary_lower', 'salary_upper')
    list_filter = ('category', 'city', 'employer')
    search_fields = ('name', 'description', 'employer__name')
    readonly_fields = ('created_at', 'updated_at')
