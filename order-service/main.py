from fastapi import FastAPI
import requests

app = FastAPI()

PAYMENT_SERVICE_URL = "http://payment-container:5001"

@app.get("/")
def home():
    return {
        "service": "Order Service",
        "status": "running"
    }


@app.post("/order/{order_id}")
def create_order(order_id: int):

    payment_data = {
        "order_id": order_id,
        "amount": 500
    }

    response = requests.post(
        f"{PAYMENT_SERVICE_URL}/payment",
        json=payment_data
    )

    return {
        "order_id": order_id,
        "message": "Order created",
        "payment_response": response.json()
    }