from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import aiofiles
import uuid

from app import models, schemas
from app.core.database import get_db

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/", response_model=schemas.ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(product: schemas.ProductCreate, db: AsyncSession = Depends(get_db)):
    """Adds a new product to the system."""
    query = select(models.Product).where(models.Product.title == product.title)
    result = await db.execute(query)
    existing_product = result.scalars().first()

    if existing_product:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A product with this name already exists in the catalog!"
        )

    new_product = models.Product(**product.model_dump())

    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)

    return new_product


@router.post("/upload-image")
async def upload_product_image(file: UploadFile = File(...)):
    """Uploads a new product image to the system and returns its URL."""
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload a valid image file.")

    file_extension = file.filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4()}.{file_extension}"
    file_path = f"static/images/{unique_filename}"

    # Fixed: use aiofiles for non-blocking async file write
    content = await file.read()
    async with aiofiles.open(file_path, "wb") as buffer:
        await buffer.write(content)

    return {"image_url": f"/{file_path}"}


@router.get("/", response_model=list[schemas.ProductResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    """Lists all products in the system."""
    query = select(models.Product)
    result = await db.execute(query)
    products = result.scalars().all()

    return products
