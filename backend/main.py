from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.mongodb import (
    check_database_connection,
    contacts_collection
)


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


# ==============================
# CONTACT
# ==============================

@app.post("/api/contact")
def create_contact(
    name: str,
    email: str,
    subject: str,
    message: str
):

    contact_data = {
        "name": name,
        "email": email,
        "subject": subject,
        "message": message
    }

    result = contacts_collection.insert_one(contact_data)

    return {
        "status": "success",
        "message": "Contact message saved successfully",
        "id": str(result.inserted_id)
    }