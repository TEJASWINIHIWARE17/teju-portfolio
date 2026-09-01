from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.mongodb import check_database_connection


app = FastAPI(
    title="Teju Hiware Portfolio API",
    description="Backend API for Teju Hiware's portfolio",
    version="1.0.0"
)


# ==============================
# CORS
# ==============================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==============================
# STARTUP
# ==============================

@app.on_event("startup")
def startup_event():
    check_database_connection()


# ==============================
# HOME
# ==============================

@app.get("/")
def home():
    return {
        "message": "Teju Hiware Portfolio API is running"
    }


# ==============================
# HEALTH CHECK
# ==============================

@app.get("/api/health")
def health_check():
    return {
        "status": "success",
        "message": "Backend is healthy"
    }