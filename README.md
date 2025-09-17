# Crampons Étoiles — Football Shop

Live app: <>

---
## A2 - 10/09
### How I implemented the checklist 

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

### Diagram: Request → Django → Response

![alt text](<img/Diagram client request-1.png>)

- `urls.py` maps a URL path to a specific view.

- `views.py` prepares the data (linked models.py) and chooses a template.

- `models.py` defines the database schema and fetch/store data.

- The HTML template renders the final page using the context sent by the view.

### What is the role of settings.py?

`settings.py` holds the project’s configuration: installed apps, middleware, database settings, template directories, static files config, security keys, allowed hosts, and other framework options. Django reads it at the beginning to know how to run the project in each environment.

### How do database migrations work in Django?

Run `python manage.py makemigrations` in the terminal to create migration files (schema changes).

Run `python manage.py migrate` in the terminal to apply those changes to the actual database.

Django tracks which migrations have run so every environment can move to the same schema state.

### Why start with Django?

Django is beginner-friendly while still being efficient. It offers clear structure (MVT), migrations, an admin interface, strong documentation and effective support from the Django community through forums.

---


## A3 - 17/09

### Why do we need data delivery in a platform?
- Other front-ends (web, mobile), services, or partners need a standard way to read your data. Delivering data as XML/JSON lets dashboards, apps, or scripts consume it reliably.
- Scripts and BI tools can fetch machine-readable data for reporting, backups, or ML.

- Multiple clients can access the same API endpoints instead of scraping HTML pages.

### In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?

In my opinion, JSON is better for most app platforms because it’s lighter, easier to read, and easier to manipulate in code. It maps naturally to common data structures (objects, arrays, strings, numbers), and visually it’s clearer.

JSON is more popular because it's native to JavaScript and trivially handled in browsers and most frameworks. It fits REST patterns well and most public/web APIs default to JSON.

### What does is_valid() do in Django forms? Why do we need it?

is_valid() runs all validation (built-in + custom field/clean methods).

If valid: populates form.cleaned_data (safe, typed values) and returns True.

If invalid: returns False and exposes form.errors for user feedback.

We need it to enforce server-side validation to prevent bad/malicious data from being saved, and to display precise error messages back to users.

### How I implemented the check-list

1. Data Views: Added 4 views (show_xml, show_json, show_xml_by_id, show_json_by_id) using Django serializers.

2. URLs: Created routes in main/urls.py for all views and pages.

3. Main Page: show_main displays all products in a table with an Add Product button and Detail button for each item.

4. Form Page: create_product with ProductForm lets users add new products.

5. Detail Page: product_detail shows complete product info with links to JSON/XML.

### PostMan


![alt text](<img/xml.png>)
XML

![alt text](<img/json.png>)
JSON

![alt text](<img/xml_id.png>)
XML_ID

![alt text](<img/json_id.png>)
JSON_ID
