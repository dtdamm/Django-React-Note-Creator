# Django React Note App

## Setup

❯ python -m venv .venv
❯ source .venv/bin/activate
❯ pip install -r requirements.txt
❯ django-admin startproject backend
❯ cd backend
❯ python3 manage.py startapp api

#### serializers.py

Sets the user model from django and validates it as well as creating a user object if data is valid

#### views.py

Generates generic views for testing the serilizer from rest framework library, has access to all models from the django user model

#### urls.py

Generates routes client can access to test views.

### Learning Journal

- Learned Django library with bultin ORM to manage ddatabase in sqlite
- How to create login, signup, and authenticate user with bultin Django components and authenticate them using JWT
- Create access token, and a refresh token that returns another token for the user once hte inital
  access token expires

Frontend

- Ditch all boilerplate when using vite and create a /styles, /components and pages directories
- As well as a constants.js and api.js and envoirnment varibale file
- Use axios to make network requests and wrap them in headers for enring correct authentication
- Created protected route component to wrap protected routes and call the backend access token and refresh tokens and set them in local storage, ensuring proper validation of authenticated users
