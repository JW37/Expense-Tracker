# ⛪ FaithLedger – Church Account Management System

A complete, production-ready Django web application for managing church income and expenses.

---

## 🚀 Features

| Feature | Details |
|---|---|
| **Authentication** | Gmail login, secure password hashing, password reset via email |
| **Dashboard** | Monthly totals, net balance, 3 live charts, recent transactions |
| **Transactions** | Add/Edit/Delete, filters, search, pagination, pending status |
| **Calendar** | Monthly grid with daily income/expense/pending indicators |
| **Reports** | Date-range filter, Excel (.xlsx) export, PDF export |
| **Analytics** | Top categories, monthly trends, expense breakdown |
| **Categories** | Income & Expense categories with sub-categories, enable/disable |

---

## 📋 Requirements

- Python 3.10+
- pip

---

## ⚡ Quick Start

### 1. Clone / Extract the project

```bash
cd faithledger
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run setup (migrations + seed data + create admin)

```bash
python setup.py
```

Or manually:
```bash
python manage.py migrate
python manage.py seed_data
python manage.py createsuperuser
```

### 5. Start the server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000** in your browser.

---

## 📧 Gmail SMTP Configuration (for Password Reset)

1. Enable **2-Factor Authentication** on your Google account.
2. Go to: Google Account → Security → **App Passwords**
3. Generate an App Password for "Mail"
4. Set environment variables:

**Windows (PowerShell):**
```powershell
$env:EMAIL_HOST_USER = "your-church@gmail.com"
$env:EMAIL_HOST_PASSWORD = "your-16-char-app-password"
```

**Mac/Linux:**
```bash
export EMAIL_HOST_USER="your-church@gmail.com"
export EMAIL_HOST_PASSWORD="your-16-char-app-password"
```

Or edit `faithledger/settings.py` directly (not recommended for production):
```python
EMAIL_HOST_USER = 'your-church@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

---

## 🔐 Password Rules

When resetting password, the new password must:
- Be at least **8 characters** long
- Contain at least **1 number**
- Contain at least **1 special character** (`!@#$%^&*` etc.)

---

## 🏗️ Project Structure

```
faithledger/
├── faithledger/           # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── finance/               # Main app
│   ├── models.py          # Category, SubCategory, Transaction
│   ├── views.py           # All view logic
│   ├── forms.py           # All forms
│   ├── urls.py            # URL patterns
│   ├── admin.py           # Django admin config
│   ├── migrations/        # Database migrations
│   ├── management/commands/
│   │   └── seed_data.py   # Seed default categories
│   └── templates/finance/ # All HTML templates
├── templates/
│   └── base.html          # Base layout with sidebar
├── static/                # CSS, JS assets
├── requirements.txt
├── manage.py
└── setup.py               # Quick setup script
```

---

## 🗄️ Default Categories Seeded

**Income:** Sunday Offerings, Tithes, Special Donations, Festival Contributions, Building Fund

**Expense:** Electricity, Water, Pastor Salary, Staff Salary, Maintenance, Charity, Repairs

---

## 🌐 Production Deployment

### PostgreSQL Setup

Uncomment the PostgreSQL section in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'faithledger'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
```

### Security Checklist for Production

1. Change `SECRET_KEY` to a random 50+ char string
2. Set `DEBUG = False`
3. Set `ALLOWED_HOSTS = ['yourdomain.com']`
4. Set `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` via environment variables
5. Run `python manage.py collectstatic`
6. Use gunicorn + nginx for serving

---

## 🎨 UI Theme

| Color | Usage |
|---|---|
| Blue (`#1a56db`) | Primary, sidebar, buttons |
| Green (`#059669`) | Income, positive balance |
| Red (`#dc2626`) | Expense, negative |
| Yellow (`#d97706`) | Pending |
| White + light gray | Background, cards |

---

## 📊 Technology Stack

- **Backend:** Python 3.10+ / Django 5.0
- **Frontend:** Bootstrap 5.3 + Bootstrap Icons
- **Charts:** Chart.js 4.4
- **Excel Export:** openpyxl
- **PDF Export:** reportlab
- **Database:** SQLite (dev) / PostgreSQL (production)
- **Email:** Gmail SMTP

---

Built with ❤️ for church financial transparency and accountability.
