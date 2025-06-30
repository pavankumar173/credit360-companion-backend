from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.upload import router as upload_router

app = FastAPI()

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include upload route
app.include_router(upload_router)
