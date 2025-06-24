from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import httpx

router = APIRouter()
BASE_URL = "http://localhost:3002"

async def forward(method: str, endpoint: str, data=None):
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}{endpoint}"
        try:
            if method == "GET":
                response = await client.get(url)
            elif method == "POST":
                response = await client.post(url, json=data)
            elif method == "PATCH":
                response = await client.patch(url, json=data)
            elif method == "DELETE":
                response = await client.delete(url)
            else:
                return JSONResponse({"error": "Méthode non supportée"}, status_code=405)

            return JSONResponse(response.json(), status_code=response.status_code)
        except Exception as e:
            return JSONResponse({"error": str(e)}, status_code=500)
@router.get("/order-api/menu")
async def get_menu():
    return await forward("GET", "/menu")

@router.get("/order-api/menu/filter")
async def filter_menu_by_category(categorie: str):
    return await forward("GET", f"/menu?categorie={categorie}")
@router.get("/order-api/commandes")
async def list_commandes():
    return await forward("GET", "/commandes")

@router.get("/order-api/commandes/{commande_id}")
async def get_commande(commande_id: str):
    return await forward("GET", f"/commandes/{commande_id}")

@router.post("/order-api/commandes")
async def create_commande(request: Request):
    body = await request.json()
    return await forward("POST", "/commandes", data=body)

@router.patch("/order-api/commandes/{commande_id}/status")
async def update_commande_status(commande_id: str, request: Request):
    body = await request.json()
    return await forward("PATCH", f"/commandes/{commande_id}/status", data=body)
