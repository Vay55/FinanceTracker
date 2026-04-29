#entry point
from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from app import models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "http://[::]:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "FinanceFlow API running"}