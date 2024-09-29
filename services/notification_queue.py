from asyncio import Queue
from pydantic import BaseModel
from typing import List, Dict
import time
from services.email_service import send_price_drop_notification

class QueuedNotification(BaseModel):
    user_email: str
    flight_number: str
    original_price: float
    new_price: float
    timestamp: float

notification_queue: Queue = Queue()
rate_limit_store: Dict[str, List[float]] = {}

async def enqueue_notification(notification: QueuedNotification):
    await notification_queue.put(notification)

async def process_notifications():
    while True:
        notification = await notification_queue.get()
        if await check_rate_limit(notification.user_email):
            await send_notification(notification)
        notification_queue.task_done()

async def check_rate_limit(user_email: str, limit: int = 5, window: int = 3600) -> bool:
    current_time = time.time()
    if user_email not in rate_limit_store:
        rate_limit_store[user_email] = []
    
    rate_limit_store[user_email] = [t for t in rate_limit_store[user_email] if current_time - t < window]
    
    if len(rate_limit_store[user_email]) < limit:
        rate_limit_store[user_email].append(current_time)
        return True
    return False

async def send_notification(notification: QueuedNotification):
    await send_price_drop_notification(
        notification.user_email,
        notification.flight_number,
        notification.original_price,
        notification.new_price
    )


