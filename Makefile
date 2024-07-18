.PHONY: test
test:
	docker compose run --rm app sh -c "python manage.py test"

.PHONY: lint
lint:
	docker compose run --rm app sh -c "flake8"

.PHONY: migrations
migrations:
	docker compose run --rm app sh -c "python manage.py makemigrations"

.PHONY: migrate
migrate:
	docker compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"