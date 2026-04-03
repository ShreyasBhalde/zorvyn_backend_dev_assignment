# 💰 Finance Dashboard Backend (Django + DRF)

---

## 📌 Project Overview

This project is a backend system designed to manage financial records with role-based access control and dashboard analytics.

The system allows different users (Admin, Analyst, Viewer) to interact with financial data based on their permissions. It demonstrates clean backend architecture, proper API design, and real-world features such as filtering, pagination, and secure authentication.

## 📦 Sample Database

A sample SQLite database (`db.sqlite3`) with pre-populated data has been included in the repository for quick testing and demonstration purposes.
Users with different roles (Admin, Analyst, Viewer) and sample financial records are already available in the database.
---

## 🎯 Objectives

* Design a modular backend system
* Implement role-based access control (RBAC)
* Provide CRUD operations for financial records
* Build dashboard APIs for aggregated insights
* Ensure proper validation and error handling
* Document APIs using Swagger

---

## 🚀 Tech Stack

* **Backend Framework**: Django
* **API Framework**: Django REST Framework (DRF)
* **Database**: SQLite3
* **Authentication**: Token-based authentication (DRF TokenAuth)
* **API Documentation**: Swagger (drf-yasg)

---

## 🏗️ Project Architecture

The project is structured into three main apps for better separation of concerns:

### 👤 1. users App

Responsible for:

* User registration
* User login
* Role assignment (Admin, Analyst, Viewer)
* Token generation for authentication

---

### 💰 2. records App

Responsible for:

* Creating, updating, deleting financial records
* Listing records with:

  * Filtering (category, date range)
  * Search (category and notes)
  * Pagination
* Soft delete implementation (records are not permanently removed)

---

### 📊 3. dashboard App

Responsible for:

* Providing aggregated financial insights:

  * Total income
  * Total expenses
  * Net balance
  * Category-wise summary

---

## 👥 Role-Based Access Control (RBAC)

| Role    | Permissions                                |
| ------- | ------------------------------------------ |
| Admin   | Full access (Create, Update, Delete, View) |
| Analyst | View records + access dashboard            |
| Viewer  | View records only                          |

### 🔐 Enforcement

* Implemented using DRF permission classes
* Backend strictly controls access (not frontend)

---

## 🔐 Authentication (Token-Based)

### 🔹 How It Works

1. User registers via `/users/register/`
2. User logs in via `/users/login/`
3. On successful login, a **token** is generated
4. This token must be sent with every protected API request

---

### 🔹 Token Usage

All secured APIs require the following header:

Authorization: Token <your_token>

Example:
Authorization: Token 1020a0282bd2e6cf78c0597acb4206e11b7472a7

---

### 🔹 Why Token Authentication?

* Stateless authentication (no sessions required)
* Secure (password not sent repeatedly)
* Suitable for frontend/mobile integration

---

## 📡 API Endpoints

---

### 👤 User APIs

#### ➤ Register User

POST /users/register/

#### ➤ Login User

POST /users/login/

---

### 💰 Records APIs

#### ➤ List Records

GET /records/

Supports:

* Category filter → `/records/?category=rent`
* Date range → `/records/?start_date=2026-03-01&end_date=2026-03-31`
* Search → `/records/?search=rent`
* Pagination → `/records/?page=1`

---

#### ➤ Create Record (Admin Only)

POST /records/create/

---

#### ➤ Update Record (Admin Only)

PUT /records/update/<id>/

---

#### ➤ Delete Record (Soft Delete, Admin Only)

DELETE /records/delete/<id>/

---

### 📊 Dashboard APIs

#### ➤ Summary API

GET /dashboard/summary/

Returns:

* Total income
* Total expenses
* Net balance

---

#### ➤ Category-wise Summary

GET /dashboard/category/

---

## 🔍 Request Body Example

### ➤ Create / Update Record

{
"amount": 5000,
"type": "income",
"category": "salary",
"date": "2026-04-01",
"notes": "Monthly salary"
}

---

## 📘 Swagger API Documentation

Swagger UI is integrated for API documentation and testing.

### 🔗 Access Swagger:

http://localhost:8000/swagger/

### Features:

* View all APIs
* Test APIs directly
* Add authentication token using "Authorize 🔒" button

---

## 🧪 How to Use (Step-by-Step)

1. Register a user
2. Login to receive token
3. Click "Authorize 🔒" in Swagger
4. Enter:
   Token <your_token>
5. Test APIs

---

## ⚙️ Setup Instructions

1. Clone repository:
   git clone <your_repo_url>

2. Navigate to project:
   cd finance_dashboard

3. Install dependencies:
   pip install -r requirements.txt

4. Apply migrations:
   python manage.py makemigrations
   python manage.py migrate

5. Run server:
   python manage.py runserver

---

## 💡 Features Implemented

* Role-based access control (RBAC)
* Token-based authentication
* CRUD operations for financial records
* Filtering (category, date range)
* Search functionality
* Pagination
* Soft delete mechanism
* Dashboard analytics APIs
* Swagger API documentation

---

## 📌 Assumptions

* Only Admin users can create, update, and delete records
* Analysts can access dashboard insights
* Viewers have read-only access
* Soft delete is used instead of permanent deletion

---

## 🚀 Future Improvements

* JWT-based authentication
* Monthly trend analysis
* Rate limiting
* Caching for dashboard APIs
* Export reports (PDF/Excel)

---

## 🎯 Conclusion

This project demonstrates strong backend engineering practices including modular design, secure authentication, role-based access control, and efficient data processing for real-world financial systems.
