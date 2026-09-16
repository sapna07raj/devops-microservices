from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "service": "Payment Service",
        "status": "running"
    }


@app.post("/payment")
def make_payment(data: dict):

    order_id = data.get("order_id")
    amount = data.get("amount")

    return {
        "order_id": order_id,
        "amount": amount,
        "payment_status": "Payment Successful"
    }