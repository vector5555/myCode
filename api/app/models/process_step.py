from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class ProcessStep(Base):
    __tablename__ = "process_steps"

    id = Column(Integer, primary_key=True, index=True)
    process_id = Column(Integer, ForeignKey("processes.id"))
    step_order = Column(Integer)
    name = Column(String)
    description = Column(String)
    
    # Relationships
    process = relationship("Process", back_populates="steps")
