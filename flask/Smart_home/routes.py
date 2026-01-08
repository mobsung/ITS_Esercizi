from flask import Flask, request, jsonify, url_for

from Classi.iotHub import IoTHub
from Classi.smartBulb import SmartBulb
from Classi.securityCamera import SecurityCamera

iotHub: IoTHub = IoTHub()

app = Flask(__name__)

def validate_json(new_device: dict):

    if ("id" not in new_device
        or "brand" not in new_device
        or "room" not in new_device
        or "installation_year" not in new_device
        or "status" not in new_device):
        return False
    
    if (new_device["type"] == "bulb" 
        and "brightness_lumens" in new_device
        and "color_capability" in new_device):
        return True
    
    elif (new_device["type"] == "camera" 
        and "resolution" in new_device
        and "night_vision" in new_device):
        return True

    else:
        return False

def create_device(new_device: dict) -> SmartBulb | SecurityCamera:
    if new_device["type"] == "bulb":
        device: SmartBulb = SmartBulb(
            serial_number=new_device[id],
            brand=new_device["brand"],
            room=new_device["room"],
            installation_year=new_device["installation_year"],
            status=new_device["status"],
            brightness_lumens=new_device["brightness_lumens"],
            color_capability=new_device["color_capability"]
        )

    elif new_device["type"] == "camera":
        device: SecurityCamera = SecurityCamera(
            serial_number=new_device[id],
            brand=new_device["brand"],
            room=new_device["room"],
            installation_year=new_device["installation_year"],
            status=new_device["status"],
            resolution=new_device["resolution"],
            night_vision=new_device["night_vision"]
        )
    return device

@app.get("/devices")
def get_devices():
    return jsonify(iotHub.list_all()), 200

@app.get("/devices/<string:serial_number>")
def get_deevice(serial_number: str):
    if iotHub.get(serial_number):
        return jsonify(iotHub.get(serial_number).info()), 200
    else:
        return jsonify({"error": "device not found"}), 404
    
@app.get("/devices/<string:serial_number>/diagnostic/<float:factor>")
def get_diagnostic_time(serial_number: str, factor: float):
    if iotHub.get(serial_number):
        device = iotHub.get(serial_number)
        d_factor: float = device.diagnostic_time(factor)
        return jsonify({
            "id": serial_number,
            "device_type": device.device_type(),
            "factor": factor,
            "diagnostic_seconds": d_factor
        }), 200
    
    else:
        return jsonify({"error": "device not found"}), 404

@app.post("/devices")
def post_device():
    new_device = request.get_json()

    if validate_json(new_device):
        device = create_device(new_device)
        iotHub.add(device)
        return jsonify(device.info()), 201
        
    else:
        return jsonify({"campi mancanti, tipo non riconosciuto"}), 400
    
@app.put("/devices/<string:serial_number>")
def put_device(serial_number: str):
    new_device = request.get_json()

    if validate_json(new_device):
        device = create_device(new_device)

        if iotHub.get(serial_number):
            iotHub.update(serial_number, device)

        else:
            iotHub.add(device)
        return jsonify(device.info()), 201
    
    else:
        return jsonify({"campi mancanti, tipo non riconosciuto"}), 400
    
@app.patch("/devices/<string:serial_number>/status")
def patch_device(serial_number: str):
    new_status = request.get_json()
    if "status" in new_status:
        if iotHub.get(serial_number):
            iotHub.patch_status(serial_number, new_status["status"])
        else:
            return jsonify({"error": "device not found"}), 404
    else:
        return jsonify({"campi mancanti, tipo non riconosciuto"}), 400






