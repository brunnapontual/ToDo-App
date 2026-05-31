from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Task

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def index(request: Request, db: Session = Depends(get_db)):
    tasks = db.query(Task).order_by(Task.created_at.desc()).all()
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})


@router.post("/tasks")
def create_task(title: str = Form(...), db: Session = Depends(get_db)):
    task = Task(title=title.strip())
    db.add(task)
    db.commit()
    return RedirectResponse("/", status_code=303)


@router.post("/tasks/{task_id}/toggle")
def toggle_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.done = not task.done
        db.commit()
    return RedirectResponse("/", status_code=303)


@router.post("/tasks/{task_id}/delete")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return RedirectResponse("/", status_code=303)
