from Serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        self.engines  = engine
        self.battery = battery
        self.tire = tires

    def needs_service(self) -> bool:
        return self.engines.needs_service() or self.battery.needs_service() or self.tire.needs_service()
