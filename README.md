![Python](https://img.shields.io/badge/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

# 🚀 Task Manager API

A production-oriented REST API built with FastAPI that demonstrates modern backend development practices including
authentication, database design, testing, Docker, security, and clean architecture.

The API provides secure user authentication using **JWT**, password hashing with **Argon2**, and **PostgreSQL** as the
database while following clean architecture and backend best practices.

---

## ✨ Features

- 👤 User registration and management
- 📝 Task management (CRUD)
- 🔑 Secure authentication with JWT
- 🔒 Password hashing using Argon2
- 🗄️ PostgreSQL database integration
- 📦 SQLAlchemy ORM
- 🐳 Fully Dockerized application (FastAPI + PostgreSQL)
- ⚡ Interactive API documentation (Swagger & ReDoc)
- ⚙️ Environment-based configuration with `.env`

---

## 🛠️ Tech Stack

| Technology     | Purpose                       |
|----------------|-------------------------------|
| Python 3.14    | Programming Language          |
| FastAPI        | REST API Framework            |
| SQLAlchemy     | ORM                           |
| PostgreSQL     | Database                      |
| Docker         | Containerization              |
| Docker Compose | Multi-container orchestration |
| Pydantic       | Data validation               |
| JWT            | Authentication                |
| Argon2         | Password hashing              |
| Uvicorn        | ASGI Server                   |

---

## 🏗️ Architecture

The project follows a layered architecture to keep the code modular, maintainable and easy to scale.

```text
app/
├── core/          # Configuration, security and validators
├── database/      # Database engine and session management
├── models/        # SQLAlchemy ORM models
├── routers/       # API endpoints
├── schemas/       # Pydantic request/response schemas
└── main.py        # FastAPI application entry point
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MiguelP0rtela/task-manager-api.git
cd task-manager-api
```

### 2. Create and activate a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the environment variables

Create a `.env` file using `.env.example` as a template.

| Variable                      | Description                                |
|-------------------------------|--------------------------------------------|
| `SECRET_KEY`                  | Secret key used to sign JWT tokens         |
| `ALGORITHM`                   | JWT signing algorithm                      |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | JWT token expiration time (minutes)        |
| `DATABASE_URL`                | PostgreSQL connection string               |
| `TEST_DATABASE_URL`           | PostgreSQL test database connection string |

Example:

```env
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

DATABASE_URL=postgresql://user:password@localhost:5432/task_manager
TEST_DATABASE_URL=postgresql://user:password@localhost:5432/task_manager_test
```

### 5. Run the application

#### Option 1 — Run locally

Start the PostgreSQL container:

```bash
docker compose up -d postgres
```

Run the API:

```bash
python -m uvicorn app.main:app --reload
```

---

#### Option 2 — Run everything with Docker

Build and start the application:

```bash
docker compose up --build
```

The API will be available at:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

ReDoc:

```
http://localhost:8000/redoc
```

---

## 📖 API Documentation

After starting the server, the documentation is available at:

| Documentation | URL                         |
|---------------|-----------------------------|
| Swagger UI    | http://127.0.0.1:8000/docs  |
| ReDoc         | http://127.0.0.1:8000/redoc |

---

## 🧪 Testing

Run all tests:

```bash
python -m pytest
```

Run all tests with coverage:

```bash
python -m pytest --cov=app --cov-report=term-missing
```

Current code coverage: **88%**

---

## 📌 Project Status

| Feature                                  | Status |
|:-----------------------------------------|:------:|
| User CRUD                                |   ✅   |
| Task CRUD                                |   ✅   |
| JWT Authentication                       |   ✅   |
| Password Hashing                         |   ✅   |
| Protected Routes                         |   ✅   |
| Environment Configuration                |   ✅   |
| API Documentation (Swagger/OpenAPI)      |   ✅   |
| Dockerized PostgreSQL                    |   ✅   |
| Alembic Migrations                       |   ✅   |
| Task Status (Completed / Pending)        |   ✅   |
| Timestamps (`created_at` / `updated_at`) |   ✅   |
| Filtering & Pagination                   |   ✅   |
| Unit Tests                               |   ✅   |
| Dockerized Application                   |   ✅   |
| GitHub Actions (CI/CD)                   |   ✅   |
| Refresh Tokens                           |   ⏳   |
| Role-Based Authorization                 |   ⏳   |
| Rate Limiting                            |   ⏳   |
| Deployment                               |   ⏳   |

---

## 🎯 Project Goals

The purpose of this project is to build a production-oriented REST API while applying modern backend development
practices, including authentication, testing, Docker, database migrations and clean architecture.

---

## 🎯 Learning Objectives

This project is being developed to strengthen practical knowledge of:

- REST API development
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Docker
- JWT Authentication
- Secure password hashing
- Software architecture
- Backend development best practices
- Testing and CI/CD
- Production-ready API design

---

## 🚀 Future Improvements

- 🔄 Refresh Token authentication
- 🔄 Role-based authorization
- 🔄 Rate Limiting
- 🔄 Improve GitHub Actions (Ruff + Mypy)
- 🔄 Improve 
- 🔄 Cloud deployment

---

## 🤝 Author

**Miguel Portela**

- GitHub: **https://github.com/MiguelP0rtela**
- LinkedIn: **https://www.linkedin.com/in/miguel-portela-helloworld/**

---

## 📄 License

This project is licensed under the MIT License.