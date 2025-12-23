from Classi.vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, plate_id: str, model: str, driver_name: str, registration_year: int, status: str, doors: int, is_cabrio: bool) -> None:
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.doors = doors
        self.is_cabrio = is_cabrio

    def vehicle_type(self) -> str:
        return "car"
    
    def base_cleaning_time(self) -> int:
        return 30
    
    def wear_level(self) -> int:
        return 2
    
    def info(self):
        base_dict: dict = super().info()

        base_dict['doors'] = self.doors
        base_dict['is_cabrio'] = self.is_cabrio

        return base_dict
    
    