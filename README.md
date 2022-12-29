# Проект YaMDb с применением CI/CD

[![](https://github.com/vkfedosov/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/vkfedosov/yamdb_final/actions/workflows/yamdb_workflow.yml)

Проект YaMDb собирает отзывы пользователей на различные произведения такие как
фильмы, книги и музыка. Для приложения настроен Continuous Integration (CI) и
Continuous Deployment (CD).

Реализован:
* автоматический запуск тестов;
* обновление образов на DockerHub;
* автоматический деплой на боевой сервер при push-е в главную ветку main.

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

[Fedoska48](https://github.com/Fedoska48) - категории (Categories), жанры (Genres)
и произведения (Titles): модели, view и эндпойнты для них;

[LevLM](https://github.com/LevLM) (teamlead) - отзывы (Review) и комментарии (Comments):
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
* [flake8](https://pypi.org/project/flake8/#files)
* [flake8-broken-line](https://pypi.org/project/flake8-broken-line/#files)
* [flake8-isort](https://pypi.org/project/flake8-isort/#files)
* [flake8-return](https://pypi.org/project/flake8-return/#files)
* [gunicorn 20.0.4](https://pypi.org/project/gunicorn/#files)
* [pep8-naming](https://pypi.org/project/pep8-naming/#files)
* [psycopg2-binary 2.8.6](https://pypi.org/project/psycopg2-binary/#files)
* [pytest-django 4.4.0](https://pypi.org/project/pytest-django/)
* [pytest-pythonpath 0.7.3](https://pypi.org/project/pytest-pythonpath/)
* [pytest 6.2.4](https://pypi.org/project/pytest/)
* [pytz 2020.1](https://pypi.org/project/pytz/#files)
* [requests 2.26.0](https://pypi.org/project/requests/)
* [sqlparse 0.3.1](https://pypi.org/project/sqlparse/#files)

## Начало работы
* Клонировать репозиторий, перейти в директорию с проектом:
```
git clone git@github.com:vkfedosov/api_yamdb_ci_cd.git
```
```
cd api_yamdb_ci_cd
```

* Установить виртуальное окружение, активировать его:
```
python -m venv venv
```
```
. venv/scripts/activate
```

* Перейти в директорию с приложением ```api_yamdb```, установить зависимости:
```
pip install -r requirements.txt
```

* Для подключения GitHub Actions в ```api_yamdb```, необходимо создать директорию 
```.github/workflows``` и скопировать в неё файл ```yamdb_workflow.yml``` из
директории проекта.

* Для прохождения тестов, в директории ```infra```, создать файл ```.env``` с
переменными окружения:
```
# settings.py
SECRET_KEY='<secret_key>'      # стандартный ключ, который создается при старте проекта
DEBUG=False                    # опция отладчика True/False
ALLOWED_HOSTS                  # список хостов/доменов, для которых дотсупен текущий проект

ENGINE=django.db.backends.postgresql
DB_NAME                        # имя БД - postgres (по умолчанию)
POSTGRES_USER                  # логин для подключения к БД - postgres (по умолчанию)
POSTGRES_PASSWORD              # пароль для подключения к БД (установите свой)
DB_HOST=db                     # название сервиса (контейнера)
DB_PORT=5432                   # порт для подключения к БД

# default.conf.template
LOCALHOST                      # имя хоста/домена
PORT                           # порт для подключения
UPSTREAM                       # название сервиса (контейнера) в формате: <название сервиса>:<порт>
```

* В директории проекта ```yamdb_final```, запустить ```pytest```:
```
SECRET_KEY='<secret_key>' pytest
```

## Workflow

Для использования Continuous Integration (CI) и Continuous Deployment (CD): в
репозитории GitHub Actions ```Settings/Secrets/Actions``` прописать Secrets -
переменные окружения для доступа к сервисам:

```
SECRET_KEY                     # стандартный ключ, который создается при старте проекта
DEBUG=False                    # опция отладчика True/False
ALLOWED_HOSTS                  # список хостов/доменов, для которых дотсупен текущий проект

ENGINE=django.db.backends.postgresql
DB_NAME                        # имя БД - postgres (по умолчанию)
POSTGRES_USER                  # логин для подключения к БД - postgres (по умолчанию)
POSTGRES_PASSWORD              # пароль для подключения к БД (установите свой)
DB_HOST=db                     # название сервиса (контейнера)
DB_PORT=5432                   # порт для подключения к БД

LOCALHOST                      # имя хоста/домена
PORT                           # порт для подключения
UPSTREAM                       # название сервиса (контейнера) в формате: <название сервиса>:<порт>

DOCKER_USERNAME                # имя пользователя в DockerHub
DOCKER_PASSWORD                # пароль пользователя в DockerHub
HOST                           # ip_address сервера
USER                           # имя пользователя
SSH_KEY                        # приватный ssh-ключ (cat ~/.ssh/id_rsa)
PASSPHRASE                     # кодовая фраза (пароль) для ssh-ключа

TELEGRAM_TO                    # id телеграм-аккаунта (можно узнать у @userinfobot, команда /start)
TELEGRAM_TOKEN                 # токен бота (получить токен можно у @BotFather, /token, имя бота)
```

При push в ветку main автоматически отрабатывают сценарии:
* *tests* - проверка кода на соответствие стандарту PEP8 и запуск pytest.
Дальнейшие шаги выполняются только если push был в ветку main;
* *build_and_push_to_docker_hub* - сборка и доставка докер-образов на DockerHub
* *deploy* - автоматический деплой проекта на боевой сервер. Выполняется
копирование файлов из DockerHub на сервер;
* *send_message* - отправка уведомления в Telegram.

## Подготовка удалённого сервера
* Войти на удалённый сервер, для этого необходимо знать адрес сервера, имя
пользователя и пароль. Адрес сервера указывается по IP-адресу или по доменному
имени:
```
ssh <username>@<ip_address>
```

* Остановить службу ```nginx```:
```
sudo systemctl stop nginx
```

* Установить Docker и Docker-compose:
```
sudo apt update
sudo apt upgrade -y
sudo apt install docker.io
sudo apt install docker-compose -y
```

* Проверить корректность установки Docker-compose:
```
sudo docker-compose --version
```
* На сервере создать директорию ```nginx```:
```
sudo mkdir nginx
```

* Скопировать файлы ```docker-compose.yaml``` и
```nginx/templates/default.conf.template``` из проекта (локально) на сервер в
```home/<username>/docker-compose.yaml``` и
```home/<username>/nginx/templates/default.conf.template``` соответственно:
  * перейти в директорию с файлом ```docker-compose.yaml``` и выполните:
  ```
  scp docker-compose.yaml <username>@<ip_address>:/home/<username>/docker-compose.yaml
  ```
  * перейти в директорию с файлом ```default.conf.template``` и выполните:
  ```
  scp docker-compose.yaml <username>@<ip_address>:/home/<username>/nginx/templates/default.conf.template
  ```

## После успешного деплоя
* Создать суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```

* Для проверки работоспособности приложения, перейти на страницу:
```
http:/<ip_address>/admin/
```

## Документация для YaMDb доступна по адресу:
```
http:/<ip_address>/redoc/
```