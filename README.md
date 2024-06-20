# Catalyst Media

Catalyst Media is a Django-based web application that allows users to upload large CSV files, perform data queries, and manage users. The application uses Celery for background processing and Redis as the message broker.

## Features

- User authentication and management with django-allauth
- Large CSV file upload with background processing using Celery
- Query builder to search and filter uploaded data
- Responsive UI built with Bootstrap

## Requirements

- Python 3.6+
- Django 3.2.25
- Celery 5.1.2
- Redis 3.5.3
- django-allauth 0.44.0

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-github-username/your-repository.git
   cd your-repository

2. Create  a virtual environment:
python -m venv .venv
3. Activate :- 
.venv\Scripts\activate
4. Install the dependencies:pip install -r requirements.txt
5. Run database migrations:
python manage.py makemigrations
python manage.py migrate
6. Start the Redis server: redis-server
7. Start the Celery worker: celery -A catalystmedia worker --loglevel=info
8. Run the Django development server: python manage.py runserver
9. Access the application: http://127.0.0.1:8000


Usage :-
Login with your user credentials.
Upload CSV File
Navigate to the Upload Data page.
Select a CSV file and click Upload.
The file will be uploaded and processed in the background.

Query Data:-
Navigate to the Query Builder page.
Enter your search criteria and click Query Data.
The number of records matching your query will be displayed.

Manage Users:- 
Navigate to the Users page.
Add new users or manage existing users.

Project Structure:-

catalystmedia/
├── catalystmedia/
│   ├── __init__.py
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
├── uploader/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tasks.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   ├── uploader/
│   │   │   ├── upload.html
│   │   │   ├── success.html
│   │   │   ├── query_builder.html
│   │   └── base.html
│   ├── migrations/
│   │   └── __init__.py
├── manage.py
├── requirements.txt
├── .env
└── README.md




