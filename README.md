# Book Management API

A Django REST API for managing books and reading lists. Built as part of a job assessment task.

## Features

- User registration and authentication
- Book management (CRUD operations)
- Personal reading lists
- Add/remove books from reading lists

## Tech Stack

- Django + Django REST Framework
- PostgreSQL
- Token Authentication

## Setup

1. **Clone and setup**
```bash
git clone <repository-url>
cd book-management-api
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

2. **Environment variables**
Create `.env` file:
```env
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

3. **Database setup**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## API Endpoints

### Authentication
- `POST /api/users/register/` - Register user
- `POST /api/users/login/` - Login user
- `GET /api/users/profile/` - User profile

### Books
- `GET /api/books/` - List books
- `POST /api/books/` - Create book
- `GET /api/books/<id>/` - Get/Update/Delete book

### Reading Lists
- `GET /api/reading-lists/` - List user's reading lists
- `POST /api/reading-lists/` - Create reading list
- `GET /api/reading-lists/<id>/` - Get/Update/Delete list
- `POST /api/reading-lists/<id>/add-book/` - Add book to list
- `DELETE /api/reading-lists/<id>/remove-book/<book_id>/` - Remove book

## Usage

All protected endpoints require token authentication:
```http
Authorization: Token your_token_here
```

## Author

Sreeraj K Rajan