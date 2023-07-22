from abc import ABC


class Battery(ABC):
    def needs_service(self):
        return self.age >= 3