
# Django Blog Project

A feature-rich blog application built with Django, designed for creating, reading, updating, and deleting blog posts. It includes user authentication, comments, categories, tags, search functionality, and pagination.

## Features

- **User Authentication**: Registration, login, and logout functionality.
- **CRUD Operations**: Create, read, update, and delete blog posts.
- **Comments**: Add comments to posts.
- **Categories & Tags**: Organize posts into categories and tags.
- **Search Functionality**: Search for posts by title or content.
- **Pagination**: Display posts and search results with pagination.


## Installation

Follow these steps to set up the project locally:

### Prerequisites

- Python (>= 3.8)
- Django (>= 4.x)
- SQLite (default database)
- Virtual Environment (optional but recommended)

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/django-blog.git
    cd django-blog
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/MacOS
    venv\Scripts\activate     # For Windows
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser** (for admin access):
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the Application**:
    Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Usage

- Navigate to the homepage to view all blog posts.
- Login or register to create and manage posts.
- Search for posts using the search bar.
- Leave comments on posts.

### Admin Panel

Access the admin panel at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin). Use the superuser credentials created earlier to log in.

---

## Project Structure

```plaintext
django-blog/
├── blog/                   # Blog application
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   ├── static/             # Static files (CSS, JS, Images)
│   ├── models.py           # Data models
│   ├── views.py            # Application logic
│   └── urls.py             # URL routes
├── myproject/              # Project configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # Project URL configuration
│   └── wsgi.py             # WSGI entry point
├── manage.py               # Django's CLI utility
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## Technologies Used

- **Back-End**: Django (Python)
- **Database**: SQLite (default, easily replaceable with PostgreSQL)
- **Frontend**: HTML, CSS, Bootstrap

---

## Future Enhancements

- Add social media sharing for posts.
- Implement a REST API using Django REST Framework.
- Add email notifications for comments and new posts.
- Integrate advanced search with filters (e.g., by date, category, tag).

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add feature description"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For any inquiries or support, feel free to reach out:

- **Email**: davidcd08@gmail.com.com
- **LinkedIn**: [LinkedIn](https://linkedin.com/davidcuevasdíaz)
- **GitHub**: [GitHub](https://github.com/DavidcD8)

---
