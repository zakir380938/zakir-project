from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DATABASE_URL ="mysql+pymysql://root:root@localhost:3306/new"
DATABASE_URL = "postgresql+psycopg2://db_students_f1rc_user:cVvqcq9lVVW9vwBDloardV465TxMbdQB@dpg-dbcac9l9fdbs73ccl8l0-a.oregon-postgres.render.com/db_students_f1rc"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()