from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from services.notification_queue import QueuedNotification, enqueue_notification
import time

router = APIRouter()

class PriceDropNotification(BaseModel):
    user_email: str
    flight_number: str
    original_price: float
    new_price: float

@router.post("/notification/price-drop")
async def create_price_drop_notification(notification: PriceDropNotification, background_tasks: BackgroundTasks):
    try:
        queued_notification = QueuedNotification(**notification.dict(), timestamp=time.time())
        background_tasks.add_task(enqueue_notification, queued_notification)
        return {"status": "success", "message": "Notification queued successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))