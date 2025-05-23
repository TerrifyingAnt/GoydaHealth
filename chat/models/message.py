from sqlalchemy import Column, BigInteger, String, Boolean, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from core.database import Base

class Message(Base):
    __tablename__ = "message_table"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)  # Add autoincrement=True
    from_user_id = Column(BigInteger, ForeignKey("user_table.id"), nullable=False)
    status = Column(Boolean, nullable=False)
    date = Column(DateTime, nullable=False, server_default=func.now())  # Default to current time
    media = Column(String, nullable=True)
    chat_id = Column(BigInteger, ForeignKey("chat_table.id"), nullable=False)
    text = Column(String, nullable=False)
    emotional_state = Column(Float, nullable=True)  # От -1 (очень плохое эмоциональное состояние) до 1 (очень хорошее)
    emotion = Column(String, nullable=True)  # Например: happiness, sadness, calm, anger и т.д.
    
    from_user = relationship("User", back_populates="messages")
    chat = relationship("Chat", back_populates="messages")