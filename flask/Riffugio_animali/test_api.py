import requests
# va installato con 'pip install requests'
import json

if __name__ == "__main__":
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }

    # ESEMPIO DI GET
    # response = requests.get(
    #     url="http://localhost:5000/Animals",
    #     headers=headers
    # )
    # print("Risposta GET:", response.json())

    # response = requests.get(
    #     url="http://localhost:5000/Animals/2",
    #     headers=headers
    # )
    # print("Risposta GET:", response.json())

    # ESEMPIO DI POST
    # payload = {
    #     "type": "dog",
    #     "id": "0",
    #     "name": "Baldur",
    #     "age_years": 3,
    #     "weight_kg": 2.3,
    #     "breed": "cane piccolo",
    #     "is_trained": True
    # }

    # SENZA JSON DUMPS
    # response_post = requests.post(
    #     url="http://localhost:5000/Animals/add",  # esempio di endpoint
    #     json=payload,
    #     headers=headers
    # )
    # print("Risposta POST:", response_post.json())

    # response = requests.get(
    #     url="http://localhost:5000/Animals",
    #     headers=headers
    # )
    # print("Risposta GET:", response.json())

    payload = {
        "adopter_name": "Real Chat"
    }

    response_post = requests.post(
        url="http://localhost:5000/Animals/1/adopt",  # esempio di endpoint
        json=payload,
        headers=headers
    )
    print("Risposta POST:", response_post.json())


    response = requests.get(
        url="http://localhost:5000/Animals",
        headers=headers
    )
    print("Risposta GET:", response.json())