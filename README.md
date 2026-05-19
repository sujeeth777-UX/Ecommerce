# ShopModern - Django E-Commerce Platform

A fully functional, responsive, and secure full-stack e-commerce web application built from scratch using the Django framework and Tailwind CSS. 

## 🚀 Features

- **Dynamic Product Catalog**: Browse products with ease, featuring image support and dynamic pricing.
- **Category Filtering**: Quickly filter the product catalog by categories (e.g., Electronics, Clothing) using a modern sidebar.
- **Secure Local Authentication**: Independent user registration, login, and logout flows with secure password hashing and personalized customer profiles.
- **Session-Based Shopping Cart**: Users can add, remove, and update product quantities in their cart without losing their data on page refresh. 
- **End-to-End Checkout Pipeline**: Seamlessly convert shopping carts into official database Order records linked to specific users.
- **Order History Dashboard**: A dedicated portal for logged-in users to track their past purchases and order statuses.
- **Admin Dashboard**: Full integration with the Django Admin panel for store owners to manage inventory, categories, customers, and orders.
- **Modern UI**: A clean, beautiful, and fully responsive user interface styled with Tailwind CSS.

## 🛠️ Tech Stack

- **Backend**: Python, Django (MVT Architecture)
- **Frontend**: HTML5, Django Templates, Tailwind CSS (via CDN)
- **Database**: SQLite3 (Development) 
- **Documentation**: python-docx

## 💻 Local Setup & Installation

Follow these steps to run the project locally on your machine.

### Prerequisites
- Python 3.8+ installed on your machine.
- `pip` package manager.

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-github-repo-url>
   cd ecommerce
   ```

2. **Create a Virtual Environment (Optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install django pillow
   ```

4. **Apply Database Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser (Admin)**
   Create an admin account so you can manage the store's inventory.
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   The application will now be running at `http://127.0.0.1:8000/`.

## 🛒 How to Use

1. **Populate the Store**: Go to `http://127.0.0.1:8000/admin/`, log in with your superuser credentials, and add a few Categories and Products to the database.
2. **Shop**: Go back to the homepage (`http://127.0.0.1:8000/`), browse your new products, and add them to your cart.
3. **Checkout**: Click the "Cart" button, review your items, and click "Proceed to Checkout" to place your order!

## 📝 License
This project is open-source and available under the MIT License.
