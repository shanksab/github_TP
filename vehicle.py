class Vehicle:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self._mileage = 0  # Protected attribute
        self._fuel_level = 100  # Protected attribute

    def start_engine(self):
        return f"Starting {self.brand} {self.model}'s engine..."

    def stop_engine(self):
        return f"Stopping {self.brand} {self.model}'s engine..."

    def get_mileage(self):
        return self._mileage

    def add_mileage(self, distance):
        if distance > 0:
            self._mileage += distance
            return f"Added {distance} miles. New mileage: {self._mileage}"
        return "Distance must be positive"

    def get_fuel_level(self):
        return self._fuel_level

    def refuel(self, amount):
        if amount > 0:
            self._fuel_level = min(100, self._fuel_level + amount)
            return f"Refueled {amount} units. New fuel level: {self._fuel_level}%"
        return "Amount must be positive" 