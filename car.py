from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, color, num_doors, transmission_type):
        super().__init__(brand, model, year, color)
        self.num_doors = num_doors
        self.transmission_type = transmission_type
        self._is_locked = True

    def lock_doors(self):
        self._is_locked = True
        return "Doors locked"

    def unlock_doors(self):
        self._is_locked = False
        return "Doors unlocked"

    def get_door_status(self):
        return "locked" if self._is_locked else "unlocked"

    def honk(self):
        return "Beep! Beep!"

    def get_info(self):
        return (f"{self.year} {self.brand} {self.model}\n"
                f"Color: {self.color}\n"
                f"Doors: {self.num_doors}\n"
                f"Transmission: {self.transmission_type}\n"
                f"Mileage: {self._mileage}\n"
                f"Fuel Level: {self._fuel_level}%") 