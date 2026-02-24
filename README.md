# Task Manager API

## Overview

Task Manager API is a RESTful backend application built using Django and Django REST Framework.  
It provides authenticated users with the ability to perform CRUD operations on tasks.

The application uses JWT-based authentication to secure endpoints and ensure only authorized users can modify data.

---

## Features

- User Registration
- User Login (JWT Authentication)
- Create Task
- Retrieve All Tasks
- Retrieve Single Task
- Update Task
- Delete Task
- Role-based Access (Admin and Regular User)
- Pagination Support
- Filtering by Completion Status
- API Documentation (Swagger)
- Unit Tests

---

## Tech Stack

- Python 3.x
- Django
- Django REST Framework
- Simple JWT (JWT Authentication)
- drf-yasg (Swagger Documentation)
- SQLite (default database)

---

## Project Setup Instructions

### 1. Clone the Repository

"""bash
git clone <your-repository-url>
cd task_manager
"""

---

### 2. Create Virtual Environment

"""bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
# venv\Scripts\activate    # Windows
"""

---

### 3. Install Dependencies

"""bash
pip install -r requirements.txt
"""

---

### 4. Apply Migrations

"""bash
python manage.py makemigrations
python manage.py migrate
"""

---

### 5. Create Superuser (Optional - For Admin Role)

"""bash
python manage.py createsuperuser
"""

---

### 6. Run Development Server

"""bash
python manage.py runserver
"""

Server will start at:

"""
http://127.0.0.1:8000/
"""

---

## Authentication

This project uses JWT Authentication.

### Register User

**POST** "/api/register/"

Example Body:

"""json
{
  "username": "john",
  "email": "john@example.com",
  "password": "strongpassword"
}
"""

---

### Login User

**POST** "/api/login/"

Example Body:

"""json
{
  "username": "john",
  "password": "strongpassword"
}
"""

Response:

"""json
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
"""

Use the access token in headers:

"""
Authorization: Bearer <access_token>
"""

---

## API Endpoints

## Sample Curl
'curl -H "Authorization: Bearer <token>" http://127.0.0.1:8000/api/tasks/'

### Get All Tasks

**GET** "/api/tasks/"

---

### Get Task by ID

**GET** "/api/tasks/{id}/"



---

### Create Task

**POST** "/api/tasks/"

Example Body:

"""json
{
  "title": "Complete assignment",
  "description": "Finish the API task",
  "completed": false
}
"""

---

### Update Task

**PUT** "/api/tasks/{id}/"

---

### Delete Task

**DELETE** "/api/tasks/{id}/"

---

## Filtering

Filter tasks by completion status:

"""
GET /api/tasks/?completed=true
"""

---

## Pagination

Default page size: 5

Example:

"""
GET /api/tasks/?page=2
"""

---

## Role-Based Access

- Regular users can manage only their own tasks.
- Admin users (is_staff=True) can access and manage all tasks.

---


## API Documentation

Swagger documentation is available at:

"""
http://127.0.0.1:8000/swagger/
"""

---

## Running Tests

Run the following command:

"""bash
python manage.py test
"""

This will execute all unit tests covering authentication and CRUD operations.

---

## Notes

- SQLite is used as the default database.
- JWT tokens expire based on configuration in settings.
- Ensure Authorization header is included for protected endpoints.

---

## Author

Sahil Vishwakarma