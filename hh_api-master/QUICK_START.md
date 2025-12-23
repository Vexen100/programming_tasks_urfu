# Быстрый старт

## Минимальные команды для запуска:

```bash
# 1. Установить зависимости
pip install -r requirements.txt

# 2. Перейти в папку Django и выполнить миграции
cd hh_api
python manage.py migrate

# 3. Вернуться в корень и запустить парсер
cd ..
python parser.py

# 4. Запустить сервер
cd hh_api
python manage.py runserver
```

После этого откройте в браузере: **http://127.0.0.1:8000/**

---

**Подробная инструкция:** см. `SETUP_INSTRUCTIONS.md`

