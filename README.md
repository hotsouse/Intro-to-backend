# Django Todo App

A simple todo application built with Django that allows users to create, view, and manage their todos.

## Features

- User registration and authentication
- Create, view, and delete todos
- Secure user-specific todo management
- Clean and responsive UI

## Setup Instructions

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install django
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Visit http://127.0.0.1:8000/register/ to create an account and start using the app.

## Usage

1. Register a new account
2. Log in with your credentials
3. Create new todos
4. View and manage your todos
5. Log out when done

## Technologies Used

- Django
- Python
- HTML/CSS 