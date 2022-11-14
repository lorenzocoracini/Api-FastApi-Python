from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

import crud
import models
import schemas
import database

models.database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/compradores/", response_model=schemas.Comprador)
async def create_comprador(comprador: schemas.CompradorCreate, db: Session = Depends(get_db)):
    db_comprador = crud.get_comprador_by_email(db=db, email=comprador.email)
    if db_comprador:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email already registered")
    return crud.create_comprador(db=db, comprador=comprador)


@app.get("/compradores/{comprador_id}", response_model=schemas.Comprador)
async def get_comprador_by_id(comprador_id: int, db: Session = Depends(get_db)):
    db_comprador = crud.get_comprador_by_id(db, comprador_id=comprador_id)
    if db_comprador is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comprador not found")
    return db_comprador


@app.get("/compradores/", response_model=list[schemas.Comprador])
async def get_compradores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    compradores = crud.get_compradores(db, skip=skip, limit=limit)
    return compradores


@app.post("/compradores/{comprador_id}/ingressos/", response_model=schemas.Ingresso)
async def create_ingresso_for_comprador(
        comprador_id: int, ingresso: schemas.IngressoCreate, db: Session = Depends(get_db)
):
    return crud.create_ingresso_for_comprador(db=db, ingresso=ingresso, comprador_id=comprador_id)


@app.get("/ingressos/", response_model=list[schemas.Ingresso])
async def get_ingressos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ingressos = crud.get_ingressos(db, skip=skip, limit=limit)
    return ingressos
