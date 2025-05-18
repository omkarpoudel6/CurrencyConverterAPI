from fastapi import APIRouter, Query, HTTPException
from .services import get_exchange_rate

router = APIRouter()

@router.get("/convert")
async def convert(from_currency: str = Query(...), to_currency: str = Query(...), amount: float = Query(...)):
    rate = await get_exchange_rate(from_currency.upper(), to_currency.upper())
    if rate is None:
        raise HTTPException(status_code=404, detail="Currency not supported")
    return {
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "converted_amount": amount * rate,
        "rate": rate
    }
