![Python](https://img.shields.io/badge/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

# 🚀 Task Manager API

A production-oriented REST API built with **FastAPI**, focused on modern backend development practices including
authentication, authorization, database management, testing, containerization, security, and clean architecture.

The API provides secure authentication using **JWT Access Tokens** and **Refresh Tokens**, password hashing with
**Argon2**, **PostgreSQL** as the database, and follows modern backend development practices.

---

# ✨ Features

- 👤 User registration and management
- 📝 Task management (CRUD)
- 🔑 JWT Authentication
- 🔄 Refresh Token authentication
- 🔁 Refresh Token Rotation
- 🚪 Logout and Refresh Token revocation
- 👥 Role-Based Authorization
- 🔒 Password hashing using Argon2
- 🔐 Protected API endpoints
- 🛡️ User-based task authorization
- 🗄️ PostgreSQL database integration
- 📦 SQLAlchemy ORM
- 📜 Alembic database migrations
- 🐳 Fully Dockerized application
- ⚡ Interactive API documentation (Swagger & ReDoc)
- ⚙️ Environment-based configuration with `.env`
- 🧪 Automated API testing
- 📊 96% test coverage

---

# 🛠️ Tech Stack

| Technology      | Purpose                       |
|-----------------|-------------------------------|
| Python 3.14     | Programming Language          |
| FastAPI         | REST API Framework            |
| SQLAlchemy      | ORM                           |
| PostgreSQL      | Database                      |
| Alembic         | Database Migrations           |
| Docker          | Containerization              |
| Docker Compose  | Multi-container orchestration |
| Pydantic        | Data Validation               |
| JWT             | Authentication                |
| pwdlib (Argon2) | Password Hashing              |
| Uvicorn         | ASGI Server                   |
| Pytest          | Automated Testing             |

---

# 🏗️ Architecture

```text
app/
├── core/          # Configuration and security
├── database/      # Database engine and session management
├── models/        # SQLAlchemy models
├── routers/       # API endpoints
├── schemas/       # Pydantic schemas
└── main.py        # FastAPI application
```

The project follows a modular architecture separating:

- API routing
- Data validation
- Database models
- Authentication and security
- Database configuration
- Application configuration

---

# 🔐 Security

The API implements several security mechanisms:

- JWT-based authentication
- Short-lived access tokens
- Rotating refresh tokens
- Refresh token revocation
- Argon2 password hashing
- Role-Based Authorization
- Protected API endpoints
- User-based task authorization
- Password change validation
- Pydantic input validation
- Environment-based secret management

---

# 🔄 Authentication Flow

The authentication system follows the following flow:

```text
1. User registers
        ↓
2. User logs in
        ↓
3. API returns Access Token + Refresh Token
        ↓
4. Access Token is used for protected endpoints
        ↓
5. Access Token expires
        ↓
6. Refresh Token is sent to /auth/refresh
        ↓
7. Old Refresh Token is revoked
        ↓
8. New Access Token + Refresh Token are issued
        ↓
9. Logout revokes the active Refresh Token
```

Refresh Token Rotation prevents previously used refresh tokens from being reused.

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/MiguelP0rtela/task-manager-api.git
cd task-manager-api
```

---

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

> Never commit real secrets or credentials to the repository.

---

## 5. Run the application

### Option 1 — Local

Start PostgreSQL:

```bash
docker compose up -d postgres
```

Run the API:

```bash
python -m uvicorn app.main:app --reload
```

---

### Option 2 — Docker

```bash
docker compose up --build
```

---

The API will be available at:

```text
http://localhost:8000
```

---

# 📖 API Documentation

Once the application is running:

| Documentation | URL                         |
|---------------|-----------------------------|
| Swagger UI    | http://localhost:8000/docs  |
| ReDoc         | http://localhost:8000/redoc |

Swagger can be used to interact directly with the API and test authenticated endpoints.

---

# 📡 Main Endpoints

## Authentication

| Method | Endpoint        | Description                                        |
|--------|-----------------|----------------------------------------------------|
| POST   | `/auth/login`   | Login and obtain access/refresh tokens             |
| POST   | `/auth/refresh` | Rotate refresh token and obtain a new access token |
| POST   | `/auth/logout`  | Revoke refresh token                               |

---

## Users

| Method | Endpoint             | Description                    |
|--------|----------------------|--------------------------------|
| POST   | `/users`             | Register user                  |
| GET    | `/users`             | List users (Admin)             |
| GET    | `/users/{id}`        | Get user (Admin)               |
| PUT    | `/users/{id}`        | Update user (Admin)            |
| DELETE | `/users/{id}`        | Delete user (Admin)            |
| GET    | `/users/me`          | Get current authenticated user |
| PATCH  | `/users/me/password` | Change current user's password |

---

## Tasks

| Method | Endpoint      | Description                      |
|--------|---------------|----------------------------------|
| POST   | `/tasks`      | Create task                      |
| GET    | `/tasks`      | List authenticated user's tasks  |
| GET    | `/tasks/{id}` | Get authenticated user's task    |
| PATCH  | `/tasks/{id}` | Update authenticated user's task |
| DELETE | `/tasks/{id}` | Delete authenticated user's task |

Tasks are associated with the authenticated user. Users cannot access or modify tasks belonging to other users.

---

# 🧪 Testing

The project includes automated API tests covering:

- User registration
- User authentication
- Invalid credentials
- JWT authentication
- Protected endpoints
- Refresh token generation
- Refresh token rotation
- Refresh token revocation
- Logout
- Task authorization
- User authorization
- Password changes
- Validation errors
- Duplicate users
- Health checks
- Task CRUD operations
- User CRUD operations

### Run all tests

```bash
pytest
```

### Run tests with coverage

```bash
pytest --cov=app --cov-report=term-missing
```

Current test coverage:

```text
96%
```

---

## 🌐 Live Demo

The API is publicly deployed and available to test online.

🔗 **[Task Manager API](https://task-manager-api-mw96.onrender.com/)**

📚 **[Interactive Swagger Documentation](https://task-manager-api-mw96.onrender.com/docs)**

No local setup is required. Visit the Swagger documentation to explore the available endpoints and interact with the API directly.

---

# 📌 Project Status

| Feature                      | Status |
|------------------------------|:------:|
| User CRUD                    |   ✅   |
| Task CRUD                    |   ✅   |
| JWT Authentication           |   ✅   |
| Refresh Tokens               |   ✅   |
| Refresh Token Rotation       |   ✅   |
| Login Endpoint               |   ✅   |
| Refresh Endpoint             |   ✅   |
| Logout / Token Revocation    |   ✅   |
| Password Hashing             |   ✅   |
| Password Change              |   ✅   |
| Protected Routes             |   ✅   |
| Role-Based Authorization     |   ✅   |
| User Authorization           |   ✅   |
| Task Authorization           |   ✅   |
| Environment Configuration    |   ✅   |
| API Documentation            |   ✅   |
| Dockerized PostgreSQL        |   ✅   |
| Dockerized Application       |   ✅   |
| Alembic Migrations           |   ✅   |
| Task Status                  |   ✅   |
| Created / Updated timestamps |   ✅   |
| Filtering & Pagination       |   ✅   |
| Automated Tests              |   ✅   |
| GitHub Actions (CI/CD)       |   ✅   |
| Deployment                   |   ✅   |
| Test Coverage                |  96%   |
| Rate Limiting                |   ⏳   |
| Logging & Monitoring         |   ⏳   |

---

# 🎯 Project Goals

The goal of this project is to build a production-oriented REST API while applying modern backend development practices,
including:

- Authentication
- Authorization
- Database migrations
- Docker
- Secure password hashing
- API security
- Testing
- Clean backend architecture
- CI/CD
- Production-oriented API design

---

# 🎓 Learning Objectives

This project was developed to strengthen practical knowledge of:

- REST API development
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Docker
- Alembic
- JWT Authentication
- Refresh Token Authentication
- Refresh Token Rotation
- Secure Password Hashing
- Role-Based Authorization
- Backend Architecture
- API Security
- Software Engineering Best Practices
- Automated Testing
- CI/CD

---

# 🚀 Future Improvements

The core API functionality is complete. Potential future improvements include:

- 🚦 Rate Limiting
- ☁️ Cloud Deployment
- 📊 Logging & Monitoring
- 📈 Metrics with Prometheus
- 🧹 Ruff and Mypy integration
- 🔐 Additional security hardening
- 🩺 Production health and readiness checks

---

# 🤝 Author

**Miguel Portela**

### GitHub

https://github.com/MiguelP0rtela

### LinkedIn

https://www.linkedin.com/in/miguel-portela-helloworld/

---

# 📄 License

This project is licensed under the MIT License.