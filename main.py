from config import settings
from fastapi import FastAPI
from routers import health, notifications
from services.notification_queue import process_notifications
import asyncio

app = FastAPI()

app.include_router(health.router)
app.include_router(notifications.router)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(process_notifications())

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.app_name}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=settings.debug)