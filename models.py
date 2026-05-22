from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(120), nullable=False, unique=True)
    full_name = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>" 
