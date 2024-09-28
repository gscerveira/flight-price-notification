from fastapi import FastAPI
from pydantic import BaseSettings

app = FastAPI()

class Settings(BaseSettings):
    app_name: str = "Fligh Price Notification Service"
    debug: bool = False
    
settings = Settings()

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.app_name}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)