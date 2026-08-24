# 🚀 Universal FastAPI Backend Starter

A clean, reusable, and scalable backend foundation built with **FastAPI** for modern web applications, SaaS platforms, automation systems, dashboards, mobile backends, and business software.

Designed to provide a professional starting point for new backend projects without being tied to any specific product or use case.

---

## ✨ Features

* ⚡ FastAPI
* 🐍 Python 3.12+
* 🗄 PostgreSQL
* 🧩 SQLAlchemy ORM
* 🔄 Alembic-ready database migrations
* 🔐 Authentication architecture
* 🔑 JWT-ready security structure
* 👤 User management foundation
* 🛡 Role-Based Access Control (RBAC)
* ⚙️ Service Layer architecture
* 📦 Repository Pattern
* 🚀 Redis support
* 🧵 Celery background worker structure
* 📧 Email service foundation
* 📁 File storage service foundation
* 🚦 Rate limiting ready
* 🐳 Docker support
* 🌐 Nginx reverse proxy
* 🧪 Testing structure
* 🔄 GitHub Actions CI
* ❤️ Health check endpoint
* 🧱 Modular and extendable architecture

---

## 🏗 Project Structure

```text
universal-fastapi-backend-starter/
│
├── app/
│   ├── api/
│   ├── auth/
│   ├── cache/
│   ├── core/
│   ├── database/
│   ├── permissions/
│   ├── services/
│   ├── users/
│   ├── workers/
│   └── main.py
│
├── nginx/
│   └── default.conf
│
├── tests/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🎯 Suitable For

This starter can be used as the foundation for:

* SaaS platforms
* REST APIs
* Mobile application backends
* Admin dashboards
* E-commerce platforms
* Automation systems
* CRM applications
* Business management systems
* Internal enterprise tools
* AI-powered applications
* Microservices
* API-driven platforms

---

## 🛠 Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic

### Database & Cache

* PostgreSQL
* Redis

### Background Processing

* Celery

### Infrastructure

* Docker
* Docker Compose
* Nginx

### Development

* Pytest
* GitHub Actions
* Alembic

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/rezaabbasi-dev/universal-fastapi-backend-starter.git
```

```bash
cd universal-fastapi-backend-starter
```

### 2. Create the environment file

```bash
cp .env.example .env
```

Update the environment variables based on your project requirements.

---

## 🐳 Run With Docker

```bash
docker compose up --build
```

The API will be available at:

```text
http://localhost:8000
```

---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://localhost:8000/docs
```

### ReDoc

```text
http://localhost:8000/redoc
```

---

## ❤️ Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "healthy"
}
```

---

## 🔐 Security Architecture

The project includes a foundation for:

* Password hashing
* JWT authentication
* Access tokens
* Refresh tokens
* Role-based authorization
* Protected routes
* Permission management

The architecture is intentionally modular so authentication can be adapted to the requirements of each project.

---

## 🛡 Role-Based Access Control

The project contains an RBAC foundation that can be extended for roles such as:

```text
Admin
Manager
User
Moderator
Developer
```

Custom permissions can be implemented depending on the application.

---

## 🗄 Database

The starter is designed around PostgreSQL and SQLAlchemy.

It can easily be extended with:

* New models
* Relationships
* Repository classes
* Database migrations
* Custom queries

---

## 🚀 Redis

Redis can be used for:

* Application caching
* Rate limiting
* Temporary data
* Session storage
* Background queues
* Token management

---

## 🧵 Background Tasks

The project includes a Celery-ready structure for tasks such as:

* Sending emails
* Processing files
* Generating reports
* API synchronization
* Scheduled operations
* Background automation

---

## 📧 Email Service

A reusable email service structure is included and can be connected to providers such as:

* SMTP
* SendGrid
* Mailgun
* Amazon SES
* Other email APIs

---

## 📁 Storage

The storage layer can be extended for:

* Local file storage
* Amazon S3
* Cloudflare R2
* MinIO
* Other object-storage providers

---

## 🧪 Testing

The project includes a testing structure that can be expanded with:

* Unit tests
* API tests
* Authentication tests
* Database tests
* Integration tests

Run tests with:

```bash
pytest
```

---

## 🔄 Continuous Integration

GitHub Actions support is included for automated CI workflows.

It can be extended to perform:

* Automated testing
* Code quality checks
* Docker builds
* Deployment pipelines
* Security checks

---

## 🧠 Architecture Philosophy

This repository is designed to be a **general-purpose backend foundation**, not a finished application.

The goal is to provide a reusable architecture that can be cloned and adapted whenever a new backend project is started.

```text
Clone → Configure → Add Business Logic → Build
```

---

## 👨‍💻 Author

**Reza Abbasi**

Backend Developer focused on:

* Python
* FastAPI
* API Development
* Automation
* Backend Architecture
* SaaS Development

GitHub: [@rezaabbasi-dev](https://github.com/rezaabbasi-dev)

---

## ⭐ Support

If you find this project useful, consider giving the repository a **Star ⭐**.

---

Built as a reusable foundation for modern backend development.
