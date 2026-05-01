# To-Do FastAPI

Простое REST API для управления задачами (To-Do).  
Учебный проект, демонстрирующий базовые возможности **FastAPI**, **SQLAlchemy** (ORM), **PostgreSQL** и **Pydantic**.

---

## 📦 Стек технологий

- Python 3.13+
- FastAPI – веб-фреймворк
- SQLAlchemy (ORM) – работа с базой данных
- Pydantic – валидация данных
- PostgreSQL – база данных
- Uvicorn – ASGI-сервер

---

## 🚀 Возможности (API)

- ✅ Получить все задачи – `GET /tasks/`
- ✅ Получить одну задачу – `GET /tasks/{id}`
- ✅ Создать задачу – `POST /tasks/`
- ✅ Обновить задачу – `PUT /tasks/{id}`
- ✅ Удалить задачу – `DELETE /tasks/{id}`

Поля задачи:
- `title` – название (обязательное)
- `description` – описание (опциональное)
- `is_active` – активна ли задача (по умолчанию `true`)

---

## 🛠 Установка и запуск

### 1. Клонировать репозиторий
```bash
git clone https://github.com/ArbeKenn/Todo_List.git
cd to-do-fastapi
```

### 2. Создать виртуальное окружение
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

### 4. Настроить переменные окружения
Создай файл .env в корне проекта:
```bash
DATABASE_URL=postgresql://username:password@localhost:5432/db_name
```
Замени username, password, localhost, 5432, db_name на свои.

### 5. Запустить приложение
```bash
cd app
fastapi def main.py
```
После запуска открой в браузере:

Swagger UI: http://localhost:8000/docs

## 📁 Структура проекта
```text
Todo_List/
├── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI приложение
│   ├── database.py           # Подключение к БД
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py           # SQLAlchemy модель Task
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── schemas.py        # Pydantic схемы
│   └── routers/
│       ├── __init__.py
│       └── tasks.py          # Эндпоинты (CRUD)
├── .env                      # Переменные окружения
├── .gitignore
├── requirements.txt          # Библиотеки
└── README.md
```

## 📝 Что нужно доработать
• Добавить асинхронные эндпоинты (async/await)

• Написать тесты (pytest)

• Добавить аутентификацию (JWT)

• Подключить Alembic для миграций

## 👤 Автор
Bektemir – [GitHub](https://github.com/ArbeKenn) – [Telegram](https://t.me/ArbeKenn) – [Email](mailto:bektemir1102@gmail.com)