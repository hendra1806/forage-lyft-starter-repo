from datetime import datetime
from abc import ABC

from car import Car


class CapuletEngine(Car, ABC):
    SERVICE_INTERVAL = 30000  # Miles

    def __init__(self, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self) -> bool:
        return self.current_mileage - self.last_service_mileage > self.SERVICE_INTERVAL
