# Goodreads Backend

## Overview

This project is a backend system for a Goodreads-like application. It includes models for users, books, authors, reviews, comments, likes, follows, and activity logs. The system also has various database triggers, views, and stored procedures to ensure data integrity and provide useful insights.

## Project Structure

- **Models**: Define the database schema using Django's ORM.
- **Views**: Provide endpoints for various functionalities such as listing books, reviews, and user activities.
- **Utilities**: Include functions for fetching data and performing operations.
- **Templates**: HTML templates for rendering data in the user interface.

## Requirements

- Python 3.12
- Django 5.0.6
- PostgreSQL

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/goodreads-backend.git
    cd goodreads-backend
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python3 -m venv GoodreadsVenv
    source GoodreadsVenv/bin/activate
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    - Create a PostgreSQL database named `goodreads_db`.
    - Create a user named `goodreads_user` with a password `password` (you can change this as per your setup).

    ```sql
    CREATE DATABASE goodreads_db;
    CREATE USER goodreads_user WITH PASSWORD 'password';
    GRANT ALL PRIVILEGES ON DATABASE goodreads_db TO goodreads_user;
    ```

5. **Configure Django settings**:
    - Update `Goodreads/settings.py` to include your database credentials.

6. **Apply migrations**:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Run the development server**:
    ```sh
    python manage.py runserver
    ```
