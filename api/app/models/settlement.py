from sqlalchemy import Column, Integer, Numeric, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Settlement(Base):
    __tablename__ = "settlements"

    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    total_amount = Column(Numeric(15, 2))
    status = Column(String, default="pending")
    
    # Relationships
    worker = relationship("User", back_populates="settlements")
    tasks = relationship("SettlementTask", back_populates="settlement")
    project = relationship("Project")
