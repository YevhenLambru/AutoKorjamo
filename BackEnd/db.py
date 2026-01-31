import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable not set")

engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)

def db_check_connection():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
