from fastapi import FastAPI

from .database import Base, engine
from routes.auth import router as auth_router
from routes.expenses import router as expense_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SpendWise API",
    description="Personal Expense Management REST API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(expense_router)


@app.get("/")
def root():
    return {
        "message": "SpendWise API is running"
    }