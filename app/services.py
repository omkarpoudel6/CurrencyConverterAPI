import httpx
from .config import settings

async def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    url = f"{settings.api_base_url}/fetch-one?from={from_currency}&to={to_currency}&api_key={settings.api_key}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        exchange_rate = float(next(iter(data['result'].values())))
        return exchange_rate
