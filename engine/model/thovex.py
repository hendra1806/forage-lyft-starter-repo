from datetime import datetime, timedelta
from engine.capulet_engine import CapuletEngine


class Thovex(CapuletEngine):
    def needs_service(self):
        service_interval = timedelta(days=1460)  # Equivalent to 4 years
        service_threshold_date = self.last_service_date + service_interval

        if service_threshold_date <= datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
