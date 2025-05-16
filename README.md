
````markdown
# 🍲 Recipe Generator Web App

This is a Django-based web application for generating, viewing, and managing recipes. Users can browse recipes by category, view detailed instructions, and even add their own creations.

---

## 🔧 Features

- 🔍 Browse recipes by category and subcategory
- 📝 Add, update, and delete your own recipes
- ⭐ Submit reviews for recipes
- 🧾 User authentication (signup, login, logout)
- 📸 Image upload for recipes
- 🎨 Responsive user interface

---

## 🛠 Technologies Used

- Python
- Django
- HTML, CSS, Bootstrap
- SQLite (default Django database)
- JavaScript (for interactivity)

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/samrudhigaikwad/Recipe-Generator.git
cd Recipe-Generator
````

### 2. Create Virtual Environment

```bash
python -m venv env
```

### 3. Activate the Environment

* Windows:

  ```bash
  env\Scripts\activate
  ```
* macOS/Linux:

  ```bash
  source env/bin/activate
  ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the Server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser to view the app.

---

## 📂 Project Structure

```
├── myapp/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   └── ...
├── recipes/           # Django project settings
├── manage.py
└── README.md
```

---

## 🙋‍♀️ Author

Developed by **Samruddhi Gaikwad with our team** as part of Team project.
!

