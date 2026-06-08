# URL Shortener Web Application (Django)

A simple and functional URL Shortener built using Python and Django.  
This project allows users to register, log in, shorten long URLs, and manage them with analytics like click tracking.

---

# Features

# User Authentication

- User Registration
- Login / Logout system
- Session-based authentication

# URL Shortening

- Convert long URLs into short unique codes
- Automatic redirect to original URL
- Unique short code generation

# URL Management (CRUD)

- Create short URLs
- View all created URLs in dashboard
- Edit existing URLs
- Delete URLs

# Analytics

- Click tracking for each short URL
- Creation date tracking
- User-specific URL statistics

# Security

- Users can only access their own URLs
- Login required for all URL operations

---

# Tech Stack

- Python
- Django Framework
- SQLite Database
- HTML / Bootstrap (for UI)

---

# how to Run

- Clone the repository
- Install dependencies: `pip install -r requirements.txt`
- python manage.py makemigrations
- Run migrations: `python manage.py migrate`
- Start server: `python manage.py runserver`
