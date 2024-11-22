from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.recipes import Recipe
from ..schemas.recipes import RecipeCreate, RecipeUpdate

def create(db: Session, request: RecipeCreate):
    new_recipe = Recipe(**request.dict())
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe

def read_all(db: Session):
    return db.query(Recipe).all()

def read_one(db: Session, recipe_id: int):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

def update(db: Session, request: RecipeUpdate, recipe_id: int):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    db_recipe.sandwich_id = request.sandwich_id
    db_recipe.resource_id = request.resource_id
    db_recipe.amount = request.amount

    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def delete(db: Session, recipe_id: int):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    db.delete(db_recipe)
    db.commit()
    return {"detail": "Recipe deleted successfully"}
