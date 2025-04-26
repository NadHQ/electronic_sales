COMPOSE=docker compose
SERVICE=web  


up-d:
	$(COMPOSE) up -d
up:
	$(COMPOSE) up
down:
	$(COMPOSE) down

build:
	$(COMPOSE) build

rebuild:
	$(COMPOSE) down
	$(COMPOSE) build
	$(COMPOSE) up -d

migrate:
	$(COMPOSE) exec $(SERVICE) python manage.py migrate

makemigrations:
	$(COMPOSE) exec $(SERVICE) python manage.py makemigrations

createsuperuser:
	$(COMPOSE) exec $(SERVICE) python manage.py createsuperuser

collectstatic:
	$(COMPOSE) exec $(SERVICE) python manage.py collectstatic --noinput

shell:
	$(COMPOSE) exec $(SERVICE) python manage.py shell

generate-data:
	$(COMPOSE) exec $(SERVICE) python manage.py generate_network_data

logs:
	$(COMPOSE) logs -f

# Полная установка
setup: build up-d migrate generate-data
