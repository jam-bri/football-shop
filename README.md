# Crampons Étoiles — Football Shop

Live app: <>

---

## How I implemented the checklist 

I started by clarifying the goal (a Football Shop), what fields I wanted for my product and how a Django project is structured. I implemented each checklist item deliberately; for some commands I followed the tutorial to ensure correctness.

1. **Created a new Folder and set up the Environnement.**  
  
2. **Created a new Django project.**  
   Initialized a fresh repository and ran `django-admin startproject` to generate the base project.
3. **Created an application named `main`.**  
   Ran `python manage.py startapp main` and added `"main"` to `INSTALLED_APPS` in the settings of crampons_etoiles.
4. **Configured routing so the project runs the `main` app.**  
   In `crampons_etoiles/urls.py`, I included `path("", include("main.urls"))`.

5. **Created the `Product` model with the required fields.**  
   In `main/models.py`, I added `name (CharField)`, `price (IntegerField)`, `description (TextField)`, `thumbnail (URLField)`, `category (CharField)`,`is_featured (BooleanField)`,`stock (models.IntegerField)` and `rating (models.FloatField)`, 
   Then I ran `makemigrations` and `migrate`.

6. **Created a view that returns data to an HTML template showing:**
   - the application name : **Crampons Étoiles**,
   - my name :  **Berguegou Briana Yadjam**,
   - my class :  **PBP KI**.  
   In `main/views.py`, I wrote a function that renders `main/home.html` with this context.

7. **Mapped the view in `main/urls.py`.**  
   I created `main/urls.py` and added `path("", home, name="home")`.



---

## Diagram: Request → Django → Response

![alt text](<Diagram client request-1.png>)

- `urls.py` maps a URL path to a specific view.

- `views.py` prepares the data (linked models.py) and chooses a template.

- `models.py` defines the database schema and fetch/store data.

- The HTML template renders the final page using the context sent by the view.

## What is the role of settings.py?

`settings.py` holds the project’s configuration: installed apps, middleware, database settings, template directories, static files config, security keys, allowed hosts, and other framework options. Django reads it at the beginning to know how to run the project in each environment.

## How do database migrations work in Django?

Run `python manage.py makemigrations` in the terminal to create migration files (schema changes).

Run `python manage.py migrate` in the terminal to apply those changes to the actual database.

Django tracks which migrations have run so every environment can move to the same schema state.

## Why start with Django?

Django is beginner-friendly while still being efficient. It offers clear structure (MVT), migrations, an admin interface, strong documentation and effective support from the Django community through forums.