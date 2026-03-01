from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

from app.core.database import engine, Base
from app.routers import users, products, carts, payment


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("⏳ Checking database tables...")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Database is ready!")

    yield

    print("🛑 Server is shutting down...")


app = FastAPI(title="Async E-Commerce API", lifespan=lifespan)

os.makedirs("static/images", exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


app.include_router(users.router)
app.include_router(products.router)
app.include_router(carts.router)
app.include_router(payment.router)


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    """Renders the user login page."""
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    """Renders the user registration page."""
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/cart", response_class=HTMLResponse)
async def cart_page(request: Request):
    """Renders the user's shopping cart page."""
    return templates.TemplateResponse("cart.html", {"request": request})


@app.get("/success", response_class=HTMLResponse)
async def success_page(request: Request):
    """Page displayed when a Stripe payment is successful."""
    return templates.TemplateResponse("success.html", {"request": request})
