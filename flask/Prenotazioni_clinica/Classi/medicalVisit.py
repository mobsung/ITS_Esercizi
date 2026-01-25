from Classi.booking import Booking

class MedicalVisit(Booking):
    def __init__(self, booking_id: str,
                patient_name: str, 
                doctor: str, 
                department: str, 
                date: str, 
                time: str, 
                status: str, 
                visit_reason: str, 
                first_time: bool) -> None:
        super().__init__(booking_id, patient_name, doctor, department, date, time, status)
        self.visit_reason = visit_reason
        self.first_time = first_time
    
    def booking_type(self) -> str:
        return "visit"

    def base_duration(self) -> int:
        return 30

    def priority_level(self) -> int:
        # Semplice euristica: se motivo contiene parole "urgenti" alza priorità
        reason = (self.visit_reason or "").lower()
        keywords = ["urgente", "dolore", "acuto", "svenimento"]
        for k in keywords:
            if k in reason:
                return 7
        return 5
    
    def info(self) -> dict[str, int | str | bool | float]:
        base_info = super().info()
        base_info.update({
            "visit_reason": self.visit_reason,
            "first_time": self.first_time
        })
        return base_info