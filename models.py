from database import Base 
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Float;




class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    on_offer = Column(Boolean, default=False)
    
    def __ref__(self):
        return f"<Item name={self.name} price= {self.price}>"