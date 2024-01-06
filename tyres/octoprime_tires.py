from tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, sensor_readings):
        self.sensor_readings=sensor_readings

    def needs_service(self) -> bool:
        readings_sum=sum(self.sensor_readings)

        if readings_sum >= 3:
            return True
        else:
            return False



    