DRF E-Market
DRF E-Market is a Django REST Framework e-commerce app that allows users to browse, buy, and review products. It also provides CRUD (create, read, update, delete) operations for products, users, orders, and reviews. It uses JWT (JSON Web Token) authentication and admin permissions on critical functions like update and delete.

Features
Product list and detail views
User registration and login
Order creation and checkout
Review submission and rating
JWT authentication and authorization
Admin dashboard and permissions
Installation
To install DRF E-Market, you need to have Python 3.8 or higher and pip installed on your system. Then, follow these steps:

Clone the repository: git clone https://github.com/Demo-23home/DRF_E_Market.git
Navigate to the project directory: cd DRF_E_Market
Create a virtual environment: python -m venv venv
Activate the virtual environment: source venv/bin/activate (on Linux/Mac) or venv\Scripts\activate (on Windows)
Install the requirements: pip install -r requirements.txt
Run the migrations: python manage.py migrate
Create a superuser: python manage.py createsuperuser
Run the server: python manage.py runserver
Usage
To use DRF E-Market, you can access the following endpoints:

localhost:8000/ : you will find all api endpoints documentd there with the usage and parameters 
/api/token/: Obtain a JWT token by providing username and password
/api/token/refresh/: Refresh a JWT token by providing the refresh token
/admin/: Access the admin dashboard (requires admin login)
You can use tools like Postman or curl to test the API endpoints. You can also use the browsable API provided by Django REST Framework.
