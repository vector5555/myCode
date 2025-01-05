from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from .task_step import TaskStep

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    process_id = Column(Integer, ForeignKey("processes.id"))
    name = Column(String)
    description = Column(String)
    worker_id = Column(Integer, ForeignKey("users.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String, default="pending")
    
    # Relationships
    project = relationship("Project", back_populates="tasks")
    process = relationship("Process")
    worker = relationship("User", back_populates="tasks")
    steps = relationship("TaskStep", back_populates="task")
    construction_records = relationship("ConstructionRecord", back_populates="task")
    settlements = relationship("SettlementTask", back_populates="task")
