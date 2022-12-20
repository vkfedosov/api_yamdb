# Проект YaMDb упакованный в Docker-контейнер

Проект YaMDb собирает отзывы пользователей на различные произведения такие как
фильмы, книги и музыка. Проект упакован в Docker-контейнер.

![](https://github.com/github/docs/actions/workflows/main.yml/badge.svg?event=push)

## Описание проекта:

API YaMDb позволяет работать со следующими сущностями:

* JWT-токен (Auth): отправить confirmation_code на переданный email, получить
  JWT-токен
  в обмен на email и confirmation_code;
* Пользователи (Users): получить список всех пользователей, создать
  пользователя,
  получить пользователя по username, изменить данные пользователя по username,
  удалить
  пользователя по username, получить данные своей учётной записи, изменить
  данные своей учётной записи;
* Произведения (Titles), к которым пишут отзывы: получить список всех объектов,
  создать
  произведение для отзывов, информация об объекте, обновить информацию об
  объекте, удалить произведение.
  пользователя по username, получить данные своей учётной записи, изменить
  данные своей учётной записи;
* Категории (Categories) произведений: получить список всех категорий, создать
  категорию, удалить категорию;
* Жанры (Genres): получить список всех жанров, создать жанр, удалить жанр;
* Отзывы (Review): получить список всех отзывов, создать новый отзыв, получить
  отзыв по id,
  частично обновить отзыв по id, удалить отзыв по id;
* Комментарии (Comments) к отзывам: получить список всех комментариев к отзыву
  по id, создать
  новый комментарий для отзыва, получить комментарий для отзыва по id, частично
  обновить комментарий к отзыву по id, удалить комментарий к отзыву по id.

## Участники проекта:

[vkfedosov](https://github.com/vkfedosov) - управление пользователями (Auth и
Users):
система регистрации и аутентификации, права доступа, работа с токеном, система
подтверждения e-mail, поля;

[Fedoska48](https://github.com/Fedoska48) - категории (Categories), жанры (
Genres)
и произведения (Titles): модели, view и эндпойнты для них;

[LevLM](https://github.com/LevLM) (teamlead) - отзывы (Review) и комментарии (
Comments):
модели и view, эндпойнты, права доступа для запросов. Рейтинги произведений.

## Стек технологий:

* [Python 3.7+](https://www.python.org/downloads/)
* [Django 3.2](https://www.djangoproject.com/download/)
* [PyJWT 2.1.0](https://pypi.org/project/PyJWT/)
* [asgiref 3.3.2](https://pypi.org/project/asgiref/#files)
* [django-filter 2.4.0](https://pypi.org/project/django-filter/#files)
* [djangorestframework-simplejwt 4.8.0](https://pypi.org/project/djangorestframework-simplejwt/)
* [djangorestframework 3.12.4](https://pypi.org/project/djangorestframework/#files)
* [djoser 2.1.0](https://pypi.org/project/djoser/#files)
* [gunicorn 20.0.4](https://pypi.org/project/gunicorn/#files)
* [psycopg2-binary 2.8.6](https://pypi.org/project/psycopg2-binary/#files)
* [pytest-django 4.4.0](https://pypi.org/project/pytest-django/)
* [pytest-pythonpath 0.7.3](https://pypi.org/project/pytest-pythonpath/)
* [pytest 6.2.4](https://pypi.org/project/pytest/)
* [pytz 2020.1](https://pypi.org/project/pytz/#files)
* [requests 2.26.0](https://pypi.org/project/requests/)
* [sqlparse 0.3.1](https://pypi.org/project/sqlparse/#files)

## Как запустить проект:

* Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:vkfedosov/infra_sp2.git
```

```
cd infra_sp2/infra
```

* Создать файл ```.env``` с переменными окружения:

```
# settings.py
SECRET_KEY=<key>               # стандартный ключ, который создается при старте проекта
DEBUG=False                    # опция отладчика True/False
ALLOWED_HOSTS=<host_names>     # список хостов/доменов, для которых дотсупен текущий проект

DB_NAME=postgres               # имя БД
POSTGRES_USER=postgres         # логин для подключения к БД
POSTGRES_PASSWORD=<password>   # пароль для подключения к БД (установите свой)
DB_HOST=db                     # название сервиса (контейнера)
DB_PORT=5432                   # порт для подключения к БД

# default.conf.template
HOST=<server_name>             # имя хоста/домена
PORT=<port>                    # порт для подключения
UPSTREAM=<proxy_pass>          # название сервиса (контейнера):порт
```
* Установить и запустить Docker

* В командной строке выполнить docker-compose.yaml:

```
docker-compose up
```

* Для того, чтобы пересобрать контейнер, в случае изменения файлов проекта,
выполнить команду:

```
docker-compose up -d --build
```

* Создать суперпользователя, при запущенной контейнере web, в командной строке
выполнить команду:

```
docker-compose exec web python manage.py createsuperuser
```

* Для проверки работоспособности приложения, перейти на страницу:

```
 http://localhost/admin/
```

## Документация для YaMDb доступна по адресу:

```
http://localhost/redoc/
```