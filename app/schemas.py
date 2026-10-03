from pydantic import BaseModel, EmailStr
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class ExpenseCreate(BaseModel):
    amount: float = Field(gt=0)
    category: str = Field(min_length=2, max_length=50)
    description: str | None = Field(
        default=None,
        max_length=200
    )


class ExpenseResponse(BaseModel):
    id: int
    amount: float
    category: str
    description: str | None
    date: datetime

    class Config:
        from_attributes = True