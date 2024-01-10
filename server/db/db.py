import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import *
import sys
sys.path.append("update-chat-server/server")


load_dotenv("db/.env")
DB_URL = os.environ.get("DB_URL")
FAKE_DB_URL = os.environ.get("FAKE_DB_URL")

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

fake_engine = create_engine(FAKE_DB_URL)
FakeSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=fake_engine)

