import asyncio
import stripe
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from app import models
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.core.config import settings


stripe.api_key = settings.STRIPE_SECRET_KEY

router = APIRouter(
    prefix="/payment",
    tags=["Payment"]
)


@router.post("/create-checkout-session")
async def create_checkout_session(
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    query = select(models.CartItem).where(
        models.CartItem.user_id == current_user.id
    ).options(selectinload(models.CartItem.product))
    result = await db.execute(query)
    cart_items = result.scalars().all()

    if not cart_items:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Your cart is empty. Payment cannot be processed."
        )

    line_items = []
    for item in cart_items:
        line_items.append({
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": item.product.title,
                },
                "unit_amount": int(item.product.price * 100),
            },
            "quantity": item.quantity,
        })

    try:
       
        session = await asyncio.to_thread(
            stripe.checkout.Session.create,
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url="http://127.0.0.1:8000/success",
            cancel_url="http://127.0.0.1:8000/cart",
        )
        return {"checkout_url": session.url}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
