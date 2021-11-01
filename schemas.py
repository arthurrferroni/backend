from pydantic import BaseModel

# end import

# schema of "filme" class
class Filme(BaseModel):
    id: int
    titulo: str
    ano: int
    duracao: int

    class Config:         
        orm_mode = True

lista = [] 

# end schema of "filme" class