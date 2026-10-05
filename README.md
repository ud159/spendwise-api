# SpendWise API

A production-ready personal expense management REST API built with FastAPI and PostgreSQL.

## 🚀 Overview

SpendWise API is a backend application that allows users to securely manage
their personal expenses through a RESTful API.

The project implements JWT-based authentication, password hashing,
expense CRUD operations, filtering, pagination, validation, and
user-specific data isolation.

## 🚀 Live Demo

**API:** https://spendwise-api1.onrender.com

**Swagger API Documentation:** https://spendwise-api1.onrender.com/docs


## ✨ Features

- User registration and authentication
- JWT-based authorization
- Secure password hashing
- Create, read, update, and delete expenses
- Category-based filtering
- Pagination
- Spending summary
- Input validation using Pydantic
- PostgreSQL database
- SQLAlchemy ORM
- Interactive Swagger API documentation
- User-level data isolation

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend language |
| FastAPI | REST API framework |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM |
| Pydantic | Data validation |
| JWT | Authentication |
| Passlib + bcrypt | Password hashing |
| Uvicorn | ASGI server |


## 📁 Project Structure

```text
spendwise-api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── routes/
│       ├── auth.py
│       └── expenses.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md




Then include:

```markdown
## 🔐 Authentication

SpendWise uses JWT-based authentication.

1. Register a user.
2. Login with email and password.
3. Receive an access token.
4. Use the token to access protected expense endpoints.

Authorization header:

```text
Authorization: Bearer <access_token>


Then API endpoints:

```markdown
## 📡 API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Authenticate user |

### Expenses

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/expenses/` | Create expense |
| GET | `/expenses/` | List expenses |
| GET | `/expenses/summary` | Get spending summary |
| GET | `/expenses/{expense_id}` | Get expense |
| PUT | `/expenses/{expense_id}` | Update expense |
| DELETE | `/expenses/{expense_id}` | Delete expense |

## 📊 HTTP Status Codes

| Status Code | Meaning |
|-------------|---------|
| 200 | Successful request |
| 201 | Resource created |
| 204 | Resource deleted |
| 400 | Bad request |
| 401 | Authentication failed |
| 404 | Resource not found |
| 422 | Validation error |

## 📚 API Documentation

After starting the application, interactive Swagger documentation is available at:

```text
http://127.0.0.1:8000/docs


---

# 8. Add environment setup

This is important because someone should be able to clone your project and understand how to run it.

```markdown
## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/spendwise-api.git
cd spendwise-api

###2.Create virtual environment
'''bash
python -m venv venv

###3.Activate virtual environment
'''bash
.\venv\Scripts\Activate.ps1

###4.Install dependencies
'''bash
pip install -r requirements.txt

###Create environment variables
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/spendwise
SECRET_KEY=your-secret-key

###6. run application
'''bash
uvicorn app.main:app --reload


---

# 7. Add Security section

```markdown
## 🔒 Security

- Passwords are hashed using bcrypt.
- JWT tokens are used for authentication.
- Protected endpoints require authentication.
- Users can access only their own expenses.
- Sensitive configuration is stored in environment variables.
- `.env` is excluded from version control.

## 🔮 Future Improvements

- Automated test suite with Pytest
- Alembic database migrations
- Expense date-range filtering
- Monthly spending analytics
- Docker support
- CI/CD pipeline
- Production deployment




## 👨‍💻 Author

**Udaya H C**

BTech Computer Science and Engineering
