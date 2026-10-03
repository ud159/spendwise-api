from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Expense
from app.schemas import ExpenseCreate, ExpenseResponse
from app.auth1 import get_current_user


router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)


@router.post(
    "/",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED
)
def create_expense(
    expense_data: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    expense = Expense(
        amount=expense_data.amount,
        category=expense_data.category,
        description=expense_data.description,
        user_id=current_user.id
    )

    db.add(expense)
    db.commit()
    db.refresh(expense)

    return expense


@router.get(
    "/",
    response_model=list[ExpenseResponse],
    status_code=status.HTTP_200_OK
)
def get_expenses(
    category: str | None = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if page < 1:
        page = 1

    if limit < 1 or limit > 100:
        limit = 10

    query = db.query(Expense).filter(
        Expense.user_id == current_user.id
    )

    if category:
        query = query.filter(
            Expense.category == category
        )

    offset = (page - 1) * limit

    return (
        query
        .order_by(Expense.date.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )


@router.get(
    "/summary",
    status_code=status.HTTP_200_OK
)
def expense_summary(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    expenses = db.query(Expense).filter(
        Expense.user_id == current_user.id
    ).all()

    total = sum(
        expense.amount
        for expense in expenses
    )

    categories = {}

    for expense in expenses:
        categories[expense.category] = (
            categories.get(expense.category, 0)
            + expense.amount
        )

    return {
        "total_spending": total,
        "expense_count": len(expenses),
        "by_category": categories
    }


@router.get(
    "/{expense_id}",
    response_model=ExpenseResponse,
    status_code=status.HTTP_200_OK
)
def get_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    expense = db.query(Expense).filter(
        Expense.id == expense_id,
        Expense.user_id == current_user.id
    ).first()

    if not expense:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found"
        )

    return expense


@router.put(
    "/{expense_id}",
    response_model=ExpenseResponse,
    status_code=status.HTTP_200_OK
)
def update_expense(
    expense_id: int,
    expense_data: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    expense = db.query(Expense).filter(
        Expense.id == expense_id,
        Expense.user_id == current_user.id
    ).first()

    if not expense:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found"
        )

    expense.amount = expense_data.amount
    expense.category = expense_data.category
    expense.description = expense_data.description

    db.commit()
    db.refresh(expense)

    return expense


@router.delete(
    "/{expense_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    expense = db.query(Expense).filter(
        Expense.id == expense_id,
        Expense.user_id == current_user.id
    ).first()

    if not expense:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found"
        )

    db.delete(expense)
    db.commit()

    return None