from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime, Enum
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import os
from dotenv import load_dotenv
load_dotenv()
import enum
from datetime import datetime


DATABASE_URL = os.environ.get("PostgreSQL_DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# --- Models --- #

"""
NEW DATABASE WILL BE CREATED
LAST ONE WAS TOO MESSY AND I FORGOT WHAT I DID THINGS AND WHY I DID THOSE
"""