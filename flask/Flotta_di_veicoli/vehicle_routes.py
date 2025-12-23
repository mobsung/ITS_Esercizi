#flask --app vehicle_routes run --debug

from flask import Flask, request, jsonify, url_for
from Classi.car import Car
from Classi.van import Van
from Classi.fleetManager import FleetManager

fleetManager: FleetManager = FleetManager()

app = Flask(__name__)


@app.route("/vehicles")
def list_vehicles():
    return jsonify(fleetManager.list_all()), 200

@app.route("/vehicles/<string:plate_id>")
def sample_vehicle(plate_id: str):
    if fleetManager.get(plate_id):
        return jsonify(fleetManager.get(plate_id).info()), 200

    else:
        return jsonify({"error": "Vehicle not found"}), 404
    
@app.route("/vehicles/<string:plate_id>/prep-time/<float:factor>")
def sample_estimate(plate_id: str, factor: float):
    if fleetManager.get(plate_id):
        vehicle = fleetManager.get(plate_id)
        resp = {
            "id": plate_id,
            "device_type": vehicle.vehicle_type(),
            "factor": factor,
            "estimated_total_minutes": vehicle.estimated_prep_time(factor)
            }
        
        return jsonify(resp)

    return {'errore': "Vehicle not found"}, 404

def validate_json(new_vehicle: dict):

    if ("id" not in new_vehicle 
        or "veichle_type" not in new_vehicle 
        or "model" not in new_vehicle 
        or "driver_name" not in new_vehicle 
        or "registration_year" not in new_vehicle 
        or "status" not in new_vehicle):
        return False
    
    if (new_vehicle["veichle_type"] == "car" 
        and "is_cabrio" in new_vehicle 
        and "doors" in new_vehicle):
        return True
    
    elif (new_vehicle["veichle_type"] == "van" 
        and "require_special_license" in new_vehicle 
        and "max_load_kg" in new_vehicle):
        return True

    else:
        return False

@app.post("/vehicles")
def add_vehicle():

    new_vehicle = request.get_json()

    if validate_json(new_vehicle):

        if new_vehicle["vehicle_type"] == "car":
            vehicle = Car(
                plate_id=new_vehicle["plate_id"],
                model=new_vehicle["model"],
                driver_name=new_vehicle["driver_name"],
                registration_year=new_vehicle["registration_year"],
                status=new_vehicle["status"],
                doors=new_vehicle["doors"],
                is_cabrio=new_vehicle["is_cabrio"]
            )
            fleetManager.add(vehicle)
            return jsonify(vehicle.info()), 200

        elif new_vehicle["vehicle_type"] == "van":
            vehicle = Van(
                plate_id=new_vehicle["plate_id"],
                model=new_vehicle["model"],
                driver_name=new_vehicle["driver_name"],
                registration_year=new_vehicle["registration_year"],
                status=new_vehicle["status"],
                max_load_kg=new_vehicle["max_load_kg"],
                require_special_license=new_vehicle["require_special_license"]
            )
            fleetManager.add(vehicle)
            return jsonify(vehicle.info()), 200
    else:
        return jsonify({"errore": "Campi mancanti, tipo non riconosciuto"}), 400
    

@app.put("/vehicles/<string:plate_id>")
def update_vehicle(plate_id: str):
    
    new_vehicle = request.get_json()

    if validate_json(new_vehicle):

        if new_vehicle["vehicle_type"] == "car":
            vehicle = Car(
                plate_id=new_vehicle["plate_id"],
                model=new_vehicle["model"],
                driver_name=new_vehicle["driver_name"],
                registration_year=new_vehicle["registration_year"],
                status=new_vehicle["status"],
                doors=new_vehicle["doors"],
                is_cabrio=new_vehicle["is_cabrio"]
            )

        elif new_vehicle["vehicle_type"] == "van":
            vehicle = Van(
                plate_id=new_vehicle["plate_id"],
                model=new_vehicle["model"],
                driver_name=new_vehicle["driver_name"],
                registration_year=new_vehicle["registration_year"],
                status=new_vehicle["status"],
                max_load_kg=new_vehicle["max_load_kg"],
                require_special_license=new_vehicle["require_special_license"]
            )

        fleetManager.update(plate_id, vehicle)
        return jsonify(vehicle.info()), 200
    
    else:
        return jsonify({"errore": "Campi mancanti, tipo non riconosciuto"}), 400
    

@app.patch("/vehicles/<string:plate_id>/status")
def patch_status(plate_id: str):
    if fleetManager.get(plate_id) == None:
        return {'errore': "Vehicle not found"}, 404
    

    new_status = request.get_json()
    if not new_status or "status" not in new_status:
        return jsonify({"errore": "Campo 'status' mancante"}), 400
    
    fleetManager.patch_status(plate_id, new_status["status"])
    return jsonify(fleetManager.get(plate_id).info()), 200
        
@app.delete("/devices/<string:plate_id>")
def delete_vehicle(plate_id: str):
    if fleetManager.delete(plate_id):
        return jsonify({"deleted": True, "id": plate_id}), 200
    
    else:
        return {'errore': "Vehicle not found"}, 404