from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime
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

class MessageType(enum.Enum):
    dm = "dm"
    comment = "comment"

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=True)

    messages = relationship("Message", back_populates="client")

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(String)
    features = Column(Text)

    posts = relationship("Post", back_populates="listing")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    listing_id = Column(Integer, ForeignKey("listings.id"))
    post_url = Column(String, unique=True)

    listing = relationship("Listing", back_populates="posts")
    messages = relationship("Message", back_populates="post")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    message_text = Column(Text, nullable=False)
    response_text = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    #message_type = Column(, nullable=False) 
    response_sent = Column(Boolean, default=False)

    client = relationship("Client", back_populates="messages")
    post = relationship("Post", back_populates="messages")

