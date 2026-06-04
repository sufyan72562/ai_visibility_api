.PHONY: build up down restart logs shell db-shell migrate migration upgrade test

build:
	docker compose build

up:
	docker compose up

up-d:
	docker compose up -d

down:
	docker compose down

restart:
	docker compose down && docker compose up -d

logs:
	docker compose logs -f web

shell:
	docker compose exec web sh

db-shell:
	docker compose exec db psql -U $${POSTGRES_USER} -d $${POSTGRES_DB}

migration:
	docker compose exec web flask --app run.py db migrate -m "$(m)"

upgrade:
	docker compose exec web flask --app run.py db upgrade

test:
	docker compose exec web pytest