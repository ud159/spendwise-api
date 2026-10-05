

# SpendWise API

A personal expense management REST API built with **FastAPI** and **PostgreSQL**.

## 🚀 Live Demo

* **API:** https://spendwise-api1.onrender.com
* **Swagger Docs:** https://spendwise-api1.onrender.com/docs

## ✨ Features

* 🔐 JWT-based authentication
* 👤 User registration and login
* 💰 Create, read, update, and delete expenses
* 🔎 Filter expenses by category
* 📄 Pagination support
* 📊 Expense summary
* 🔒 User-specific expense access
* ✅ Request validation with Pydantic
* 🗄️ PostgreSQL database
* 📚 Interactive Swagger API documentation

## 🛠️ Tech Stack

| Technology       | Purpose              |
| ---------------- | -------------------- |
| Python           | Programming language |
| FastAPI          | REST API framework   |
| PostgreSQL       | Relational database  |
| SQLAlchemy       | ORM                  |
| Pydantic         | Data validation      |
| JWT              | Authentication       |
| Passlib / bcrypt | Password hashing     |
| Uvicorn          | ASGI server          |
| Render           | Deployment           |

## 📁 Project Structure

```text
spendwise-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── routes/
│       ├── __init__.py
│       ├── auth.py
│       └── expenses.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔐 Authentication

SpendWise uses JWT-based authentication.

### Register

```http
POST /auth/register
```

### Login

```http
POST /auth/login
```

After login, use the returned JWT token to access protected expense endpoints.

## 📌 API Endpoints

### Authentication

| Method | Endpoint         | Description           |
| ------ | ---------------- | --------------------- |
| POST   | `/auth/register` | Register a new user   |
| POST   | `/auth/login`    | Login and receive JWT |

### Expenses

| Method | Endpoint                 | Description            |
| ------ | ------------------------ | ---------------------- |
| POST   | `/expenses/`             | Create an expense      |
| GET    | `/expenses/`             | List expenses          |
| GET    | `/expenses/summary`      | Get expense summary    |
| GET    | `/expenses/{expense_id}` | Get a specific expense |
| PUT    | `/expenses/{expense_id}` | Update an expense      |
| DELETE | `/expenses/{expense_id}` | Delete an expense      |

## 📊 HTTP Status Codes

| Status | Meaning            |
| ------ | ------------------ |
| 200    | Successful request |
| 201    | Resource created   |
| 204    | Resource deleted   |
| 400    | Bad request        |
| 401    | Unauthorized       |
| 404    | Resource not found |
| 422    | Validation error   |

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git git clone https://github.com/ud159/spendwise-api.git
cd spendwise-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/spendwise
SECRET_KEY=your-secret-key
```

### 5. Start the server

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## 🌐 Deployment

The API is deployed using **Render** with PostgreSQL.

Live API:

https://spendwise-api1.onrender.com

Swagger documentation:

https://spendwise-api1.onrender.com/docs

## 🔒 Security

* Passwords are securely hashed before storage.
* JWT tokens protect authenticated endpoints.
* Users can access only their own expenses.
* Sensitive environment variables are stored outside the source code.

## 🔮 Future Improvements

* Automated tests with Pytest
* Database migrations with Alembic
* Docker support
* Expense analytics and charts
* Monthly budget tracking
* CI/CD with GitHub Actions
* Production monitoring and logging

## 📌 Project Status

**Deployed and functional.**

The API is currently available online with interactive Swagger documentation.

## 👨‍💻 Author

**Udaya H C**

BTech Computer Science and Engineering





