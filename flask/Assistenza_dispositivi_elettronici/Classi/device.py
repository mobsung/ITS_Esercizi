from abc import ABC, abstractmethod


class Device(ABC):

    @abstractmethod
    def __init__(self, id: str, model: str, customer_name: str, purchase_year: int, status: str ) -> None:
        self.id = id
        self.model = model
        self.customer_name = customer_name
        self.purchase_year = purchase_year
        self.setStatus(status)

    @abstractmethod
    def device_type(self):
        pass

    @abstractmethod
    def base_diagnosis_time(self):
        pass

    @abstractmethod
    def repair_complexity(self):
        pass

    def setStatus(self, status: str) -> None:
        self.status = status

    def info(self) -> dict:

        toDict: dict = {
            'id': self.id,
            'device_type': self.device_type(),
            'model': self.model,
            'customer_name': self.customer_name,
            'purchase_year': self.purchase_year,
            'status': self.status
        }

        return toDict
    
    def estimated_total_time(self, factor: float = 1.0) -> int:
        return int(self.base_diagnosis_time() * factor + self.repair_complexity() * 30)