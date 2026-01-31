from fastapi import FastAPI
from db import db_check_connection

app = FastAPI(title="Autoservice Backend API")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/db-check")
def database_check():
    try:
        db_check_connection()
        return {"db_status": "ok"}
    except Exception as e:
        return {
            "db_status": "error",
            "error": str(e)
        }
    
    