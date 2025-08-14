# Flexi

A modern, flexible Software Media System backend built with Django 5.2+ and Python 3.13+.

## 🚀 Overview

Flexi is a robust backend system designed to provide a flexible foundation for media management applications. Built with modern Django practices, it offers a scalable architecture with modular app design, comprehensive logging, and multiple API interfaces.

## ✨ Features

- **Modern Django 5.2+** - Built on the latest Django framework
- **Modular Architecture** - Clean separation of concerns with dedicated apps
- **Multiple API Interfaces** - REST API and GraphQL support
- **Comprehensive Logging** - Structured logging with rotation and multiple handlers
- **Environment Configuration** - Flexible settings management with environment variables
- **API Key Authentication** - Secure API access with key-based authentication
- **Split Settings** - Organized configuration management
- **Python 3.13+** - Latest Python features and performance improvements

## 🏗️ Project Structure

```
backend/
├── apps/                    # Django applications
│   ├── core/               # Core functionality and app loader
│   ├── account/            # Authentication and user management
│   └── library/            # Media library management
├── flexi/                  # Main project configuration
│   ├── settings/           # Split settings configuration
│   │   ├── base.py         # Base Django settings
│   │   ├── common.py       # Common configuration
│   │   ├── database.py     # Database configuration
│   │   ├── logging.py      # Logging configuration
│   │   └── security.py     # Security settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI application
├── config/                 # Configuration files
│   └── apps.yaml          # App definitions
├── manage.py               # Django management script
├── pyproject.toml          # Project dependencies and metadata
└── dev_launch.sh          # Development server launcher
```

## 🛠️ Technology Stack

- **Backend Framework**: Django 5.2.5+
- **Python Version**: 3.13+
- **Package Manager**: uv
- **API Framework**: Django REST Framework
- **GraphQL**: Graphene Django
- **Authentication**: Django REST Framework API Keys
- **Configuration**: python-decouple
- **YAML Processing**: PyYAML
- **Settings Management**: django-split-settings

## 📋 Prerequisites

- Python 3.13 or higher
- uv package manager
- Git

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd flexi/backend
```

### 2. Install Dependencies

```bash
uv sync
```

### 3. Run Development Server

```bash
./dev_launch.sh
```

Or manually:

```bash
source .venv/bin/activate
DEBUG=True python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
MODE=dev
```

### App Configuration

Apps are defined in `config/apps.yaml` and automatically loaded by the core app loader system.

## 📱 API Endpoints

- **Admin Interface**: `/admin/`
- **REST API**: Configured with Django REST Framework
- **GraphQL**: Available through Graphene Django

## 🗄️ Database

The project uses SQLite by default for development. Database configuration can be customized in `flexi/settings/database.py`.

## 📝 Logging

Comprehensive logging is configured with:

- Console output for development
- File rotation for production
- Separate error and security logs
- Structured formatting for easy parsing

## 🏗️ Development

### Adding New Apps

1. Create your Django app in the `apps/` directory
2. Add app definition to `config/apps.yaml`
3. The app loader will automatically discover and configure it

## 📚 Documentation

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Graphene Django](https://docs.graphene-python.org/projects/django/)

## 📄 License

This project is licensed under the terms specified in the LICENSE file.

---

**Flexi** - Building flexible media systems for the modern web.
