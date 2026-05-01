from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")

DATABASE_URL = database_url
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
