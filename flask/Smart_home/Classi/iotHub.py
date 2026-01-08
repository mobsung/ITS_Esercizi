from Classi.smartDevice import SmartDevice

class IoTHub:

    def __init__(self) ->  None:
        self.devices: dict[str, SmartDevice] = {}

    def add(self, device: SmartDevice) -> bool:
        if device.serial_number not in self.devices:
            self.devices[device.serial_number] = device
            return True
        return False
    
    def get(self, serial_number: str) -> SmartDevice | None:
        if serial_number in self.devices:
            return self.devices.get(serial_number)
        return None
    
    def update(self, serial_number: str, new_device: SmartDevice) -> None:
        if serial_number in self.devices:
            self.devices[serial_number] = new_device

    def patch_status(self, serial_number: str, new_status: str) -> None:
        if serial_number in self.devices:
            self.devices[serial_number].status = new_status

    def delete(self, serial_number: str) -> bool:
        if serial_number in self.devices:
            self.devices.pop(serial_number)
            return True
        return False
    
    def list_all(self) -> list[dict[str, float | int | str]]:
        return [d.info() for d in self.devices.values()]
