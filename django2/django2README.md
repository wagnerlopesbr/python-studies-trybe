# Django2 README

## Templates

To use a different template (example: Jinja2 x DTL) you have to update the "BACKEND" key inside the "TEMPLATES" variable at "settings.py" file:<br>
(example)
- ..."BACKEND": "django.template.backends.django.DjangoTemplates"...,
- ..."BACKEND": "django.template.backends.jinja2.Jinja2"...,
```
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

## Running a new project

#### *Step-by-step*:
1. **Create the virtual environment and install the packages:**
- python3 -m venv .venv && source .venv/bin/activate
- pip install django
- pip install Pillow           ///  library to work with images
- pip install mysqlclient          ///  library to communicate with MySQL
2. **Create the Django project and app:**
- django-admin startproject event_manager .
- django-admin startapp events
3. **Update the "INSTALLED_APPS" and "DATABASES" variables at "settings.py" file:**
- ```
    INSTALLED_APPS = [
        ...
        'events',
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'event_manager_database',
            'USER': 'root',
            'PASSWORD': 'password',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
    ```
4. **Create the SQL script inside the "./database" folder:**
- mkdir database && cd database
- touch 01_create_database.sql
- ```
    CREATE DATABASE IF NOT EXISTS event_manager_database;
    USE event_manager_database;
    ```
5. **Create the Dockerfile at the project root:**
- touch Dockerfile
- ```
    FROM mysql:8.0.32
    ENV MYSQL_ROOT_PASSWORD password
    COPY ./database/01_create_database.sql /docker-entrypoint-initdb.d/data.sql01
    ```
6. **Build the image and execute the container: (run in root terminal)**
- docker build -t event-manager-db .
- docker run -d -p 3306:3306 --name=event-manager-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=event_manager_database event-manager-db
7. **Run the Django "migrate":**
- python3 manage.py migrate
8. **Rendering templates:**
(forcing Django to look for templates in the specific directory):
- Update the "settings.py" file:
- ```
    import os


    TEMPLATES = [
        {
            ...,
            "DIRS": [os.path.join(BASE_DIR,"templates")],
            ...,
        },
    ]
    ```
9. **Create the "templates" folder inside the "events" folder, then create "home.html" file:**
- mkdir events/templates
- touch events/templates/home.html
- type "html:5" and hit "enter"
- ```
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Django Template</title>
    </head>
    <body>
        <h1>My first Django template!</h1>
    </body>
    </html>
    ```
10. **Implement "views.py" inside the "events" folder:**
- ```
    from django.shortcuts import render


    def index(request):
        return render(request, "home.html")
    ```
11. **Create and implement the "urls.py" inside the "events" folder:**
- touch events/urls.py
- ```
    from django.urls import path
    from events.views import index


    urlpatterns = [
        path("", index, name="home-page")
    ]
    ```
    ***The "path" method:*** path(route, function to be executed when the route is accessed, route name)
12. **Update the "urls.py" file in the "event_manager" folder to include the "events" app routes in the "event_manager" project:**
- ```
    from django.contrib import admin
    from django.urls import path

    urlpatterns = [
        ...,
        path("", include("events.urls")),
    ]
    ```
13. **Execute the server and check the app**:
- python3 manage.py runserver           /// run in root terminal

---
## Exercise 01
Create a new template "about.html":
1. Create the "about.html" file inside the "templates" directory of "events" app and add the HTML content you want to display on the screen.
2. Create the "about" function in the "views.py" file of "events" app and render the template created.
3. Create a new route in the "urls.py" file of "events" app and link the "about" function.
