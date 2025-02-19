from sqlalchemy.orm import Session
from sqlalchemy import func
import models, schemas

def get_properties(db: Session, skip: int = 0, limit: int = 10, city: str = None):
    query = db.query(models.Property)
    if city:
        query = query.filter(func.lower(models.Property.city) == city.lower())
    return query.offset(skip).limit(limit).all()

def get_property(db: Session, property_id: int):
    return db.query(models.Property).filter(models.Property.id == property_id).first()

def create_property(db: Session, property: schemas.PropertyCreate):
    db_property = models.Property(**property.dict())
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

def update_property(db: Session, property_id: int, updates: schemas.PropertyUpdate):
    db_property = get_property(db, property_id)
    if not db_property:
        return None
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(db_property, key, value)
    db.commit()
    db.refresh(db_property)
    return db_property

def delete_property(db: Session, property_id: int):
    db_property = get_property(db, property_id)
    if db_property:
        db.delete(db_property)
        db.commit()
        return True
    return False
