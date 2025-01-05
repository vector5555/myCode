from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from .process_step import ProcessStep

class Process(Base):
    __tablename__ = "processes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    
    # Relationships
    steps = relationship("ProcessStep", back_populates="process")
    tasks = relationship("Task", back_populates="process")
