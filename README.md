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
```


## Описание ##

Foodgram - онлайн-сервис и API для него. На этом сервисе пользователи смогут публиковать рецепты, 
подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», 
а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

## Технологии  ##

 - Python 
 - Django  
 - Docker
 - Git Action
 - React 

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
$sudo docker-compose exec web python manage.py makemigrations
$sudo docker-compose exec web python manage.py migrate
$sudo docker-compose exec web python manage.py collectstatic --no-input
$sudo docker-compose exec web python manage.py createsuperuser
$sudo docker-compose exec web python manage.py loaddata ingredients.json
```
- Либо выполнить команду "make" из каталога infra, для автоматического 
выполнения команд миграций и создания супер пользователя:
```python
$ sudo apt install make
$ cd ../infra
$ make
```