from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from batteryy.spindler_battery import SpindlerBattery
from batteryy.nubbin_battery import NubbinBattery

#current date is being passed in create function, but not passed ahead as aleady being calculated in battery classes.
#program is not relying on user to provide it the current date, it is calculating the date accurately itself to avoid human error

class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage) 
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)  
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage) 
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)  
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)