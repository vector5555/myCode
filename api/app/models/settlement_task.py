from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class SettlementTask(Base):
    __tablename__ = "settlement_tasks"

    id = Column(Integer, primary_key=True, index=True)
    settlement_id = Column(Integer, ForeignKey("settlements.id"))
    task_id = Column(Integer, ForeignKey("tasks.id"))
    amount = Column(Numeric(15, 2))
    
    # Relationships
    settlement = relationship("Settlement", back_populates="tasks")
    task = relationship("Task", back_populates="settlements")
