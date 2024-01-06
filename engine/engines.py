from abc import ABC, abstractmethod


class Engines(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass 
