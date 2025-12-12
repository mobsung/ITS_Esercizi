
from Classi.device import Device

class ServiceCenter:

    def __init__(self) -> None:
        self.devices: dict[str, Device] = {}


    def add(self, device: Device) -> bool:
        if device.id not in self.devices:
            self.devices[device.id] = device
            return True
        return False
    
    def get(self, device_id: str) -> Device | None:
        if device_id in self.devices:
            return self.devices[device_id]
        return None
    

    def update(self, device_id: str, new_device: Device) -> None:
        if device_id in self.devices:
            self.devices[device_id] = new_device

    def patch_status(self, device_id: str, new_status: str) -> None:
        if device_id in self.devices:
            self.devices[device_id].setStatus(new_status)

    def delete(self, device_id) -> bool:
        if device_id in self.devices:
            self.devices.pop(device_id)
            return True
        return False
    
    def list_all(self) -> list[dict]:
        return [d.info() for d in self.devices]