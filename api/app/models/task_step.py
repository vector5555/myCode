from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class TaskStep(Base):
    __tablename__ = "task_steps"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    step_order = Column(Integer)
    name = Column(String)
    description = Column(String)
    status = Column(String)
    
    # Relationships
    task = relationship("Task", back_populates="steps")
