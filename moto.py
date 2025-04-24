from vehicle import Vehicle  # Assure-toi que ton fichier s'appelle bien vehicule.py

class Moto(Vehicle):
    def __init__(self, brand, model, year, color, moto_type):
        super().__init__(brand, model, year, color)
        self.moto_type = moto_type  # Par exemple: "Sport", "Cruiser", "Touring", etc.

    def pop_a_wheelie(self):
        return f"{self.brand} {self.model} fait un wheeling impressionnant!"

    def __str__(self):
        return (f"{self.year} {self.color} {self.brand} {self.model} "
                f"(Type: {self.moto_type}) - {self._mileage} miles, "
                f"Fuel: {self._fuel_level}%")
