class CarriganTire:
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        # Service Carrigan tires when any value in tire_wear array is greater than or equal to 0.9
        for value in self.tire_wear:
            if value >= 0.9:
                return True
        return False


class OctoprimeTire:
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        # Service Octoprime tires when the sum of values in tire_wear array is greater than or equal to 3
        return sum(self.tire_wear) >= 3
