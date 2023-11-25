# DRF E-Market

## Introduction

DRF E-Market is a Django REST Framework e-commerce app that allows users to browse, buy, and review products. It also provides CRUD (create, read, update, delete) operations for products, users, orders, and reviews. It uses JWT (JSON Web Token) authentication and admin permissions on critical functions like update and delete.


## Features

1.**Product list and detail views**
2.**User registration and login**
3.**Order creation and checkout**
4.**Review submission and rating**
5.**JWT authentication and authorization**
6.**Admin dashboard and permissions**

## Setup Instructions

# 1. Clone the Repository:
```bash
git clone https://github.com/Demo-23home/DRF_E_Market.git
```
# 2. Create Virtual Environment:
```
python -m venv venv
```
# 3. Activate Virtual Environment:
```
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
# 4. Install Dependencies:
```
pip install -r requirements.txt
```
# 5. Run Migrations:
```
python manage.py migrate
```
# 6. Create Superuser:
```
python manage.py createsuperuser
```
# 7. Run the Development Server:
```
python manage.py runserver
```

# 8. Access API doc Swagger page:
```
localhost:8000/
```
