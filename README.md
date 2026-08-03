# 🚀 Task Manager API

A production-oriented REST API built with **FastAPI** to practice modern backend development concepts including
authentication, database design, security, Docker, testing, and deployment.

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
- 🐳 Docker support for PostgreSQL
- ⚡ Interactive API documentation (Swagger & ReDoc)
- ⚙️ Environment-based configuration with `.env`

---

## 🛠️ Tech Stack

| Technology  | Purpose              |
|-------------|----------------------|
| Python 3.14 | Programming Language |
| FastAPI     | REST API Framework   |
| SQLAlchemy  | ORM                  |
| PostgreSQL  | Database             |
| Docker      | PostgreSQL Container |
| Pydantic    | Data validation      |
| JWT         | Authentication       |
| Argon2      | Password hashing     |
| Uvicorn     | ASGI Server          |

---

## 🏗️ Architecture

The project follows a layered architecture to keep the code modular, maintainable and easy to scale.

```text
app/
├── core/          # Security, configuration
├── database/      # Database connection
├── models/        # SQLAlchemy models
├── routers/       # API endpoints
├── schemas/       # Pydantic schemas
└── main.py        # Application entry point
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

### 4. Configure the environment

Create a `.env` file using `.env.example` as a template.

Example:

```env
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

DATABASE_URL= your-database-url
```

### 5. Start PostgreSQL

```bash
docker compose up -d
```

### 6. Run the application

```bash
python -m uvicorn app.main:app --reload
```

---

## 📖 API Documentation

After starting the server, the documentation is available at:

| Documentation | URL                         |
|---------------|-----------------------------|
| Swagger UI    | http://127.0.0.1:8000/docs  |
| ReDoc         | http://127.0.0.1:8000/redoc |

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
| Refresh Tokens                           |   ⏳   |
| Role-Based Authorization                 |   ⏳   |
| Rate Limiting                            |   ⏳   |
| Unit Tests                               |   ⏳   |
| GitHub Actions (CI/CD)                   |   ⏳   |
| Dockerized API                           |   ⏳   |
| Deployment                               |   ⏳   |

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

## 🚀 Roadmap

The next planned improvements are:

- ✅ Complete CRUD for Users
- ✅ Complete CRUD for Tasks
- ✅ Database migrations with Alembic
- ✅ Task completion status
- ✅ Automatic timestamps
- ✅ Filtering and pagination
- ⏳ Unit testing with Pytest
- 🔄 Refresh Token authentication
- 🔄 Role-based authorization
- 🔄 GitHub Actions (CI/CD)
- 🔄 Full Docker support
- 🔄 Cloud deployment

---

## 🤝 Author

**Miguel Portela**

GitHub: https://github.com/MiguelP0rtela

---

## 📄 License

This project is licensed under the MIT License.