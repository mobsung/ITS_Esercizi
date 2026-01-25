from abc import ABC, abstractmethod

class Booking(ABC):

    def __init__(self,
                booking_id: str,
                patient_name: str,
                doctor: str,
                department: str,
                date: str,
                time: str,
                status: str
                ) -> None:
        self.booking_id = booking_id
        self.patient_name = patient_name
        self.doctor = doctor
        self.department = department
        self.date = date
        self.time = time
        self.status = status

    @abstractmethod
    def booking_type(self) -> str:
        ...

    @abstractmethod
    def base_duration(self) -> int:
        ...

    @abstractmethod
    def priority_level(self) -> int:
        ...

    def info(self) -> dict[str, int | str | bool | float]:
        return {
            "booking_id": self.booking_id,
            "patient_name": self.patient_name,
            "doctor": self.doctor,
            "department": self.department,
            "date": self.date,
            "time": self.time,
            "status": self.status
        }
    
    def estimated_wait(self, factor: float = 1.0) -> int:
        return int(self.base_duration() * factor + self.priority_level() * 5)
    
