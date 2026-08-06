![Python](https://img.shields.io/badge/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

# 🚀 Task Manager API

A production-oriented REST API built with **FastAPI** that demonstrates modern backend development practices including authentication, database design, testing, Docker, security, and clean architecture.

The API provides secure authentication using **JWT Access Tokens** and **Refresh Tokens**, password hashing with **Argon2**, **PostgreSQL** as the database, and follows clean architecture and backend best practices.

---

# ✨ Features

- 👤 User registration and management
- 📝 Task management (CRUD)
- 🔑 JWT Authentication
- 🔄 Refresh Token authentication
- 🔒 Password hashing using Argon2
- 🗄️ PostgreSQL database integration
- 📦 SQLAlchemy ORM
- 📜 Alembic database migrations
- 🐳 Fully Dockerized application
- ⚡ Interactive API documentation (Swagger & ReDoc)
- ⚙️ Environment-based configuration with `.env`

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.14 | Programming Language |
| FastAPI | REST API Framework |
| SQLAlchemy | ORM |
| PostgreSQL | Database |
| Alembic | Database Migrations |
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| Pydantic | Data Validation |
| JWT | Authentication |
| pwdlib (Argon2) | Password Hashing |
| Uvicorn | ASGI Server |

---

# 🏗️ Architecture

```
app/
├── core/          # Configuration, security and authentication
├── database/      # Database engine and session management
├── models/        # SQLAlchemy models
├── routers/       # API endpoints
├── schemas/       # Pydantic schemas
├── services/      # Business logic (future)
└── main.py        # FastAPI application
```

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/MiguelP0rtela/task-manager-api.git
cd task-manager-api
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file based on `.env.example`.

Example:

```env
SECRET_KEY=your-secret-key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

DATABASE_URL=postgresql://user:password@localhost:5432/task_manager

TEST_DATABASE_URL=postgresql://user:password@localhost:5432/task_manager_test
```

---

## 5. Run the application

### Option 1 — Local

Start PostgreSQL

```bash
docker compose up -d postgres
```

Run the API

```bash
python -m uvicorn app.main:app --reload
```

---

### Option 2 — Docker

```bash
docker compose up --build
```

---

The API will be available at

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# 📖 API Documentation

| Documentation | URL |
|---------------|-----|
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |

---

# 📡 Main Endpoints

## Authentication

| Method | Endpoint |
|--------|----------|
| POST | `/auth/login` |
| POST | `/auth/refresh` |

---

## Users

| Method | Endpoint |
|--------|----------|
| POST | `/users` |
| GET | `/users/{id}` |
| PUT | `/users/{id}` |
| DELETE | `/users/{id}` |

---

## Tasks

| Method | Endpoint |
|--------|----------|
| GET | `/tasks` |
| POST | `/tasks` |
| GET | `/tasks/{id}` |
| PUT | `/tasks/{id}` |
| DELETE | `/tasks/{id}` |

---

# 🧪 Testing

Run all tests

```bash
pytest
```

Run with coverage

```bash
pytest --cov=app --cov-report=term-missing
```

---

# 📌 Project Status

| Feature | Status |
|-----------------------------------------|:------:|
| User CRUD | ✅ |
| Task CRUD | ✅ |
| JWT Authentication | ✅ |
| Refresh Tokens | ✅ |
| Login Endpoint | ✅ |
| Refresh Endpoint | ✅ |
| Password Hashing | ✅ |
| Protected Routes | ⏳ |
| Logout Endpoint | ⏳ |
| Environment Configuration | ✅ |
| API Documentation | ✅ |
| Dockerized PostgreSQL | ✅ |
| Alembic Migrations | ✅ |
| Task Status | ✅ |
| Created / Updated timestamps | ✅ |
| Filtering & Pagination | ✅ |
| Unit Tests | ⏳ |
| Dockerized Application | ✅ |
| GitHub Actions (CI/CD) | ⏳ |
| Role-Based Authorization | ⏳ |
| Rate Limiting | ⏳ |
| Deployment | ⏳ |

---

# 🎯 Project Goals

The goal of this project is to build a production-ready REST API while applying modern backend development practices, including:

- Authentication
- Database migrations
- Docker
- Secure password hashing
- Clean Architecture
- Testing
- CI/CD
- Production-ready API design

---

# 🎯 Learning Objectives

This project is being developed to strengthen practical knowledge of:

- REST API development
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Docker
- Alembic
- JWT Authentication
- Refresh Token Authentication
- Secure Password Hashing
- Backend Architecture
- Software Engineering Best Practices
- Testing
- CI/CD

---

# 🚀 Future Improvements

- 🚪 Logout endpoint
- 👥 Role-Based Authorization (RBAC)
- 🚦 Rate Limiting
- ☁️ Cloud Deployment (Railway / Render / Azure)
- 📊 Logging & Monitoring
- 📈 Metrics (Prometheus)
- 🧪 Increase Test Coverage
- ⚡ Improve GitHub Actions (Tests + Ruff + Mypy)

---

# 🤝 Author

**Miguel Portela**

GitHub

https://github.com/MiguelP0rtela

LinkedIn

https://www.linkedin.com/in/miguel-portela-helloworld/

---

# 📄 License

This project is licensed under the MIT License.