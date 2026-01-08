from abc import ABC, abstractmethod

class SmartDevice:

    def __init__(self,
                 serial_number: str,
                 brand: str,
                 room: str,
                 installation_year: int,
                 status: str 
                ) -> None:
        
        self.serial_number = serial_number
        self.brand = brand
        self.room = room
        self.installation_year = installation_year
        self.status = status

    @abstractmethod
    def device_type(self) -> str:
        ...

    @abstractmethod
    def energy_consumption(self) -> float | int:
        ...

    @abstractmethod
    def connection_quality(self) -> int:
        ...

    def info(self) -> dict[str, float | int | str]:
        return {
            "serial_number": self.serial_number,
            "brand": self.brand,
            "room": self.room,
            "installation_year": self.installation_year,
            "status": self.status,
        }

    def diagnostic_time(self, factor: float) -> float:
        return self.energy_consumption() * factor + self.connection_quality() * 10