from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Flight Price Notification Service"
    debug: bool = False
    email_sender: str = "trpcldprsn@gmail.com"
    smtp_server: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_username: str = "trpcldprsn@gmail.com"
    smtp_password: str = "hpjj rfht dbqx dkzv"
    
settings = Settings()