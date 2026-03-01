# 🛒 TechStore — Async E-Commerce API

A full-stack e-commerce web application built with **FastAPI** and **async SQLAlchemy**, featuring JWT authentication, a product catalog, shopping cart, and Stripe payment integration.

## ✨ Features

- 🔐 JWT-based user authentication (register / login)
- 📦 Product catalog with image upload and stock tracking
- 🛒 Shopping cart (add, update quantity, remove, clear)
- 💳 Stripe Checkout integration
- 🎨 Responsive frontend with Tailwind CSS

## 🗂️ Project Structure

```
16-OnlineShop/
├── app/
│   ├── main.py          # FastAPI app & page routes
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── core/
│   │   ├── config.py    # Settings (.env)
│   │   ├── database.py  # Async DB engine & session
│   │   ├── security.py  # Password hashing & JWT
│   │   └── dependencies.py  # Auth dependency
│   └── routers/
│       ├── users.py     # /users
│       ├── products.py  # /products
│       ├── carts.py     # /cart
│       └── payment.py   # /payment
├── templates/           # Jinja2 HTML pages
├── static/images/       # Uploaded product images
└── .env
```

## 🚀 Getting Started

### 1. Clone & install dependencies

```bash
git clone https://github.com/Kerim-Altny/16-OnlineShop.git
cd 16-OnlineShop
pip install -r requirements.txt
```

### 2. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+asyncpg://postgres:your-password@localhost:5432/ecommerce_db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
```

### 3. Run the server

```bash
uvicorn app.main:app --reload
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI, async SQLAlchemy |
| Database | PostgreSQL (via asyncpg) |
| Auth | JWT (PyJWT) + bcrypt |
| Payments | Stripe Checkout |
| Frontend | Jinja2, Tailwind CSS, Font Awesome |

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users/register` | Register a new user |
| POST | `/users/login` | Login & get JWT token |
| GET | `/products/` | List all products |
| POST | `/products/` | Add a new product |
| POST | `/products/upload-image` | Upload a product image |
| GET | `/cart/` | Get current user's cart |
| POST | `/cart/add/{id}` | Add product to cart |
| PUT | `/cart/update/{id}` | Update quantity |
| DELETE | `/cart/remove/{id}` | Remove from cart |
| DELETE | `/cart/clear` | Clear entire cart |
| POST | `/payment/create-checkout-session` | Start Stripe checkout |

Interactive API docs available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
