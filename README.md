![example workflow](https://github.com/Petrichao/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
# YamDB
<hr>

## Описание
Представляет собой расширение возможностей проекта YaMDB для совершения удаленных операций.
Благодаря этому проекту зарегистрированные и аутентифицированные пользователи получают возможность оставлять рецензии на произведения различных категорий, комментировать рецензии других пользователей,просматривать сформированные на основе оценок рейтинги произведений. Сайт не предоставляет прямой доступ или ссылки для ознакомления непосредственно с произведениями.

## Расширение функциональности
Функционал проекта адаптирован для использования PostgreSQL и развертывания в контейнерах Docker. Используются инструменты CI и CD.

## Ссылка на сайт
YamDB доступен по [адресу](http://pesy.ddns.net).
<hr>

## Установка
### Шаблон описания файла .env
- DB_ENGINE=django.db.backends.postgresql
- DB_NAME=postgres
- POSTGRES_USER=postgres
- POSTGRES_PASSWORD=postgres
- DB_HOST=db
- DB_PORT=5432

### Инструкции для развертывания и запуска приложения
для Linux-систем все команды необходимо выполнять от имени администратора
- Склонировать репозиторий:

```git clone https://github.com/Petrichao/yamdb_final.git```

- Выполнить вход на удаленный сервер
- Установить docker а сервер:

```apt install docker.io ```

- Установить docker-compose на сервер:

```curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose chmod +x /usr/local/bin/docker-compose```

- Создать .env файл по предлагаемому выше шаблону. Обязательно изменить значения POSTGRES_USER и POSTGRES_PASSWORD
- Для работы с Workflow добавить в Secrets GitHub переменные окружения для работы:

```
DB_ENGINE=<django.db.backends.postgresql>
DB_NAME=<имя базы данных postgres>
DB_USER=<пользователь бд>
DB_PASSWORD=<пароль>
DB_HOST=<db>
DB_PORT=<5432>

DOCKER_PASSWORD=<пароль от DockerHub>
DOCKER_USERNAME=<имя пользователя>

SECRET_KEY=<секретный ключ проекта django>

USER=<username для подключения к серверу>
HOST=<IP сервера>
PASSPHRASE=<пароль для сервера, если он установлен>
SSH_KEY=<ваш SSH ключ (для получения команда: cat ~/.ssh/id_rsa)>

TELEGRAM_TO=<ID чата, в который придет сообщение>
TELEGRAM_TOKEN=<токен вашего бота>
```
- Workflow состоит из четырёх шагов:
  - Проверка кода на соответствие PEP8
  - Сборка и публикация образа бекенда на DockerHub.
  - Автоматический деплой на удаленный сервер.
  - Отправка уведомления в телеграм-чат.

- собрать и запустить контейнеры на сервере:

```docker-compose up -d --build```

- После успешной сборки выполнить следующие действия (только при первом деплое):
  - Создать суперпользователя Django, после запроса от терминала ввести логин и пароль для суперпользователя: 

  ```docker-compose exec web python manage.py createsuperuser```

## Примеры API-запросов
<hr>

Подробные примеры запросов и коды ответов приведены в прилагаемой документации в формате ReDoc по [адресу](http://pesy.ddns.net/redoc) 
    