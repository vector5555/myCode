from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    real_name = Column(String)
    phone = Column(String)
    email = Column(String)
    status = Column(String, default="active")
    
    # Relationships
    roles = relationship("UserRole", back_populates="user")
    projects = relationship("Project", back_populates="manager")
    tasks = relationship("Task", back_populates="worker")
    construction_records = relationship("ConstructionRecord", back_populates="worker")
    settlements = relationship("Settlement", back_populates="worker")
