"""
Представления для работы с вакансиями.
"""
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Vacancy, Category, City, Employer


ITEMS_PER_PAGE = 10


class VacancyListView(View):
    """Представление для отображения списка всех вакансий."""
    
    template_name = "works/index.html"
    
    def get(self, request):
        """Обработка GET-запроса для списка вакансий."""
        page_number = request.GET.get("page", 1)
        
        queryset = Vacancy.objects.select_related(
            "category", "city", "employer"
        ).all()
        
        total_count = queryset.count()
        paginator = Paginator(queryset, ITEMS_PER_PAGE)
        
        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        
        context = {
            "vacancies": page_obj,
            "vacancies_count": total_count
        }
        
        return render(request, self.template_name, context)


class VacancyDetailView(View):
    """Представление для отображения детальной информации о вакансии."""
    
    template_name = "works/detail.html"
    
    def get(self, request, vacancy_id):
        """Обработка GET-запроса для детальной страницы."""
        vacancy = get_object_or_404(
            Vacancy.objects.select_related("category", "city", "employer"),
            pk=vacancy_id
        )
        
        context = {
            "vacancy": vacancy
        }
        
        return render(request, self.template_name, context)


class VacancySearchView(View):
    """Представление для поиска и фильтрации вакансий."""
    
    template_name = "works/search.html"
    
    def get_queryset(self, request):
        """Формирует queryset на основе параметров запроса."""
        queryset = Vacancy.objects.select_related(
            "category", "city", "employer"
        )
        
        # Текстовый поиск
        search_query = request.GET.get("q", "").strip()
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        
        # Фильтры
        filters = {}
        for filter_name in ["category", "city", "employer"]:
            filter_value = request.GET.get(filter_name, "")
            if filter_value:
                try:
                    filters[f"{filter_name}_id"] = int(filter_value)
                except ValueError:
                    pass
        
        if filters:
            queryset = queryset.filter(**filters)
        
        # Сортировка
        sort_option = request.GET.get("sort", "")
        sort_mapping = {
            "newest": ["-id"],
            "salary_desc": ["-salary_lower", "-salary_upper"],
            "salary_asc": ["salary_lower", "salary_upper"],
        }
        order_by = sort_mapping.get(sort_option, ["-id"])
        queryset = queryset.order_by(*order_by)
        
        return queryset, search_query, sort_option
    
    def get(self, request):
        """Обработка GET-запроса для поиска."""
        queryset, query, sort = self.get_queryset(request)
        
        # Пагинация
        total_count = queryset.count()
        paginator = Paginator(queryset, ITEMS_PER_PAGE)
        page_number = request.GET.get("page", 1)
        
        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        
        # Данные для фильтров
        filter_data = {
            "categories": Category.objects.all().order_by('name'),
            "cities": City.objects.all().order_by('name'),
            "employers": Employer.objects.all().order_by('name'),
        }
        
        # Выбранные значения фильтров
        selected_filters = {
            "selected_category": request.GET.get("category", ""),
            "selected_city": request.GET.get("city", ""),
            "selected_employer": request.GET.get("employer", ""),
        }
        
        context = {
            "vacancies": page_obj,
            "vacancies_count": total_count,
            "query": query,
            "sort": sort,
            **filter_data,
            **selected_filters,
        }
        
        return render(request, self.template_name, context)


# Функции-обёртки для обратной совместимости с URL
def index(request):
    """Обёртка для VacancyListView."""
    view = VacancyListView()
    return view.get(request)


def work_detail(request, pk):
    """Обёртка для VacancyDetailView."""
    view = VacancyDetailView()
    return view.get(request, pk)


def search_work(request):
    """Обёртка для VacancySearchView."""
    view = VacancySearchView()
    return view.get(request)
