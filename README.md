## Foodgram ##

## Учебный проект ##

![workflow](https://github.com/GUSICATC/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

Проект доступен по ip:
```
158.160.30.63/api/
```
Frontend доступен по ip:
```
158.160.30.63
```
Для теста admin панели используйте:
```
username: admin
password: admin
email: admin@yandex.ru
```


## Описание ##

Foodgram - онлайн-сервис и API для него. На этом сервисе пользователи смогут публиковать рецепты, 
подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», 
а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

## Технологии  ##

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

## Запуск проекта ##
- Установить на сервер docker и docker-compose

- Скопировать из папки infra файл docker-compose.yml и папку nginx на ваш сервер в папку /home/<ваш-юзернейм>/:
```python
$scp -i <path-to-ssh-key> infra/docker-compose.yml <servername>@<ip>:/home/<username>/
```
```python
$scp -r -i <path-to-ssh-key> infra/nginx/ <servername>@<ip>:/home/<username>/
```
- Сделать любые изменения в файле README и запушить изменения в репозиторий.

- На сервере создать супер пользователя  и выполнить миграции:
```python
$sudo docker-compose exec backend python manage.py makemigrations
$sudo docker-compose exec backend python manage.py migrate
$sudo docker-compose exec backend python manage.py collectstatic --no-input
$sudo docker-compose exec backend python manage.py createsuperuser
$sudo docker-compose exec backend python load_ingredients
```
- Либо выполнить команду "make" из каталога infra, для автоматического 
выполнения команд миграций и создания супер пользователя:
```python
$ sudo apt install make
$ cd ../infra
$ make 
```
