# Flight Price Notification Service

A FastAPI-based service for notifying users about flight price drops.

## Project Description

This service allows users to receive notifications when the price of a flight they're interested in drops. It uses FastAPI for the API, asyncio for handling asynchronous operations, and integrates with an email service for sending notifications.

## Installation and Setup

### Prerequisites

- Python 3.12 or higher
- Docker (optional, for containerized deployment)

### Local Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flight-price-notification
   ```

2. Create a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add the following variables:
   ```
   APP_NAME="Flight Price Notification Service"
   DEBUG=False
   EMAIL_SENDER=your_email@example.com
   SMTP_SERVER=smtp.example.com
   SMTP_PORT=587
   SMTP_USERNAME=your_username
   SMTP_PASSWORD=your_password
   ```

5. Run the application:
   ```
   uvicorn main:app --reload
   ```

### Docker Setup

1. Build the Docker image:
   ```
   docker build -t flight-price-notification .
   ```

2. Run the container:
   ```
   docker run -p 8000:8000 flight-price-notification
   ```

## Usage

The service exposes the following endpoints:

- `GET /`: Welcome message
- `GET /health`: Health check endpoint
- `POST /notification/price-drop`: Endpoint to create a price drop notification