# Django - 01
A Basic Start with Learning Django

## Prerequisites
- Python 3.8 or higher
- VSCode
- Extension: SQLiteViewer

## Basic Installation
1. Create a virtual environment:
   ```bash
   python -m venv env
   ```
2. Activate the virtual environment:
    - On Windows:
      ```bash
      .\env\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source env/bin/activate
      ```
3. Install pipenv:
   ```bash
   pip install pipenv
   ```
4. Install Django:
   ```bash
   pipenv install django
   ```
5. Activate the pipenv shell:
   ```bash
   pipenv shell
   ```
6. Create a new Django project:
   ```bash
   django-admin startproject app
   ```
7. Navigate to the project directory:
   ```bash
    cd app
    ```
8. Run the development server:
    ```bash
    python manage.py runserver
    ```

## NOTE 01:
- The `manage.py` file is a command-line utility that lets you interact with your Django project.
- The `settings.py` file contains all the settings for your Django project.
- The `urls.py` file is where you define the URL patterns for your project.
- The `wsgi.py` file is used for deploying your project to a web server.
- The `asgi.py` file is used for deploying your project to an ASGI server.
- The `__init__.py` file is used to mark a directory as a Python package.
- The `db.sqlite3` file is the default database file created by Django.

## NOTE 02:
- We can create multiple apps within a single Django project.
- Each app can have its own models, views, and templates.
- We can have seperate apps for different functionalities within the same project like 
  - Blog
  - Forum
  - E-commerce
  - etc.

## Creating a New App
1. Create a new app:
   ```bash
   python manage.py startapp myapp01
   ```
