# Django - 01

A Basic Start with Learning Django

## Prerequisites

-   Python 3.8 or higher
-   VSCode
-   Extension: SQLiteViewer

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

-   The `manage.py` file is a command-line utility that lets you interact with your Django project.
-   The `settings.py` file contains all the settings for your Django project.
-   The `urls.py` file is where you define the URL patterns for your project.
-   The `wsgi.py` file is used for deploying your project to a web server.
-   The `asgi.py` file is used for deploying your project to an ASGI server.
-   The `__init__.py` file is used to mark a directory as a Python package.
-   The `db.sqlite3` file is the default database file created by Django.

## NOTE 02:

-   We can create multiple apps within a single Django project.
-   Each app can have its own models, views, and templates.
-   We can have seperate apps for different functionalities within the same project like
    -   Blog
    -   Forum
    -   E-commerce
    -   etc.

## NOTE 03:

-   Web Frameworks are designed to make it easier to build web applications.
-   A Library is a collection of code that you can use in your own projects.
-   A Framework is a collection of libraries and tools that provide a structure for building applications.
-   A Framework is opinionated, meaning it has a specific way of doing things.
-   Django is a framework, not a library.

## NOTE 04: Understanding MVT

-   MVT stands for Model-View-Template.
-   Model: Represents the data and business logic of the application.
-   View: Handles the user interface and user interaction.
-   Template: Defines the presentation layer and how the data is displayed to the user.

## Creating a New App

1. Create a new app:
    ```bash
    python manage.py startapp myapp01
    ```

## NOTE 05: Understanding App Structure

-   `app/`: The main project directory.
-   `myapp01/`: The new app directory.
-   `migrations/`: Directory for database migrations.
-   `admin.py`: File for registering models with the Django admin interface.
-   `apps.py`: File for app configuration.
-   `models.py`: File for defining models (database tables).
-   `tests.py`: File for writing tests for the app.
-   `views.py`: File for defining views (business logic).
-   `urls.py`: File for defining URL patterns for the app.
-   `static/`: Directory for static files (CSS, JavaScript, images).
-   `templates/`: Directory for HTML templates.
-   `__init__.py`: File to mark the directory as a Python package.

## NOTE 06:

-   Views can be defined as functions or class-based views.
-   Function-based views are simpler and easier to understand.
-   Class-based views provide more functionality and are more flexible.
-   Class based views needs Inheritance to work.
-   We need to map the views to app level and project level urls.

## Creating a View

1. Create a view in `views.py`:
   **Refer to the views.py file in the repository.**
2. Create a URL pattern in `urls.py`:
   **Refer to the urls.py file in the repository.**
3. Include the app's URLs in the project's `urls.py`:

    ```python
    from django.urls import include, path

    urlpatterns = [
         path('myapp01/', include('myapp01.urls')),
    ]
    ```
4. Add the app to the `INSTALLED_APPS` list in `settings.py`:

    ```python
    INSTALLED_APPS = [
        # other apps
        'myapp01',
        # other apps
    ]
    ```
5. Access the view in the browser by running the server:
    ```bash
    python manage.py runserver
    ```