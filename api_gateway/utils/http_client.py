import httpx

async def forward_request(method: str, url: str, data=None):
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            if method == "GET":
                response = await client.get(url)
            elif method == "POST":
                response = await client.post(url, json=data)
            else:
                return {"error": f"Unsupported method {method}"}
            response.raise_for_status()
            return response.json()
    except httpx.RequestError:
        return {"error": f"Service '{url}' indisponible"}
    except httpx.HTTPStatusError as e:
        return {"error": f"Erreur HTTP depuis {url}: {e.response.status_code}"}
