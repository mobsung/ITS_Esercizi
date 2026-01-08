from Classi.smartDevice import SmartDevice

class SmartBulb(SmartDevice):

    def __init__(self, 
                 serial_number: str, 
                 brand: str, 
                 room: str, 
                 installation_year: int, 
                 status: str,
                 brightness_lumens: int,
                 color_capability: bool 
                ) -> None:
        
        super().__init__(serial_number, brand, room, installation_year, status)
        self.brightness_lumens = brightness_lumens
        self.color_capability = color_capability

    def device_type(self) -> str:
        return 'bulb'
    
    def energy_consumption(self) -> int:
        return 9
    
    def connection_quality(self) -> int:
        return 2
    
    def info(self):

        base_dict: dict = super().info()

        base_dict['brightness_lumens'] = self.brightness_lumens
        base_dict['color_capability'] = self.color_capability

        return base_dict
        
