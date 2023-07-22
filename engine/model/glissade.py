from datetime import datetime, timedelta
from engine.willoughby_engine import WilloughbyEngine


class Glissade(WilloughbyEngine):
    def needs_service(self):
        service_interval = timedelta(days=730)  # Equivalent to 2 years
        service_threshold_date = self.last_service_date + service_interval

        if service_threshold_date <= datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
