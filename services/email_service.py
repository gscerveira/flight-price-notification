from aiosmtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
from config import settings

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader("templates"))

async def send_email(to_email: str, subject: str, template_name: str, context: dict):
    # Create message
    message = MIMEMultipart()
    message["From"] = settings.email_sender
    message["To"] = to_email
    message["Subject"] = subject

    # Render HTML content
    template = env.get_template(template_name)
    html_content = template.render(context)

    # Attach HTML content
    message.attach(MIMEText(html_content, "html"))

    # Send email
    async with SMTP(hostname=settings.smtp_server, port=settings.smtp_port) as smtp:
        await smtp.login(settings.smtp_username, settings.smtp_password)
        await smtp.send_message(message)

async def send_price_drop_notification(user_email: str, flight_number: str, original_price: float, new_price: float):
    subject = f"Price Drop Alert for Flight {flight_number}"
    template_name = "price_drop_notification.html"
    context = {
        "flight_number": flight_number,
        "original_price": original_price,
        "new_price": new_price,
        "savings": original_price - new_price
    }
    await send_email(user_email, subject, template_name, context)
