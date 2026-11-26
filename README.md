# Learning Log

Учебный проект на Django: журнал, в котором пользователь ведёт темы и записи по ним.

## Возможности
- регистрация, вход и выход;
- темы и записи (создание, просмотр, редактирование записей);
- каждый пользователь видит только свои темы (чужие — ошибка 404);
- административная панель Django;
- оформление на Bootstrap 5.

## Запуск

```bash
# 1. Виртуальное окружение
python -m venv ll_env
# Windows:       ll_env\Scripts\activate
# Linux / macOS: source ll_env/bin/activate

# 2. Зависимости
pip install -r requirements.txt

# 3. База данных
python manage.py makemigrations learning_logs
python manage.py migrate

# 4. Администратор (для входа в /admin/)
python manage.py createsuperuser

# 5. Сервер
python manage.py runserver
```

Сайт: http://127.0.0.1:8000/ · Админка: http://127.0.0.1:8000/admin/

## Тесты
```bash
python manage.py test
```

## Структура
```
learning_log/
├── manage.py
├── requirements.txt
├── ll_project/        # настройки и корневые маршруты
├── learning_logs/     # модели Topic и Entry, представления, шаблоны
└── accounts/          # вход, выход, регистрация
```

