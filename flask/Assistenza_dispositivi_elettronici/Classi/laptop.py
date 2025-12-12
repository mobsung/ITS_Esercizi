from Classi.device import Device


class Laptop(Device):

    def __init__(self, id, model, customer_name, purchase_year, status, has_dedicated_gpu: bool, screen_size_inches: float) -> None:
        super().__init__(id, model, customer_name, purchase_year, status)
        self.has_dedicated_gpu = has_dedicated_gpu
        self.screen_size_inches = screen_size_inches

    def device_type(self) -> str:
        return 'laptop'
    
    def base_diagnosis_time(self) -> int:
        return 40
    
    def repair_complexity(self) -> int:
        return 5
    
    def info(self) -> dict:

        base_dict: dict = super().info()

        base_dict['has_dedicated_gpu'] = self.has_dedicated_gpu
        base_dict['screen_size_inches'] = self.screen_size_inches

        return base_dict
