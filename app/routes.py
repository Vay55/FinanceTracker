from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Expense
from app.schemas import ExpenseCreate

router = APIRouter()

# CREATE
@router.post("/expenses")
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = Expense(**expense.dict())
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


# READ ALL
@router.get("/expenses")
def get_expenses(db: Session = Depends(get_db)):
    return db.query(Expense).all()


# READ ONE
@router.get("/expenses/{expense_id}")
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

# UPDATE
@router.put("/expenses/{expense_id}")
def update_expense(expense_id: int, updated_data: ExpenseCreate, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    expense.amount = updated_data.amount
    expense.category = updated_data.category
    expense.description = updated_data.description

    db.commit()
    db.refresh(expense)

    return expense


# DELETE
@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(expense)
    db.commit()
    return {"message": "Expense deleted"}