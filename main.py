from fastapi import FastAPI
import enum
from sqlalchemy import create_engine

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Double, Numeric, Enum
from sqlalchemy.orm import sessionmaker, declarative_base

from sqladmin import Admin, ModelView

# connection db
SQLALCHEMY_DATABASE_URL = "sqlite:///app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# open data
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


app = FastAPI()
admin = Admin(app, engine)

#
