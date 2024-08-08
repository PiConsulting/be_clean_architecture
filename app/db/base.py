from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'sqlite:///example.db'
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
