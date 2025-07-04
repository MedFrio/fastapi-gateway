from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import httpx

router = APIRouter()
BASE_URL = "http://localhost:3003"  #  microservice livreur sur le port 3003

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


# ========= ROUTES LIVREURS ===========
@router.get("/delivery-api/livreurs")
async def list_livreurs():
    return await forward("GET", "/livreurs")

@router.post("/delivery-api/livreurs")
async def create_livreur(request: Request):
    body = await request.json()
    return await forward("POST", "/livreurs", data=body)

@router.get("/delivery-api/livreurs/{livreur_id}")
async def get_livreur(livreur_id: str):
    return await forward("GET", f"/livreurs/{livreur_id}")

@router.patch("/delivery-api/livreurs/{livreur_id}")
async def update_livreur(livreur_id: str, request: Request):
    body = await request.json()
    return await forward("PATCH", f"/livreurs/{livreur_id}", data=body)

@router.delete("/delivery-api/livreurs/{livreur_id}")
async def delete_livreur(livreur_id: str):
    return await forward("DELETE", f"/livreurs/{livreur_id}")


# ========= ROUTES LIVRAISONS ===========
@router.get("/delivery-api/livraisons")
async def list_livraisons():
    return await forward("GET", "/livraisons")

@router.get("/delivery-api/livraisons/{livraison_id}")
async def get_livraison(livraison_id: str):
    return await forward("GET", f"/livraisons/{livraison_id}")

@router.post("/delivery-api/livraisons")
async def create_livraison(request: Request):
    body = await request.json()
    return await forward("POST", "/livraisons", data=body)

@router.patch("/delivery-api/livraisons/{livraison_id}")
async def update_livraison(livraison_id: str, request: Request):
    body = await request.json()
    return await forward("PATCH", f"/livraisons/{livraison_id}", data=body)

@router.post("/delivery-api/livraisons/{livraison_id}/assigner")
async def assigner_livraison(livraison_id: str, request: Request):
    body = await request.json()
    return await forward("POST", f"/livraisons/{livraison_id}/assigner", data=body)
