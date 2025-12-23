from flask import Flask, jsonify, request, url_for

from Classi.device import Device
from Classi.smartphone import Smartphone
from Classi.laptop import Laptop
from Classi.serviceCenter import ServiceCenter


#flask --app centro_assistenza_routes run --debug

serviceCenter: ServiceCenter = ServiceCenter()

app = Flask(__name__)


def validate_json(new_device: dict):

    if ("id" not in new_device 
        or "device_type" not in new_device 
        or "model" not in new_device 
        or "customer_name" not in new_device 
        or "purchase_year" not in new_device 
        or "status" not in new_device):
        return False
    
    if (new_device["device_type"] == "smartphone" 
        and "has_protective_case" in new_device 
        and "storage_gb" in new_device):
        return True
    
    elif (new_device["device_type"] == "laptop" 
        and "has_dedicated_gpu" in new_device 
        and "screen_size_inches" in new_device):
        return True

    else:
        return False


@app.route('/')
def home():
    home_out = {
        'message': "Welcome to Service Center API",
        'links': {
            'list_devices': url_for("list_devices"),
            'sample_device': url_for("sample_device", device_id="1"),
            'sample_estimate': url_for('sample_estimate', device_id="1", factor=1.5),
        }
    }

    return jsonify(home_out)

@app.route("/devices")
def list_devices():
    return jsonify(serviceCenter.list_all())

@app.route("/devices/<string:device_id>")
def sample_device(device_id):
    if device_id in serviceCenter.devices:
        device = serviceCenter.get(device_id).info()
        return jsonify(device)

    else:
        return {'errore': "Device not found"}, 404

@app.route("/devices/<string:device_id>/estimate/<float:factor>")
def sample_estimate(device_id: str, factor: float):
    if device_id in serviceCenter.devices:
        device = serviceCenter.get(device_id)
        sample = {
            "id": device_id,
            "device_type": device.device_type(),
            "factor": factor,
            "estimated_total_minutes": device.estimated_total_time(factor)
            }
        
        return jsonify(sample)

    return {'errore': "Device not found"}, 404


@app.post("/devices/add")
def add_device():
    new_device = request.get_json()

    if validate_json(new_device):

        if new_device["device_type"] == "smartphone":
            device = Smartphone(
                id=new_device["id"],
                model=new_device["model"],
                customer_name=new_device["customer_name"],
                purchase_year=new_device["purchase_year"],
                status=new_device["status"],
                has_protective_case=new_device["has_protective_case"],
                storage_gb=new_device["storage_gb"]
            )
            serviceCenter.add(device)
            return jsonify(device.info()), 201
    
        elif new_device["device_type"] == "laptop":
            device = Laptop(
                id=new_device["id"],
                model=new_device["model"],
                customer_name=new_device["customer_name"],
                purchase_year=new_device["purchase_year"],
                status=new_device["status"],
                has_dedicated_gpu=new_device["has_dedicated_gpu"],
                screen_size_inches=new_device["screen_size_inches"]
            )
            serviceCenter.add(device)
            return jsonify(device.info()), 201

    else:
        return jsonify({"errore": "Campi mancanti, tipo non riconosciuto"}), 400

app.put("/devices/<string:device_id>")
def update_device(device_id: str):
    new_device = request.get_json()

    if validate_json(new_device):
        
        if new_device["device_type"] == "smartphone":
            device = Smartphone(
                id=new_device["id"],
                model=new_device["model"],
                customer_name=new_device["customer_name"],
                purchase_year=new_device["purchase_year"],
                status=new_device["status"],
                has_protective_case=new_device["has_protective_case"],
                storage_gb=new_device["storage_gb"]
            )
    
        elif new_device["device_type"] == "laptop":
            device = Laptop(
                id=new_device["id"],
                model=new_device["model"],
                customer_name=new_device["customer_name"],
                purchase_year=new_device["purchase_year"],
                status=new_device["status"],
                has_dedicated_gpu=new_device["has_dedicated_gpu"],
                screen_size_inches=new_device["screen_size_inches"]
            )

        if device_id in serviceCenter:
            serviceCenter.update(device_id=device_id, new_device=device)
            return jsonify(device.info()), 201
        
        else:
            serviceCenter.add(device=device)
            return jsonify(device.info()), 201
    else:
        return jsonify({"errore": "Campi mancanti, tipo non riconosciuto"}), 400
    

@app.patch("/devices/<string:device_id>/status")
def update_status(device_id: str):
    if serviceCenter.get(device_id) == None:
        return jsonify({"errore": "Il dispositivo non esiste"}), 404

    new_status = request.get_json()
    if not new_status or "status" not in new_status:
        return jsonify({"errore": "Campo 'status' mancante"}), 400

    serviceCenter.patch_status(device_id, new_status["status"])
    return jsonify(serviceCenter.get(device_id).info()), 200


@app.delete("/devices/<string:device_id>")
def delete_device(device_id: str):
    if serviceCenter.delete(device_id):
        return jsonify({"deleted": True, "id": device_id}), 200
    else:
        return jsonify({"errore": "Il dispositivo non esiste"}), 404
    


