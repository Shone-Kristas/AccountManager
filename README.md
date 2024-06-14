# Сервис для работы с учетными записями пользователей


<br>

## Оглавление
- [Технологии](#технологии)
- [Описание](#описание)
- [Установка приложения](#установка-приложения)
- [Запуск приложения](#запуск-приложения)
- [Инструкции](#Инструкции)
- [Автор](#автор)

<br>

## Технологии

[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?logo=Django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/-DjangoRESTFramework-464646?logo=DjangoRESTFramework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)
[![psycopg2](https://img.shields.io/badge/-psycopg2-464646?logo=psycopg2)](https://pypi.org/project/psycopg2/)
[![docker](https://img.shields.io/badge/-Docker-464646?logo=docker)](https://www.docker.com/)
[![docker_compose](https://img.shields.io/badge/-Docker%20Compose-464646?logo=docker)](https://docs.docker.com/compose/)




[⬆️Оглавление](#оглавление)

<br>

## Описание

Приложение обладает следующей функциональностью:

1. Создание пользователей
2. Получение пользователей по id
3. Поиск пользователя по одному или нескольким параметрам:
   - фамилия
   - имя
   - отчество
   - телефон
   - email

Атрибуты пользователя:
   - id
   - фамилия
   - имя
   - отчество
   - дата рождения
   - номер паспорта (вместе с серией в формате ХХХХ ХХХХХХ)
   - место рождения
   - телефон (в формате 7ХХХХХХХХХХ)
   - email
   - адрес регистрации
   - адрес проживания

Пользователь может быть создан из разных приложений. 
В зависимости от приложения отличается логика валидации полей 
при создании учетной записи пользователя. 
Приложение определяется по обязательному для указания http-заголовку "x-Device".

Список значений http-заголовка и правила валидации полей:
   - mail - обязательные только имя и email
   - mobile - обязательный только номер телефона
   - web - все поля кроме емейла и адреса проживания обязательные


[⬆️Оглавление](#оглавление)

<br>

## Установка приложения:

Клонируйте репозиторий с GitHub:

```bash
git clone https://github.com/Shone-Kristas/AccountManager.git
```

Подразумевается, что на локальной машине, или на удаленном сервере, уже установлены Docker и Docker Compose.

[⬆️Оглавление](#оглавление)

<br>

## Запуск приложения:

Из корневой директории проекта "AccountManager" выполните команду:
```bash
docker compose up
```
* Сервис должен быть запущен [http://localhost:8080/](http://localhost:8080/)

[⬆️Оглавление](#оглавление)

<br>

## Инструкции:

1. Для отправки запросов на создание пользователей используйте Postman:
```bash
http://localhost:8000/api/create/
```
   - для Headers используйте ключ "x-Device" и одно из трех значений "mail", "mobile', "web'
   - тело запроса должно быть в JSON формате
2. Для получения пользователя по id:
```bash
http://localhost:8000/id/
```
3. Для поиска пользователя по параметрам:
```bash
http://localhost:8000/users/search/
```


[⬆️Оглавление](#оглавление)

<br>

## Автор:
[Nickolay](https://github.com/Shone-Kristas)

[⬆️В начало](#Сервис-для-работы-с-учетными-записями-пользователей)