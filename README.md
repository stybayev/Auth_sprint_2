## Инструкция по запуску приложения:

1) Клонируем репозиторий:
   ```
   git clone git@github.com:stybayev/Auth_sprint_2.git
   ```
2) Заходим в корневую директрию проекта `/Auth_sprint_2`:
   ```
   cd Auth_sprint_2
   ```
3) Создаем файл `.env` и копируем в него содержимое файла `.env.example`:
   ```
   cp .env.example .env
   ```
4) Запускаем сервисы:
   ```
   docker-compose -f docker-compose.dev.yml  up --build 
   ```
5) Все должно работать!

## Сервисы приложения:

### Сервис Auth

Этот сервис предназначен для управления аутентификацией и авторизацией пользователей.

С его помощью можно:

- Регистрировать пользователей.
- Выполнять вход в аккаунт и получать пару токенов (JWT-access и refresh токены).
- Обновлять access-токен.
- Выполнять выход из аккаунта.
- Изменять логин или пароль пользователя.
- Получать историю входов пользователя.
- Управлять ролями пользователей.

**Адрес:**

```
http://127.0.0.1/api/auth/openapi
```

**Добавление суперпользователя в систему:**

Для добавления суперпользователя необходимо ввести следующую команду (admin - логин пользователя, password - пароль
пользователя:

```
python auth/core/su.py admin password
```

### Сервис Django Admin

Этот сервис предназначен для управления контентом фильмов через административный интерфейс.

С помощью него можно:

- Загрузить фильм в базу данных.
- Редактировать информацию о фильме.
- Управлять жанрами и персонами.
- Просматривать подробную информацию о фильмах.

**Адрес:**

```
http://127.0.0.1/admin
```

### Cервис выдачи контента

Этот сервис предназначен для управления и предоставления информации о фильмах.

С помощью него можно:

- Получать список всех доступных фильмов.
- Получать подробную информацию о конкретном фильме.

**Адрес:**

```
http://127.0.0.1/api/films/openapi
```

### Cервис FileApi

Этот сервис предназначен для работы с файлами.

С его помощью можно:

- Загружать файлы на сервер.
- Скачивать файлы с сервера.

**Адрес:**

```
http://127.0.0.1/api/files/openapi
```

### Jaeger

Jaeger используется для трассировки запросов в микросервисной архитектуре.

**Адрес:**

```
http://127.0.0.1:16686
```

## Инструкция по запуску тестов

1. **Переход в директорию тестов:**

   Навигация к папке с тестами.
   ```bash
   cd tests/unit

2. **Запуск тестовых сервисов:**

   Используйте docker-compose для запуска тестов.
   ```bash
   docker-compose -f docker-compose.yml up --build

3. **Остановка и очистка тестовой среды:**

   После завершения тестирования рекомендуется остановить контейнеры и очистить созданные ресурсы.

   ```bash
   docker-compose down -v
