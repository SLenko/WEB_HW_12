app/: Основна папка додатку.
app/api/: Тут зберігається весь API.
app/api/auth.py: Містить логіку аутентифікації користувачів.
app/api/contacts/: Каталог для операцій, що стосуються контактів.
app/api/contacts/__init__.py: Позначає каталог contacts як пакет Python.
app/api/contacts/crud.py: Містить функції для операцій CRUD з контактами.
app/api/contacts/models.py: Моделі даних контактів.
app/api/contacts/schemas.py: Схеми Pydantic для валідації даних контактів.
app/api/contacts/main.py: Основний файл для реалізації маршрутів та операцій з контактами.
app/api/users/: Каталог для операцій, що стосуються користувачів.
app/api/users/__init__.py: Позначає каталог users як пакет Python.
app/api/users/crud.py: Містить функції для операцій CRUD з користувачами.
app/api/users/models.py: Моделі даних користувачів.
app/api/users/schemas.py: Схеми Pydantic для валідації даних користувачів.
app/api/users/tokens.py: Функції для створення та перевірки JWT токенів.
app/api/users/utils.py: Вспоміжні функції, наприклад, для хешування паролів.
app/db/: Тут знаходяться файли для роботи з базою даних.
app/db/__init__.py: Позначає каталог db як пакет Python.
app/db/base.py: Базовий клас для моделей даних SQLAlchemy.
app/db/session.py: Конфігурація сесії для роботи з базою даних.
app/main.py: Основний файл додатка, де ініціалізується FastAPI та включається маршрутизатор API.
