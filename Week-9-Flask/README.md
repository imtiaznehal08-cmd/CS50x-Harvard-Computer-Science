# CS50x - Week 9: Flask (Web Development)

This repository contains my solutions for the web development projects in **Week 9** of Harvard's CS50x introduction to computer science. This module marked the transition from frontend development to full-stack engineering, using the **Flask** microframework in Python to handle server-side routing, request validation, state management via sessions, and relational database interaction via SQLite.

## 📋 Projects Overview

1. **Birthdays**: A lightweight web application that reads from and writes to a database to log and display upcoming celebrations.
2. **C$50 Finance**: A robust full-stack web application that allows users to manage a virtual stock portfolio, look up real-time market data, and execute mock stock transactions (buy/sell).

---

## 🎂 1. Birthdays Application

A full-stack tracking application designed to master simple `GET` and `POST` server routing mechanisms combined with persistent database updates.

### ⚙️ Implementation Architecture
* **Backend (`app.py`):** Configures an explicit single-route controller logic at `/` handling both data ingestion and data rendering loops.
    * *`GET` Request:* Queries the underlying SQLite database (`birthdays.db`) via `db.execute("SELECT * FROM birthdays")` to capture all stored profiles and loads them dynamically into the frontend canvas.
    * *`POST` Request:* Captures user input fields (`name`, `month`, `day`), passes them through defensive range validation guardrails (checking that dates fit within logical `1–12` and `1–31` parameters), executes an `INSERT` SQL transaction, and returns a seamless user redirect to the index view loop.
* **Frontend UI (`index.html`):** Renders clean entry form layouts using custom numeric range parameters, accompanied by an explicit Jinja2 rendering table to output user metrics dynamically on page render.

---

## 📈 2. C$50 Finance (Virtual Stock Trading Hub)

A mock full-stack stock trading platform engineered with secure multi-user architecture, session-backed authentication states, dynamic API lookups, and transactional history ledgers.

### 📄 Comprehensive Page Map & Routes
* `/login` & `/logout` — Validates credentials using secure password hashing techniques and tracks operational session objects natively.
* `/register` — Implements backend form checking to avoid username duplicates and enforces password parameter checking before writing to the database.
* `/` (Index Portfolio) — Calculates user asset valuations across active holdings by mapping outstanding quantities against live API price lookups.
* `/quote` — Queries external stock exchange APIs to yield rapid ticker calculations and prices.
* `/buy` — Validates buying parameters (ensures inputs are positive integers) and tracks balance limitations before executing an equity purchase.
* `/sell` — Evaluates real-time holdings availability to prevent short-selling anomalies, decrementing inventory while processing equity liquidations.
* `/history` — Compiles a complete ledger of all stock transactions with real-time audit trail logs.

### 🛠️ Core Functional Logic
* **Dynamic Content Inheritance:** Uses a baseline frame layout layout (`layout.html`) containing responsive Bootstrap navigation

**Install all required dependencies specified in the manifest:**


pip install -r requirements.txt
Launch the target environment local test servers:

**To run Birthdays:**
flask run
**To run Finance:**
flask run
