from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from transactions import save_transaction, get_total_transactios

app = FastAPI()

class RequestSchema(BaseModel):
    user_id: int
    amount: int
    description: str

@app.post("/transactions")
async def root(params: RequestSchema):
    total = get_total_transactios(params.user_id)
    
    if (total + params.amount) > 1000:
        return JSONResponse(status_code=status.HTTP_402_PAYMENT_REQUIRED, content=None)
    else:
        save_transaction(params)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=None)