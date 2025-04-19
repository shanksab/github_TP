from car import Car

class ElectricCar(Car):
    def __init__(self, brand, model, year, color, num_doors, transmission_type, battery_capacity):
        super().__init__(brand, model, year, color, num_doors, transmission_type)
        self.battery_capacity = battery_capacity  # in kWh
        self._battery_level = 100
        self._charging = False

    def start_charging(self):
        if not self._charging:
            self._charging = True
            return "Started charging the battery"
        return "Already charging"

    def stop_charging(self):
        if self._charging:
            self._charging = False
            return "Stopped charging the battery"
        return "Not currently charging"

    def get_battery_level(self):
        return self._battery_level

    def charge_battery(self, amount):
        if amount > 0:
            self._battery_level = min(100, self._battery_level + amount)
            return f"Charged {amount}%. New battery level: {self._battery_level}%"
        return "Amount must be positive"

    def get_info(self):
        base_info = super().get_info()
        return (f"{base_info}\n"
                f"Battery Capacity: {self.battery_capacity} kWh\n"
                f"Battery Level: {self._battery_level}%") 