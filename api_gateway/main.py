from fastapi import FastAPI
from services import auth, orders, kitchen, delivery

app = FastAPI(title="API Gateway - Restaurant")

app.include_router(auth.router)
app.include_router(orders.router)
app.include_router(kitchen.router)
app.include_router(delivery.router)

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API Gateway"}
