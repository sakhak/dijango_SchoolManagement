# Teacher CRUD (Django + MySQL, no login required)

A minimal Django app for managing Teacher records with full Create, Read,
Update, Delete functionality, backed by MySQL, with no authentication.

user: admin
pw: Admin@!632004
## Structure

```
TeacherCRUD/
├── SchoolManagementSystem/   # Project settings & urls
├── Core/                     # base.html + home redirect
├── Apps/
│   └── Teacher/               # Teacher CRUD app
│       ├── models.py
│       ├── admin.py
│       ├── forms.py
│       ├── views.py
│       ├── urls.py
│       └── templates/teacher/
├── media/
├── .env
├── requirements.txt
└── manage.py
```

Check your versions:
```bash
python -c "import django; print(django.get_version())"
mysql --version
```
Note: I use with MySql 8.0.x => pip install "Django>=5.2,<6.0"
***************************************************************************
### ⚠️ Django 6.1 requires MySQL 8.4+
`requirements.txt` pins **`Django==6.1`**. Django 6.0+ raised its minimum
supported MySQL version to **8.4+**. If your MySQL server is older (8.0.x
is what most installers still ship, and is what commonly trips this up),
any `manage.py` command will fail with:

```
django.db.utils.NotSupportedError: MySQL 8.4 or later is required (found 8.0.29).
```

**Upgrade MySQL Server to 8.4+** (recommended if you want to keep
   Django 6.1). On Windows, download the latest MySQL Installer from
   https://dev.mysql.com/downloads/installer/ and use it to upgrade your
   existing server, or install a fresh 8.4+ instance side by side.
   On Ubuntu/Debian:
   ```bash
   sudo apt update && sudo apt install -y mysql-server
   ```
   (check `apt-cache policy mysql-server` first — some LTS releases still
   default to 8.0; you may need the official MySQL APT repo from
   https://dev.mysql.com/downloads/repo/apt/ to get 8.4+.)
*****************************************************************************



## MySQL Setup

Create the database and a user (adjust credentials as needed):

```sql
CREATE DATABASE sakhak_dj_school_management_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'school_user'@'localhost' IDENTIFIED BY '632004';
GRANT ALL PRIVILEGES ON sakhak_dj_school_management_db.* TO 'school_user'@'localhost';
FLUSH PRIVILEGES;
```

Update `.env` with your own DB credentials if different from the defaults.

## Run It

```bash
python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

pip install "Django>=5.2,<6.0"
python manage.py makemigrations Teacher
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` — it redirects straight to `/teachers/`.
No login is required for any page (list, add, edit, delete).

## Routes

| URL                     | Action              |
|--------------------------|---------------------|
| `/teachers/`              | List / search        |
| `/teachers/add/`          | Create               |
| `/teachers/<id>/`         | Detail                |
| `/teachers/<id>/edit/`    | Update                |
| `/teachers/<id>/delete/`  | Delete                |
| `/admin/`                 | Django admin (optional; create a superuser to use it) |

This was tested end-to-end against a real MySQL/MariaDB instance: migrations
applied cleanly, and a teacher record was created via the form and verified
directly in the database


Method 3: Show All URLs in Terminal
**********************************
1- ដំឡើង django-extensions
pip install django-extensions

2- settings.py
INSTALLED_APPS = [
    ...
    "django_extensions",
]
3- បន្ទាប់មក៖
python manage.py show_urls

4- Output៖
/admin/          admin:index
/                core:index
/dashboard/      core:dashboard
នេះជាវិធីល្អបំផុតសម្រាប់ Project ធំៗ។













