from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from utils.http_client import forward_request

router = APIRouter()

class Order(BaseModel):
    client_id: str
    items: List[str]

@router.post("/orders")
async def create_order(order: Order):
    return {
        "order_id": "CMD1234",
        "status": "reçue",
        "items": order.items
    }

@router.get("/orders")
async def get_all_orders():
    return [{"order_id": "CMD1234", "status": "en préparation"}]
