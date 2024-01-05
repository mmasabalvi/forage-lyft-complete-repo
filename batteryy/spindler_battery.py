from datetime import datetime

from batteryy.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = datetime.today().date()

    def needs_service(self) -> bool:
        if self.last_service_date.year + 2 < self.current_date.year:
            return True
        else:
            return False

        
