from fastapi import FastAPI
from services import auth, orders, kitchen, delivery
from fastapi.middleware.cors import CORSMiddleware

from services import client_api  # ajouter en haut
from services import order_api  # ajout en haut




app = FastAPI(title="API Gateway - Restaurant")

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(orders.router)
app.include_router(kitchen.router)
app.include_router(delivery.router)
app.include_router(client_api.router)  # ajouter en bas
app.include_router(order_api.router)  # ajout en bas



@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API Gateway"}
