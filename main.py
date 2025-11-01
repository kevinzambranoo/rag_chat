from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import rag_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rag_router.router)

@app.get("/")
async def root():
    return {"message": "API funcionando correctamente kevin zambrano"}