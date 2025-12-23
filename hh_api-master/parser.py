"""
Модуль для синхронизации данных о вакансиях с HeadHunter API.
Использует Django ORM для сохранения данных в базу данных.
"""
import os
import sys
import django
import requests
import time
from typing import List, Dict, Optional

# Инициализация Django
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HH_API_DIR = os.path.join(BASE_DIR, 'hh_api')
sys.path.insert(0, HH_API_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hh_api.settings')
django.setup()

from works.models import Category, City, Employer, Vacancy


class HeadHunterAPIClient:
    """Клиент для работы с HeadHunter API."""
    
    BASE_URL = "https://api.hh.ru/vacancies"
    HEADERS = {"User-Agent": "JobAggregator/2.1"}
    ITEMS_PER_PAGE = 100
    REQUEST_TIMEOUT = 15
    DELAY_BETWEEN_REQUESTS = 0.25  # Задержка для соблюдения rate limit
    
    def __init__(self, max_pages: int = 10):
        self.max_pages = max_pages
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)
    
    def get_vacancies_page(self, page: int) -> Optional[Dict]:
        """Получает одну страницу вакансий."""
        params = {
            "text": "",
            "page": page,
            "per_page": self.ITEMS_PER_PAGE,
        }
        
        try:
            response = self.session.get(
                self.BASE_URL,
                params=params,
                timeout=self.REQUEST_TIMEOUT
            )
            response.raise_for_status()
            time.sleep(self.DELAY_BETWEEN_REQUESTS)
            return response.json()
        except requests.RequestException as e:
            print(f"Ошибка получения страницы {page}: {e}")
            return None
    
    def get_all_vacancies(self) -> List[Dict]:
        """Получает все вакансии с указанного количества страниц."""
        all_items = []
        
        for page_num in range(self.max_pages):
            page_data = self.get_vacancies_page(page_num)
            if page_data and "items" in page_data:
                all_items.extend(page_data["items"])
                print(f"Загружена страница {page_num + 1}/{self.max_pages}")
            else:
                break
        
        return all_items
    
    def get_vacancy_full_info(self, vacancy_id: int) -> Optional[Dict]:
        """Получает полную информацию о конкретной вакансии."""
        try:
            url = f"{self.BASE_URL}/{vacancy_id}"
            response = self.session.get(url, timeout=self.REQUEST_TIMEOUT)
            response.raise_for_status()
            time.sleep(self.DELAY_BETWEEN_REQUESTS)
            return response.json()
        except requests.RequestException as e:
            print(f"Ошибка получения деталей вакансии {vacancy_id}: {e}")
            return None


class VacancyDataProcessor:
    """Обработчик данных вакансий для сохранения в БД."""
    
    @staticmethod
    def extract_city_data(vacancy: Dict) -> Optional[Dict]:
        """Извлекает данные о городе из вакансии."""
        area = vacancy.get("area")
        if area and "id" in area and "name" in area:
            return {"id": area["id"], "name": area["name"]}
        return None
    
    @staticmethod
    def extract_employer_data(vacancy: Dict) -> Optional[Dict]:
        """Извлекает данные о работодателе."""
        employer = vacancy.get("employer")
        if employer and "id" in employer and "name" in employer:
            return {"id": employer["id"], "name": employer["name"]}
        return None
    
    @staticmethod
    def extract_category_data(vacancy: Dict) -> Optional[Dict]:
        """Извлекает данные о категории (профессиональной роли)."""
        roles = vacancy.get("professional_roles", [])
        if roles and len(roles) > 0:
            role = roles[0]
            if "id" in role and "name" in role:
                return {"id": role["id"], "name": role["name"]}
        return None
    
    @staticmethod
    def extract_salary_data(vacancy: Dict) -> tuple:
        """Извлекает данные о зарплате."""
        salary = vacancy.get("salary")
        if not salary:
            return (None, None)
        return (salary.get("from"), salary.get("to"))


class VacancyRepository:
    """Репозиторий для работы с вакансиями в базе данных."""
    
    @staticmethod
    def get_or_create_city(city_data: Dict) -> Optional[City]:
        """Получает или создает город."""
        try:
            city, _ = City.objects.get_or_create(
                id=city_data["id"],
                defaults={"name": city_data["name"]}
            )
            return city
        except Exception as e:
            print(f"Ошибка работы с городом: {e}")
            return None
    
    @staticmethod
    def get_or_create_employer(employer_data: Dict) -> Optional[Employer]:
        """Получает или создает работодателя."""
        try:
            employer, _ = Employer.objects.get_or_create(
                id=employer_data["id"],
                defaults={"name": employer_data["name"]}
            )
            return employer
        except Exception as e:
            print(f"Ошибка работы с работодателем: {e}")
            return None
    
    @staticmethod
    def get_or_create_category(category_data: Dict) -> Optional[Category]:
        """Получает или создает категорию."""
        try:
            category, _ = Category.objects.get_or_create(
                id=category_data["id"],
                defaults={"name": category_data["name"]}
            )
            return category
        except Exception as e:
            print(f"Ошибка работы с категорией: {e}")
            return None
    
    @staticmethod
    def save_vacancy(vacancy_data: Dict, full_info: Dict) -> bool:
        """Сохраняет вакансию в базу данных."""
        try:
            processor = VacancyDataProcessor()
            
            city_data = processor.extract_city_data(vacancy_data)
            employer_data = processor.extract_employer_data(vacancy_data)
            category_data = processor.extract_category_data(vacancy_data)
            
            if not all([city_data, employer_data, category_data]):
                return False
            
            city = VacancyRepository.get_or_create_city(city_data)
            employer = VacancyRepository.get_or_create_employer(employer_data)
            category = VacancyRepository.get_or_create_category(category_data)
            
            if not all([city, employer, category]):
                return False
            
            description = full_info.get("description", "") if full_info else ""
            salary_from, salary_to = processor.extract_salary_data(vacancy_data)
            
            Vacancy.objects.update_or_create(
                id=int(vacancy_data["id"]),
                defaults={
                    "name": vacancy_data["name"],
                    "description": description,
                    "salary_lower": salary_from or 0,
                    "salary_upper": salary_to or 0,
                    "city": city,
                    "category": category,
                    "employer": employer,
                }
            )
            return True
        except (KeyError, ValueError, TypeError) as e:
            print(f"Ошибка обработки данных: {e}")
            return False
        except Exception as e:
            print(f"Неожиданная ошибка при сохранении: {e}")
            return False


def main():
    """Главная функция для синхронизации данных с HeadHunter."""
    print("=" * 60)
    print("Синхронизация вакансий с HeadHunter API")
    print("=" * 60)
    
    api_client = HeadHunterAPIClient(max_pages=1)
    repository = VacancyRepository()
    
    # Получаем список вакансий
    print("\nЭтап 1: Загрузка списка вакансий...")
    vacancies_list = api_client.get_all_vacancies()
    total_vacancies = len(vacancies_list)
    print(f"Загружено вакансий для обработки: {total_vacancies}\n")
    
    if not vacancies_list:
        print("Не удалось загрузить вакансии. Проверьте подключение к интернету.")
        return
    
    # Обрабатываем каждую вакансию
    print("Этап 2: Получение детальной информации и сохранение...")
    saved_count = 0
    failed_count = 0
    
    for idx, vacancy_item in enumerate(vacancies_list, 1):
        try:
            vacancy_id = int(vacancy_item["id"])
            full_info = api_client.get_vacancy_full_info(vacancy_id)
            
            if repository.save_vacancy(vacancy_item, full_info):
                saved_count += 1
            else:
                failed_count += 1
            
            # Прогресс каждые 50 вакансий
            if idx % 50 == 0:
                progress = (idx / total_vacancies) * 100
                print(f"Прогресс: {idx}/{total_vacancies} ({progress:.1f}%) | "
                      f"Сохранено: {saved_count} | Ошибок: {failed_count}")
        except Exception as e:
            print(f"Критическая ошибка при обработке вакансии {idx}: {e}")
            failed_count += 1
    
    # Итоговая статистика
    print("\n" + "=" * 60)
    print("Синхронизация завершена")
    print("=" * 60)
    print(f"Всего обработано: {total_vacancies}")
    print(f"Успешно сохранено: {saved_count}")
    print(f"Ошибок: {failed_count}")
    print("=" * 60)


if __name__ == "__main__":
    main()
