from tires import Tires

class CarriganTires(Tires):
    def __init__(self, sensor_readings):
        self.sensor_readings=sensor_readings

    def needs_service(self) -> bool:
        for number in self.sensor_readings:
            if number > 0.9:
                return True
    
        return False