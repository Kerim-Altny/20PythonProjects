from enum import Enum
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from app import models, schemas
from app.core.database import get_db
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


class CartAction(str, Enum):
    increase = "increase"
    decrease = "decrease"


@router.post("/add/{product_id}", status_code=status.HTTP_201_CREATED)
async def add_to_cart(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    query_prod = select(models.Product).where(models.Product.id == product_id)
    result_prod = await db.execute(query_prod)
    product = result_prod.scalars().first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found.")

   
    if product.stock <= 0:
        raise HTTPException(status_code=400, detail="This product is out of stock.")

    query_cart = select(models.CartItem).where(
        models.CartItem.user_id == current_user.id,
        models.CartItem.product_id == product_id
    )
    result_cart = await db.execute(query_cart)
    cart_item = result_cart.scalars().first()

    if cart_item:
      
        if cart_item.quantity >= product.stock:
            raise HTTPException(
                status_code=400,
                detail=f"Sorry, only {product.stock} unit(s) of this product are left in stock."
            )
        cart_item.quantity += 1
    else:
        new_cart_item = models.CartItem(user_id=current_user.id, product_id=product_id, quantity=1)
        db.add(new_cart_item)

    await db.commit()
    return {"message": f"{product.title} has been added to the cart!"}


@router.get("/", response_model=list[schemas.CartItemResponse])
async def get_cart(
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Returns the items in the user's cart in a stable order by ID."""
    query = select(models.CartItem).where(
        models.CartItem.user_id == current_user.id
    ).options(
        selectinload(models.CartItem.product)
    ).order_by(models.CartItem.id)

    result = await db.execute(query)
    cart_items = result.scalars().all()

    return cart_items


@router.put("/update/{product_id}", status_code=status.HTTP_200_OK)
async def update_cart_quantity(
    product_id: int,
    action: CartAction, 
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Increases or decreases a cart item's quantity based on stock availability."""
    query = select(models.CartItem).where(
        models.CartItem.user_id == current_user.id,
        models.CartItem.product_id == product_id
    ).options(selectinload(models.CartItem.product))

    result = await db.execute(query)
    cart_item = result.scalars().first()

    if not cart_item:
        raise HTTPException(status_code=404, detail="Product not found in cart.")

    if action == CartAction.increase:
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Sorry, only {cart_item.product.stock} unit(s) of this product are left in stock."
            )
    elif action == CartAction.decrease:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
        else:
            await db.delete(cart_item)

    await db.commit()
    return {"message": "Quantity updated."}


@router.delete("/remove/{product_id}", status_code=status.HTTP_200_OK)
async def remove_from_cart(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    query = select(models.CartItem).where(
        models.CartItem.user_id == current_user.id,
        models.CartItem.product_id == product_id
    )
    result = await db.execute(query)
    cart_item = result.scalars().first()

    if cart_item:
        await db.delete(cart_item)
        await db.commit()

    return {"message": "Product removed from cart."}


@router.delete("/clear", status_code=status.HTTP_200_OK)
async def clear_cart(
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    query = select(models.CartItem).where(models.CartItem.user_id == current_user.id)
    result = await db.execute(query)
    cart_items = result.scalars().all()

    for item in cart_items:
        await db.delete(item)

    await db.commit()
    return {"message": "Cart has been cleared successfully."}
