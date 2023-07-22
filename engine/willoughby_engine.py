from abc import ABC

from car import Car


class WilloughbyEngine(Car, ABC):
    SERVICE_THRESHOLD_MILEAGE = 60000

    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self) -> bool:
        return self.current_mileage - self.last_service_mileage > self.SERVICE_THRESHOLD_MILEAGE
