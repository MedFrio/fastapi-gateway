from fastapi import FastAPI
from services import auth, orders, kitchen, delivery
from fastapi.middleware.cors import CORSMiddleware


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

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API Gateway"}
