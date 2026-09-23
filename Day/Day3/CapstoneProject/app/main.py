# This file is the entry point of the application
from fastapi import FastAPI
from app.config import settings
from app.database import ping_database
from app.routers import users

# Creates a FastAPI instance with the app name from the settings
app = FastAPI(title=settings.APP_NAME)
app.include_router(users.router)  # Includes the users router for handling user-related endpoints
# This function runs once when the server starts up. It checks if the MongoDB connection is alive and raises an error if not.
@app.on_event("startup")
def startup() -> None:
    if not ping_database():
        raise RuntimeError("Could not connect to MongoDB")
    print(f"[startup] Connected to MongoDB. App: {settings.APP_NAME}")

# Checks basic health-check API endpoint & confirms GET / is running & reachable. (/ is conssidered as 'root')
@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "app": settings.APP_NAME}