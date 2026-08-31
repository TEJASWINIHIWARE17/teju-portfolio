from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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