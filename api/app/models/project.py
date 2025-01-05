from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    manager_id = Column(Integer, ForeignKey("users.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String, default="pending")
    
    # Relationships
    manager = relationship("User", back_populates="projects")
    tasks = relationship("Task", back_populates="project")
    contracts = relationship("Contract", back_populates="project")
    settlements = relationship("Settlement", back_populates="project")
    reviews = relationship("ProjectReview", back_populates="project")
