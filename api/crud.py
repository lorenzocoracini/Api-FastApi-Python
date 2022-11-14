from sqlalchemy.orm import Session

import models
import schemas


def get_comprador_by_id(db: Session, comprador_id: int):
    return db.query(models.Comprador).filter(models.Comprador.id == comprador_id).first()


def create_comprador(db: Session, comprador: schemas.CompradorCreate):
    fake_hashed_password = comprador.password + "notreallyhashed"
    db_comprador = models.Comprador(email=comprador.email, hashed_password=fake_hashed_password)
    db.add(db_comprador)
    db.commit()
    db.refresh(db_comprador)
    return db_comprador


def get_comprador_by_email(db: Session, email: str):
    return db.query(models.Comprador).filter(models.Comprador.email == email).first()


def get_compradores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Comprador).offset(skip).limit(limit).all()


def get_ingressos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ingresso).offset(skip).limit(limit).all()


def create_ingresso_for_comprador(db: Session, ingresso: schemas.IngressoCreate, comprador_id: int):
    db_ingresso = models.Ingresso(**ingresso.dict(), owner_id=comprador_id)
    db.add(db_ingresso)
    db.commit()
    db.refresh(db_ingresso)
    return db_ingresso

