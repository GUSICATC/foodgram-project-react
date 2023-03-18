build:
	sudo docker-compose up -d --build
	sudo docker-compose exec backend python manage.py makemigrations
	sudo docker-compose exec backend python manage.py migrate
	sudo docker-compose exec backend python manage.py createsuperuser
	sudo docker-compose exec backend python manage.py collectstatic --no-input
	sudo docker-compose exec backend python manage.py load_ingredients
	 