# ***Парсер 10 объявлений с сайта https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/***
___________________
## **Проект работает с Docker**

## Для запуска проекта необходимо:
### 1. Установить `docker`
### 2. Скачать проект себе на компьютер
### 3. Переименовать файл `.env.example` в `.env` и внести в него необходимые зависимости проекта 
### 4. Выполнить команду: `docker-compose up -d`
### 5. Для создания суперпользователя выполнить команду: `docker exec -it django python manage.py csu` 
### 6. **Перейти по ссылке http://localhost:8000/ для просмотра интеактивной докментации**
### ***`Логин: admin, пароль: admin суперпользователя`***
___
## Используемый стек: Docker, Docker-compose, Python 3.12, selenium, Django DRF, drf-yasg, beautifulsoup4, psycopg2
