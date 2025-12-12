
from Classi.device import Device


class Smartphone(Device):

    def __init__(self, id, model, customer_name, purchase_year, status, has_protective_case: bool, storage_gb: int):
        super().__init__(id, model, customer_name, purchase_year, status)
        self.has_protective_case = has_protective_case
        self.storage_gb = storage_gb
        

    
    def device_type(self) -> str:
        return 'smartphone'
    
    def base_diagnosis_time(self) -> int:
        return 20
    
    def repair_complexity(self) -> int:
        return 3
    
    def info(self) -> dict:

        base_dict: dict = super().info()

        base_dict['has_protective_case'] = self.has_protective_case
        base_dict['storage_gb'] = self.storage_gb

        return base_dict

    