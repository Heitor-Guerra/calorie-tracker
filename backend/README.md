# Calorie Tracker Backend

Backend API for an calorie tracker built with Django REST Framework.

----------

## Requirements

- Python 3
- Virtual Environment Manager (pip, uv, etc...)

----------

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/Heitor-Guerra/calorie-tracker.git
cd calorie-tracker/backend
```

Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependecies
### pip
```bash
pip install -r requirements.txt
```

### uv
```bash
uv sync
```

--------

## Database Setup

Before starting the server, apply the existing database migrations:

```bash
python manage.py migrate
```

--------

## Running the Server

Start the Django development server:

```bash
python manage.py runserver
```

The server will be available at:

`
http://127.0.0.1:8000/
`

----------

## Creating a Superuser

After running the project for the first time, create an administrator account:


```bash
python manage.py createsuperuser
```

Follow the prompts to create the superUser.

After creating the superuser, open the Django admin panel at:

`
http://127.0.0.1:8000/admin/
`

Log in using the superuser credentials.

----------

## Creating a New Django App

To create a new application inside the project, run:

```bash
python manage.py startapp <app\_name>
```

After creating an app, add it to INSTALLED_APPS in the project settings file.

----------

## Model Changes and Migrations

Whenever you make changes to a Django model, such as adding, removing, or modifying a field, you must create and apply new migrations.

First, generate the migration files:

```bash
python manage.py makemigrations
```

Then apply the migrations to the database:

```bash
python manage.py migrate
```

-----------

## Advise

The project is kind of unfinished. It would have some more things, like a page for the users to see their order, and a page for admins to Create, Edit and Delete items/categorie. 
The Django admin dashboard works great, though.
