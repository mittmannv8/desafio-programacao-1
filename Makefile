install:
	@pip install -r requirements.txt
	@python manage.py migrate

test:
	@python manage.py test

run:
	@python manage.py runserver
