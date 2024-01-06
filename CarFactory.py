from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from batteryy.spindler_battery import SpindlerBattery
from batteryy.nubbin_battery import NubbinBattery
from tyres.octoprime_tires import OctoprimeTires
from tyres.carrigan_tires import CarriganTires

#current date is being passed in create function, but not passed ahead as aleady being calculated in battery classes.
#program is not relying on user to provide it the current date, it is calculating the date accurately itself to avoid human error

class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, sensor_readings):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date)
        tire = OctoprimeTires(sensor_readings)
        return Car(engine, battery, tire)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, sensor_readings):
        engine = WilloughbyEngine(last_service_mileage, current_mileage) 
        battery = SpindlerBattery(last_service_date)
        tire = CarriganTires(sensor_readings)
        return Car(engine, battery, tire)

    def create_palindrome(self, current_date, last_service_date, warning_light_on, sensor_readings):
        engine = SternmanEngine(warning_light_on)  
        battery = SpindlerBattery(last_service_date)
        tire = OctoprimeTires(sensor_readings)
        return Car(engine, battery, tire)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, sensor_readings):
        engine = WilloughbyEngine(last_service_mileage, current_mileage) 
        battery = NubbinBattery(last_service_date)
        tire = CarriganTires(sensor_readings)
        return Car(engine, battery, tire)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, sensor_readings):
        engine = CapuletEngine(last_service_mileage, current_mileage)  
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTires(sensor_readings)
        return Car(engine, battery, tire)
