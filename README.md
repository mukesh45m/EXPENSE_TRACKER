# Expense Tracker

A simple and user-friendly **Expense Tracker** built with **Django**. This application helps users manage their daily expenses by organizing them into categories and tracking spending efficiently.

## Features

* User Authentication (Login & Logout)
* Add, Edit, and Delete Expenses
* Create and Manage Expense Categories
* Assign Categories to Expenses
* Search Expenses
* Filter Expenses by Category
* View Total Expenses
* Responsive Bootstrap UI
* Admin Panel for Data Management

## Tech Stack

* **Backend:** Django
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite
* **Language:** Python

## Project Structure

```text
Expense-Tracker/
│── expenses/
│── templates/
│── static/
│── db.sqlite3
│── manage.py
└── requirements.txt
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Expense-Tracker.git
```

2. Navigate to the project

```bash
cd Expense-Tracker
```

3. Create a virtual environment

```bash
python -m venv venv
```

4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Apply migrations

```bash
python manage.py migrate
```

7. Run the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

## Screenshots

Add screenshots of:

* Dashboard
* Add Expense
* Add Category
* Expense List
* Search & Filter

## Future Improvements

* Monthly Expense Reports
* Charts & Graphs
* Budget Management
* Export to Excel/PDF
* REST API using Django REST Framework
* Dark Mode
* User-wise Expense Analytics

## Author

**Mukesh Patel**

* Python Developer
* Django Developer

## License

This project is created for learning and portfolio purposes.
