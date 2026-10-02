from sqlalchemy import create_engine
from app.core.config import DATABASE_URL

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not configured")

engine = create_engine(DATABASE_URL)