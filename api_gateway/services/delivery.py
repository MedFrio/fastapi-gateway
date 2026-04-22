from fastapi import APIRouter
from utils.http_client import forward_request

router = APIRouter()

@router.get("/delivery/assigned")
async def get_deliveries():
    return [{"order_id": "CMD1234", "livreur": "Youssef"}]

@router.post("/delivery/update")
async def update_delivery_status():
    return {"order_id": "CMD1234", "status": "livré"}
