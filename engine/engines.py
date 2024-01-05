from abc import ABC, abstractmethod

from car import Car

class Engines(Car,ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass 
