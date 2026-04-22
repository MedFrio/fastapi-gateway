from fastapi import APIRouter
from utils.http_client import forward_request

router = APIRouter()

@router.get("/kitchen/orders")
async def kitchen_orders():
    return [{"order_id": "CMD1234", "status": "en préparation"}]

@router.post("/kitchen/update")
async def update_order_status():
    return {"order_id": "CMD1234", "status": "prêt"}
