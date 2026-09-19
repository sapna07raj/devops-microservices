import httpx


def test_order_service():
    response = httpx.get("http://localhost:8000/")
    
    assert response.status_code == 200
    assert response.json()["service"] == "Order Service"
    assert response.json()["status"] == "running"


def test_payment_service():
    response = httpx.get("http://localhost:5001/")
    
    assert response.status_code == 200
    assert response.json()["service"] == "Payment Service"
    assert response.json()["status"] == "running"


def test_order_payment_communication():
    response = httpx.post(
        "http://localhost:8000/order/101"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["order_id"] == 101
    assert data["message"] == "Order created"
    assert data["payment_response"]["payment_status"] == "Payment Successful"