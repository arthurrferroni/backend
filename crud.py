from sqlalchemy.orm import Session
import models, schemas

# end import

#add movie

def cria_filme(db: Session, filme: schemas.Filme):
    db_filme = models.Filme(**filme.dict())
    db.add(db_filme)
    db.commit()
    db.refresh(db_filme)
    return db_filme

#end add movie

#get movie by id

def get_filme_by_id(db: Session, filme_id: int):
    return db.query(models.Filme).filter(models.Filme.id == filme_id).first() 

# end get movie by id

# get all movies

def get_filmes(db: Session):
    return db.query(models.Filme).all()

# end get all movies