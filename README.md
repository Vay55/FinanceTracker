# Finance Tracker

A simple full-stack expense tracker built to learn REST APIs, backend development, and frontend integration.

---

## Features

- Add expenses (amount, category, description)
- View all expenses
- Edit existing expenses
- Delete expenses
- Data stored in PostgreSQL database
- REST API built with FastAPI
- Simple frontend using HTML, CSS, and JavaScript

---

## 🛠️ Tech Stack

**Backend (Python)**
- FastAPI
- SQLAlchemy
- PostgreSQL

**Frontend**
- HTML
- CSS
- JavaScript (Fetch API)

---

## Project Structure

```bash
FinanceFlow/
│  
├── requirements.txt
│  
├── app/
│   └── main.py       # entry point
│   └── route.py      # endpoints
│   └── database.py   # connecting with PostgreSQL using SQLalchemy
│   └── models.py     # PostgreSQl tables
│   └── schemas.py    # Defining datatypes
│
├── frontend/
│   └── index.html          
│   └── style.css
│   └── script.js
└── README.md
```
---

## How to Run

### 1. Backend

- Get into a virtual environment so that the dependancies dont clash with already existing depandcies on the device

```bash
cd backend
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Backend runs on:**

```bash
http://127.0.0.1:8000
```
---

### 2. Frontend

```bash
cd frontend
python3 -m http.server 5500
```

**Backend runs on:**

```bash
http://localhost:5500
```
---

## API endpoints

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| GET    | /expenses      | Get all expenses  |
| POST   | /expenses      | Add new expense   |
| PUT    | /expenses/{id} | Update an expense |
| DELETE | /expenses/{id} | Delete an expense |

---

## What I Learned
- Building REST APIs with FastAPI
- Working with relational databases (PostgreSQL)
- Using SQLAlchemy ORM
- Connecting frontend with backend using fetch API
- Handling real-world issues like CORS and environment setup


