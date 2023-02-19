## Онлайн платформа торговой сети электроники.

### Тестовое задание для старта трудоустройства.

 - Python
 - Django
 - DRF
 - PostgreSQL

#### Для запуска проекта необходимо:

1. скопировать репозиторий - 'git clone https://github.com/KeitoAV/test_project'
2. создать виртуальное окружение;
3. установить зависимости;
4. создать файл .env и заполнить в нём переменные окружения, как в .env.example;
5. 'docker run --name test_project -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres' - настроить подключение к БД;
6. 'python manage.py makemigrations' - создать миграции;
7. 'python manage.py migrate' - применить миграции;
8. 'python manage.py createsuperuser' - создать суперпользователя;
9. 'python manage.py runserver' - запустить проект.
