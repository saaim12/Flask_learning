
# 🧠 Flask Routing, Templates & Forms – Cheat Sheet

## 📂 Topics Covered

- Static & Dynamic Routing  
- Jinja2 Templates  
- Static Assets  
- Error Handling (`abort`)  
- Form Handling with `request`  
- Flask-WTF Forms (CSRF, Validation, etc.)

---

### ✅ 1. Static Routing

Static routes are **fixed URL paths**.

```python
@app.route('/about')
def about():
    return 'This is the About page'
```

🟢 Use when content doesn’t vary per user.

---

### ✅ 2. Dynamic Routing

Dynamic routes take **user input from URL**.

```python
@app.route('/user/<username>')
def show_user(username):
    return f'Hello, {username}!'
```

🟢 Flask automatically maps values from the URL to the function parameter.

---

## 🎨 Flask Templates (Jinja2)

### 🖼️ 3. Static Templates

- HTML files go inside the `templates/` folder.
- Static files (CSS/JS/images) go inside `static/` folder.
- Reference them using `url_for()`:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

---

### ⚙️ 4. Dynamic Templates with Jinja2

Use `render_template('file.html', variable=value)` to pass data.

#### a. Variables
```html
<p>Hello, {{ name }}</p>
```

#### b. If Conditions
```html
{% if logged_in %}
  Welcome back!
{% else %}
  Please log in.
{% endif %}
```

#### c. Loops
```html
<ul>
{% for item in items %}
  <li>{{ item }}</li>
{% endfor %}
</ul>
```

#### d. Template Inheritance

**base.html**
```html
<html>
  <body>
    {% block content %}{% endblock %}
  </body>
</html>
```

**child.html**
```html
{% extends 'base.html' %}
{% block content %}
  <h1>Welcome!</h1>
{% endblock %}
```

---

## 🚨 5. Error Handling & `abort`

Use `abort()` to raise HTTP errors.

```python
from flask import abort

@app.route('/admin')
def admin():
    if not user_is_admin:
        abort(403)
```

**Custom error page:**
```python
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404
```

---

## 📝 6. Form Handling (Manual with `request`)

### a. HTML Form
```html
<form method="POST" action="/submit">
  <input name="username" type="text">
  <input type="submit">
</form>
```

### b. Handling in Flask
```python
from flask import request

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    return f"Welcome {username}"
```

---

## 🔐 7. Flask-WTF Forms

A Flask extension for better form handling with validation and CSRF.

### a. Install
```bash
pip install flask-wtf
```

### b. Define Form Class (forms.py)
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
```

### c. Enable CSRF
```python
app.config['SECRET_KEY'] = 'your-secret-key'
```

### d. Use in Route
```python
from forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return f"Logged in as {form.username.data}"
    return render_template('login.html', form=form)
```

### e. Use in Template
```html
<form method="POST">
  {{ form.hidden_tag() }}
  {{ form.username.label }} {{ form.username() }}
  {{ form.password.label }} {{ form.password() }}
  {{ form.submit() }}
</form>
```

---

## 🧾 Summary Table

| Feature              | Description                                                  |
|----------------------|--------------------------------------------------------------|
| `@app.route()`       | Define URL paths (static/dynamic)                            |
| `render_template()`  | Load and render HTML files with data                         |
| Jinja2               | Embed Python logic in HTML (`{{ }}` / `{% %}`)               |
| `url_for()`          | Generate URLs for routes or static files                     |
| `abort()`            | Raise HTTP errors like 404 or 403                            |
| `request.form`       | Catch raw form input from `POST` request                     |
| Flask-WTF            | Advanced form handling with validation and CSRF protection   |
