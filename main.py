from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from auth import authenticate_user, create_access_token, get_current_user
from datetime import timedelta
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    print(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = create_access_token(data={"username": user["username"]}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/properties", response_model=schemas.PropertyResponse)
def create_property(property: schemas.PropertyCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return crud.create_property(db, property)

@app.get("/properties", response_model=list[schemas.PropertyResponse])
def list_properties(skip: int = 0, limit: int = 10, city: str = None, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return crud.get_properties(db, skip, limit, city)

@app.get("/properties/{property_id}", response_model=schemas.PropertyResponse)
def get_property(property_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    property = crud.get_property(db, property_id)
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    return property

@app.patch("/properties/{property_id}", response_model=schemas.PropertyResponse)
def update_property(property_id: int, updates: schemas.PropertyUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    updated_property = crud.update_property(db, property_id, updates)
    if not updated_property:
        raise HTTPException(status_code=404, detail="Property not found")
    return updated_property

@app.delete("/properties/{property_id}")
def delete_property(property_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    if not crud.delete_property(db, property_id):
        raise HTTPException(status_code=404, detail="Property not found")
    return {"message": "Property deleted successfully"}
