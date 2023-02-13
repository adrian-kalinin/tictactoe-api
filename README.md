# Tic-tac-toe API

This is a REST API for a game of Tic-Tac-Toe, also known as Noughts and Crosses. It allows you to play a game with the computer.

### Technologies used

- Python 3
- Django
- Docker

## Getting Started

These instructions will help you set up the API on your local machine for development and testing purposes.

### Prerequisites

To run this API, you will need to have Docker and Docker Compose installed on your local machine.

### Installing

1. Clone the repository:

```git clone https://github.com/adrian-kalinin/tictactoe-api.git```

2. Go to the project directory:

```cd tictactoe-api```

3. Build the Docker images:

```docker-compose build```

4. Create a database and run migrations:

```docker-compose run --rm server python manage.py migrate```

5. Start the container:

```docker-compose up```

The API will now be available at `http://127.0.0.1:8000/`.

### Tests

You can also run unit tests:

```docker-compose run --rm server python manage.py test```

## API Endpoints

The API has the following endpoints:

- `http://127.0.0.1:8000/api/v1/docs/` — automatically generated documentation.
- `http://127.0.0.1:8000/api/v1/games/` — list all games or create a new one.
- `http://127.0.0.1:8000/api/v1/games/{id}/` — retrieve, update, delete existing game.

## Admin site 

Django provides admin interface with full access to manage your application. First, you need to create a superuser:

```docker-compose run --rm server python manage.py createsuperuser```

Then, login with your credentials at `http://127.0.0.1:8000/admin/`.

## Project structure

Here is a short description of the project files:

```
|-- core
|   |-- asgi.py -- ASGI configuration.
|   |-- settings.py -- Project settings.
|   |-- urls.py -- Project routing.
|   `-- wsgi.py -- WSGI configuration.
|-- game
|   |-- migrations/ -- Database migrations. 
|   |-- tests/ -- Tests for models and views.
|   |-- admin.py -- Admin site configuration.
|   |-- apps.py -- Application configuration.
|   |-- models.py -- Database models.
|   |-- serializers.py -- Data serializers.
|   |-- urls.py -- Application routing.
|   `-- views.py -- API endpoints.
|-- Dockerfile -- Docker image configuration.
|-- LICENSE -- License (MIT).
|-- README.md -- This file.
|-- docker-compose.yml -- Docker container configuration.
|-- manage.py -- Django management tool.
|-- pyproject.toml -- Python project configuration.
`-- requirements.txt –– List of dependencies.
```

---

If you use MacOS with M1 chip and run into `django.db.utils.OperationalError: SCRAM authentication requires libpq version 10 or above`, use this workaround `export DOCKER_DEFAULT_PLATFORM=linux/amd64` and rebuild the image. 

