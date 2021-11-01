from fastapi import FastAPI
from fastapi import Depends, HTTPException, status
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import crud, models, schemas

#end import


#db instance
models.Base.metadata.create_all(bind = engine)
app = FastAPI()

def get_db():     
    db = SessionLocal()     
    try:         
        yield db     
    finally:
        db.close()
        

#add movie

@app.post("/filmes", response_model = schemas.Filme) 

def cadastra_filme(filme: schemas.Filme, db: Session = Depends(get_db)):
    
    db_filme = crud.get_filme_by_id(db, filme.id) 

    if db_filme:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, 
            detail = "Esse filme já foi cadastrado"
            )
    return crud.cria_filme(db=db, filme = filme)

# end add movie



#movie find by id

@app.get("/filmes/{filme_id}", response_model = schemas.Filme)

def retorna_filme(filme_id: int, db: Session = Depends(get_db)):
    
    db_filme = crud.get_filme_by_id(db, filme_id)
    
    if db_filme is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Nenhum filme encontrado"
            )
    return db_filme 

#end movie find by id


#all movies return

@app.get('/filmes', response_model = schemas.lista)

def retorna_todos_filmes(db: Session = Depends(get_db)):
    
    db_filmes = crud.get_filmes(db) #retorna db de Filme
    
    lista_filmes = []
    for filme in db_filmes:
        lista_filmes.append(filme) #add filmes do bd em uma lista vazia
    return lista_filmes     

#end all movies return