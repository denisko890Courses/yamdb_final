# YamDB [![Django-app workflow](https://github.com/denisko890Courses/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/denisko890Courses/yamdb_final/actions/workflows/yamdb_workflow.yml)

Ссылка на продакшн: http://84.201.178.155/admin
Описание проекта
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий может быть расширен администратором.

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку. В каждой категории есть произведения: книги, фильмы или музыка.

Произведению может быть присвоен жанр из списка предустановленных. Новые жанры может создавать только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти; из пользовательских оценок формируется усреднённая оценка произведения — рейтинг. На одно произведение пользователь может оставить только один отзыв.

Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
git clone https://github.com/denisko890Courses/yamdb_final
Заполните .env файл в папке infra
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
DOCKER_CLIENT_TIMEOUT=180
COMPOSE_HTTP_TIMEOUT=180
Запустите docker-compose с помощью следующих команд
docker-compose up -d --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
Можете заполнить базу данных тестовыми данными
docker-compose exec web python manage.py loaddata /app/fixtures.json
Технологии, использованные в процессе создания проекта
Python 3.7
Django 2.2.16
DjangoRestFramework 3.12.4
DjangoFilter 2.4.0
Pytest 6.2.4
SQLite
Simple JWT
Docker
Docker-compose
После запуска проекта по адресу http://localhost/redoc/ будет доступна документация. В ней описаны всевозможные запросы к API, кторые должны были быть реализовны в проекте.
