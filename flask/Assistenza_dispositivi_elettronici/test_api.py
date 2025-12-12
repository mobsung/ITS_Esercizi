import requests
# va installato con 'pip install requests'
import json

if __name__ == "__main__":
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }

#  ESEMPIO DI GET
    response = requests.get(
        url="http://localhost:5000/devices",
        headers=headers
    )
    print("Risposta GET:", response.json())

    payload = {
        "device_type": "smartphone",
        "id": "d3",
        "model": "Galaxy S21",
        "customer_name": "Mario Rossi",
        "purchase_year": 2021,
        "status": "received",
        "has_protective_case": True,
        "storage_gb": 128
    }

    # SENZA JSON DUMPS
    response_post = requests.post(
        url="http://localhost:5000/devices/add",  # esempio di endpoint
        json=payload,
        headers=headers
    )
    print("Risposta POST:", response_post.json())