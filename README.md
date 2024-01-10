# Movie Website Backend API

This repository contains the backend API for the Movie Website project. It is a RESTful API built using the Django REST Framework.

## How to start the API

Start by cloning the repository:

``
python manage.py runserver
``

Migrate the Project to the database:

``
python manage.py makemigrations
``

Migrate the database:

``
python manage.py migrate
``

Migrate the Project :

``
python manage.py makemigrations playground
``

### API Endpoints

The API has the following endpoints:

BASE_URL = ``http://127.0.0.1:8000/playground``

- ``/movie`` - returns a list of all movies in the database
- ``/movie`` - add a single movie to the database
- ``/movie/<id>`` - EDIT OR DELETE single movie with the specified id

Movie Object parameters:
```
 {
        "id": 1,
        "name": "sdfgasd",
        "description": "asdfsv",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJYjXYKsiKlYPivq55Bn84BolNPDCZgTXqiwcyF6j8bBk7N4RN9yyirT-gWK2xDM2AX48&usqp=CAU",
        "imageBanner": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJYjXYKsiKlYPivq55Bn84BolNPDCZgTXqiwcyF6j8bBk7N4RN9yyirT-gWK2xDM2AX48&usqp=CAU",
        "category": "fantacy",
        "actor": "me",
        "genre": "nogenre",
        "release": "today",
        "language": "Tamil",
        "rate": "5",
        "fee": "2000",
        "duration": "2h 30m"
    }
```
