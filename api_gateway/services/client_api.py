from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import httpx

router = APIRouter()
BASE_URL = "https://clientms-akftckgbbvdph5gu.canadacentral-01.azurewebsites.net"

async def forward(method: str, endpoint: str, data=None, token=None):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}{endpoint}"
        try:
            if method == "POST":
                response = await client.post(url, json=data, headers=headers)
            elif method == "GET":
                response = await client.get(url, headers=headers)
            elif method == "DELETE":
                response = await client.delete(url, headers=headers)
            else:
                return JSONResponse({"error": "Méthode non supportée"}, status_code=405)
            return JSONResponse(response.json(), status_code=response.status_code)
        except Exception as e:
            return JSONResponse({"error": str(e)}, status_code=500)
@router.post("/client-api/login")
async def login(request: Request):
    body = await request.json()
    return await forward("POST", "/auth/login", data=body)

@router.post("/client-api/logout")
async def logout(request: Request):
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    return await forward("POST", "/auth/logout", token=token)

@router.get("/client-api/sessions")
async def sessions(request: Request):
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    return await forward("GET", "/auth/sessions", token=token)

@router.post("/client-api/logout-all")
async def logout_all(request: Request):
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    return await forward("POST", "/auth/logout-all", token=token)
@router.post("/client-api/clients")
async def create_client(request: Request):
    body = await request.json()
    return await forward("POST", "/clients", data=body)

@router.get("/client-api/clients")
async def list_clients():
    return await forward("GET", "/clients")

@router.get("/client-api/clients/{client_id}")
async def get_client(client_id: str):
    return await forward("GET", f"/clients/{client_id}")

@router.delete("/client-api/clients/{client_id}")
async def delete_client(client_id: str):
    return await forward("DELETE", f"/clients/{client_id}")
