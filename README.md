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

--- 
## A4 - 24/09


### What is Django's AuthenticationForm? Explain its advantages and disadvantages.

`AuthenticationForm` is provided by Django for login.  
It validates username and password with `authenticate()`.  
You can call `form.get_user()` and pass it to `login()`.  
**Advantages:** quick, secure, integrates with Django’s auth.  
**Disadvantages:** username/password only by default; no MFA/rate limiting; needs subclassing for email login.

### What is the difference between authentication and authorization? How does Django implement the two concepts?
Authentication means proving who you are.  
Authorization means checking what you are allowed to do.  
Django handles authentication with the `User` model, `authenticate()`, `login()`, and auth backends.  
It handles authorization with permissions, groups, `@login_required`, and mixins like `PermissionRequiredMixin`.  

### What are the benefits and drawbacks of using sessions and cookies in storing the state of a web application?
Sessions store data on the server and keep only an id in the cookie.They are secure and revocable but need storage and scaling support.  
Cookies store data on the client side.They are lightweight and stateless but limited in size and readable unless encrypted.  

### In web development, is the usage of cookies secure by default, or is there any potential risk that we should be aware of? How does Django handle this problem?
Cookies are not secure by default because they can be stolen by XSS, intercepted over HTTP, or misused for CSRF.  
To hangdle this problem, always set the `Secure`, `HttpOnly`, and `SameSite` flags.  
Django adds CSRF middleware, signs cookies, rotates session keys on login, and provides secure settings like `SESSION_COOKIE_SECURE`.  

### Explain how you implemented the checklist above step-by-step (not just following the tutorial).
I implemented this project by first reading the tutorial thoroughly and making sure I understood each concept that was explained.  
The tutorial introduced authentication, sessions, and cookies, so I took notes on how each one works in Django.  
With this understanding, I created a small plan based on the checklist provided.  
By following this process step by step, I was able to satisfy the checklist while also making sure I really understood how each concept fits into Django’s authentication system.  



--- 
## A5- 01/10

### **CSS Selector Priority**: If multiple CSS selectors target an HTML element, explain the priority order for CSS selector selection.
If multiple CSS selectors target the same element, CSS applies the one with the highest specificity.
The order of specificity is:
1. Inline styles
2. ID selectors
3. Class selectors, attribute selectors, and pseudo-classes
4. Element selectors and pseudo-elements

### Why is responsive design important in web application development?

Responsive design ensures that a web application adapts to different screen sizes and devices such as desktops, tablets, and especially mobile phones. Since the majority of users access websites from mobile devices, a responsive layout improves usability, accessibility, and overall user experience. Without responsive design, pages may appear broken, difficult to navigate, or frustrating to use, which can reduce engagement and drive users away.

### Provide examples of applications that have and haven't implemented responsive design. Explain the reasons behind your examples. 

- **Responsive design implemented**:  
  *Scele (UI’s e-learning platform)* has implemented responsive design, allowing students to access course materials, submit assignments, and check announcements easily from both desktop and mobile devices.

- **Responsive design not implemented**:  
  Some older government or institutional websites (for example, SIAK NG) have not implemented responsive design. On mobile devices, these sites may require zooming and horizontal scrolling, making the user experience frustrating and inefficient.


### **Box Model**: Explain the differences between margin, border, and padding, and how to implement them

In CSS, every element is represented as a rectangular box. The **box model** describes the structure and spacing of this box, consisting of four layers:

- **Content**  
   The actual text, image, or other content inside the element.

- **Padding**  
   The space *between the content and the border*. It pushes the border outward without affecting elements outside the box.  
   ```css
   .example {
     padding: 20px; /* adds 20px space inside the box, around the content */
   }

- **Border**
   A line surrounding the padding and content. It can be styled with thickness, color, and style.
   ```css
   .example {
   border: 2px solid #333; /* dark gray border around the box */
   }

- **Margin**
   The space outside the border that separates the element from other elements.
   ```css
   .example {
   margin: 15px; /* adds 15px space outside the box */
   }
   
### **Layout Systems**: Explain the concepts of flexbox and grid layout along with their uses

### **Layout Systems**: Explain the concepts of flexbox and grid layout along with their uses

CSS3 provides two layout systems to create responsive and flexible designs: **Flexbox** and **Grid**.

#### 1. Flexbox
Flexbox (Flexible Box Layout) is a one-dimensional layout system. It is best for arranging items **in a row (horizontal)** or **in a column (vertical)**, and for controlling the alignment, spacing, and distribution of space between elements.

**Key features:**
- Align items horizontally or vertically
- Distribute extra space dynamically
- Easily reorder or wrap items
- Ideal for toolbars, navbars, cards in a row, etc.

**Example:**
```css
   .container {
   display: flex;
   justify-content: space-between; /* distribute items evenly */
   align-items: center;           /* align items vertically */
}
```


#### 2. CSS Grid

Grid layout is a two-dimensional system. It allows you to arrange items into rows and columns simultaneously, making it perfect for more complex, structured layouts.

**Key features:**
- Define explicit rows and columns
- Place items precisely within the grid
- Supports overlapping (like layers)
- Ideal for full-page layouts, dashboards, galleries, etc.


**Example:**
   ```css
   .container {
   display: grid;
   grid-template-columns: 1fr 1fr 1fr; /* three equal columns */
   gap: 20px;                          /* spacing between items */
   }
   ```

### Implementation Steps: Explain how you implemented the above checklist step-by-step (not just following the tutorial)

1. **Base & Brand**  
   Set up Tailwind in `base.html` and styled the brand header as *Crampons ⭐ Étoiles* using slate + gold palette.

2. **Endpoints**    
   - `edit_product`/`delete_product` restricted to owner, delete via POST with CSRF.

2. **Responsive Catalog**  
   Replaced table with a product **grid**: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`. Cards show image, price, category, rating and stock.

5. **Card Design**  
   Added Tailwind badges: Featured, Low stock, Rating. Actions row uses flex for **View / Edit / Delete** buttons.

6. **Filters & Auth**  
   “All / My Products” filter adjusts queryset. Added login/register pages styled with slate + gold, matching shop identity.

7. **Images**  
   Used `URLField` thumbnails for speed; template falls back to “No image” if empty.

**Result:** A responsive, branded shop for **Crampons Étoiles** with a catalog UI that feels like a real store.

--
## A6 - 08/10

### What is the difference between synchronous request and asynchronous request?

- **Synchronous request:** The browser must wait for the server to respond before continuing. This means the page becomes unresponsive until the process is done, creating the classic *“click–wait–refresh”* experience.  
- **Asynchronous request:** The browser can continue executing other tasks while waiting for the server’s response. AJAX uses this approach, allowing parts of a web page to update dynamically without reloading the entire page.

### How does AJAX work in Django (request–response flow)?

1. **Event Trigger:** A user action (like clicking a button or submitting a form) triggers JavaScript code.  
2. **AJAX Request:** JavaScript (using `fetch` or `XMLHttpRequest`) sends data to a Django view URL, typically under `/api/`.  
3. **Django View:** The view processes the request and returns a JSON or HTML response.  
4. **Server Response:** The server sends back the response asynchronously.  
5. **DOM Update:** JavaScript receives the response and updates only the necessary parts of the web page — no full reload needed.

This allows Django and JavaScript to communicate smoothly, improving responsiveness and performance.

### What are the advantages of using AJAX compared to regular rendering in Django?

-  **Faster performance:** Only small parts of the page are updated.  
-  **Better user experience:** No full page reloads, resulting in smoother interaction.  
-  **Reduced server load:** Less data is sent and received.  
-  **Real-time features:** Enables instant updates for chat, search, or notifications.  
-  **Event-driven design:** Updates triggered by user actions, not page reloads.

### How do you ensure security when using AJAX for Login and Register features in Django?

To protect AJAX-based authentication endpoints:

1. **Use Django’s CSRF protection:** Include the CSRF token in AJAX headers.  
   ```javascript
   headers: { 'X-CSRFToken': getCookie('csrftoken') }
2. Validate and sanitize input: Never trust client-side data — validate on the server.

3. Use HTTPS: Encrypts credentials and sensitive data.

4. Escape output: Prevents Cross-Site Scripting (XSS) attacks.

5. Avoid sensitive info in JSON responses: Don’t return debug or system data.
