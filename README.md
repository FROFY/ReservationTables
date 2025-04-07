# ReservationTables

ReservationTables — это API-сервис для бронирования столиков в заведении.  
Проект построен на основе FastAPI и использует асинхронный стек технологий.

Основные технологии:

- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Redis
- Poetry
- Docker / Docker Compose

--------------------------------

## Установка и настройка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/FROFY/ReservationTables.git
    ```

2. Перейдите в папку с проектом:
    ```bash
    cd ReservationTables
    ```

3. Установите зависимости с помощью Poetry:
    ```bash
    poetry install
    ```

4. Создайте файл `.env` на основе `.env.example` и заполните переменные окружения, например:
    ```bash
    cp .env.example .env
    ```

5. Если запуск через docker-compose, то создайте образы и запустите контейнеры (не забудьте подготовить отдельный .env
   файл:
   ```bash
    docker-compose up -d --build
    ```

6. После поднятия контейнеров, можно выполнить миграции:
    ```bash
    alembic revision --autogenerate
    ```
   ```bash
    alembic upgrade head
    ```

7. Запустите приложение (если запуск без Docker):
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

Теперь ваше приложение доступно по адресу `http://localhost:8000`.
