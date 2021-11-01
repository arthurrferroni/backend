from sqlalchemy import Column, Integer, String 
from database import Base

# end import 

# movie name model

class Filme(Base):
    __tablename__ = 'filme' 
    
    id = Column('id', Integer, primary_key=True, index=True)
    titulo = Column('titulo', String(50))
    ano = Column('ano', Integer)
    duracao = Column('duracao', Integer)
    
# end movie name model
