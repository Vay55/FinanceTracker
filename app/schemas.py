#defines what data types allowed

from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    amount: float
    category: str
    description: str