from fastapi import FastAPI
from app.routers.tables.router import router as router_tables
from app.routers.reservations.router import router as router_reservations
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_tables)
app.include_router(router_reservations)


@app.get("/")
async def hello():
    return {"message": "Hello"}
