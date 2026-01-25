import json
import requests

# Assumiamo che l'app Flask di iotHub.py giri su questa base URL
BASE_URL = "http://127.0.0.1:5000"


def print_response(title, response):
    """Utility per stampare in modo leggibile le risposte HTTP."""
    print(f"=== {title} ===")
    print("Status code:", response.status_code)
    try:
        data = response.json()
        print("JSON response:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except ValueError:
        print("Response text:")
        print(response.text)
    print()


if __name__ == "__main__":

    headers = {
        "Content-type": "application/json",
        "Accept": "application/json"
    }

    #GET /
    r = requests.get(f"{BASE_URL}/", headers=headers)
    print_response("GET /", r)

    #GET /bookings
    r = requests.get(f"{BASE_URL}/bookings", headers=headers)
    print_response("GET /bookings", r)

    #GET /booking/<booking_id> con id non presente
    r = requests.get(f"{BASE_URL}/bookings/V123", headers=headers)
    print_response("GET /bookings/<booking_id>", r)

    #post /bookings
    new_bID = "BK-3e67"
    post_body = {
        "type": "exam",
        "booking_id": new_bID,
        "patient_name": "Giulia Verdi",
        "doctor": "Dr. Neri",
        "department": "Radiologia",
        "date": "2026-02-10",
        "time": "09:15",
        "status": "scheduled",
        "exam_type": "RMN",
        "requires_fasting": True
    }

    r = requests.post(f'{BASE_URL}/bookings', 
                      headers=headers,
                      data=json.dumps(post_body)
                    )
    print_response("POST /bookings", r)

    #put /bookings/<booking_id>
    put_body = {
        "type": "exam",
        "booking_id": new_bID,
        "patient_name": "Giulia Verdi",
        "doctor": "Dr. Neri",
        "department": "Radiologia",
        "date": "2026-02-10",
        "time": "09:15",
        "status": "confirmed",
        "exam_type": "RMN",
        "requires_fasting": False
    }

    r = requests.put(f'{BASE_URL}/bookings/{new_bID}', 
                      headers=headers,
                      data=json.dumps(put_body)
                    )
    print_response("PUT /bookings", r)

    #patch /bookings/<booking_id>
    patch_body = {"status": "completed"}
    r = requests.patch(
        f"{BASE_URL}/bookings/{new_bID}/status",
        headers=headers,
        data=json.dumps(patch_body),
    )
    print_response("PATCH /bookings/<string:booking_id>/status", r)

    #delete /bookings/<booking_id>
    r = requests.delete(f'{BASE_URL}/bookings/{new_bID}', headers=headers)
    print_response("DLETE /bookings/<string:booking_id>", r)

    #GET /bookings
    r = requests.get(f"{BASE_URL}/bookings", headers=headers)
    print_response("GET /bookings", r)