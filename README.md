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

The API will now be available at `http://0.0.0.0:8000/`.

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

`docker-compose run --rm server python manage.py createsuperuser`

Then, login with your credentials at `http://0.0.0.0:8000/admin/`.

---

If you use MacOS with M1 chip and run into `django.db.utils.OperationalError: SCRAM authentication requires libpq version 10 or above
`, use this workaround `export DOCKER_DEFAULT_PLATFORM=linux/amd64`. 

