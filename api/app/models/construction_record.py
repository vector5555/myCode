from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.db.base import Base

class ConstructionRecord(Base):
    __tablename__ = "construction_records"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    worker_id = Column(Integer, ForeignKey("users.id"))
    description = Column(String)
    photos = Column(JSON)
    quality_report = Column(String)
    
    # Relationships
    task = relationship("Task", back_populates="construction_records")
    worker = relationship("User")
