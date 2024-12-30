from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .models import Blog as BlogModel
from .schemas import BlogResponse, Blog as BlogSchema
from ...database import get_db

router = APIRouter()


@router.get("/blog", status_code=status.HTTP_200_OK, response_model=List[BlogResponse], tags=["blogs"])
def get_all(db: Session = Depends(get_db)):
    blogs = db.query(BlogModel).all()
    return blogs

@router.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=BlogResponse, tags=["blogs"])
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    return blog


@router.post("/blog", status_code=status.HTTP_201_CREATED, tags=["blogs"])
def create(request: BlogSchema, db: Session = Depends(get_db)):
    new_blog = BlogModel(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
def update_blog(id: int, request: BlogSchema, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    blog.update(request.model_dump())
    db.commit()
    return {"data": {"message": "Blog updated successfully"}}


@router.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return {"data": {"message": "Blog deleted successfully"}}