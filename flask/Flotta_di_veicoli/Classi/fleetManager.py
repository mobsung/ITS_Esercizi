from Classi.vehicle import Vehicle

class FleetManager():

    def __init__(self):
        self.vehicles: dict[str, Vehicle] = {}

    def add(self, vehicle: Vehicle) -> bool:
        if vehicle.plate_id not in self.vehicles:
            self.vehicles[vehicle.plate_id] = vehicle
            return True
        return False
    
    def get(self, plate_id: str) -> Vehicle | None:
        return self.vehicles.get(plate_id)
    
    def update(self, plate_id: str, new_vehicle: Vehicle) -> None:
        if self.get(plate_id):
            self.vehicles[new_vehicle.plate_id] = new_vehicle
            self.vehicles.pop(plate_id)

    def patch_status(self, plate_id: str, new_status: str) -> None:
        if self.vehicles.get(plate_id):
            self.vehicles[plate_id].status = new_status

    def delete(self, plate_id: str) -> bool:
        if self.vehicles.get(plate_id):
            self.vehicles.pop(plate_id)
            return True
        return False
    
    def list_all(self) -> list[dict]:
        return [v.info() for v in self.vehicles.values()]
