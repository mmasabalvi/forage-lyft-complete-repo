from engine.engines import Engines

class SternmanEngine(Engines):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        if self.warning_light_is_on:
            return True
        else:
            return False
    