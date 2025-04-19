from car import Car

class LuxuryCar(Car):
    def __init__(self, brand, model, year, color, num_doors, transmission_type, leather_interior=True, sunroof=True, premium_sound_system=True):
        super().__init__(brand, model, year, color, num_doors, transmission_type)
        self.leather_interior = leather_interior
        self.sunroof = sunroof
        self.premium_sound_system = premium_sound_system
        self._massage_seats_active = False
        self._climate_control_temp = 22  # Default temperature in Celsius
        self._ambient_lighting = "off"

    def activate_massage_seats(self):
        if not self._massage_seats_active:
            self._massage_seats_active = True
            return "Massage seats activated"
        return "Massage seats already active"

    def deactivate_massage_seats(self):
        if self._massage_seats_active:
            self._massage_seats_active = False
            return "Massage seats deactivated"
        return "Massage seats already inactive"

    def set_climate_control(self, temperature):
        if 16 <= temperature <= 30:
            self._climate_control_temp = temperature
            return f"Climate control set to {temperature}°C"
        return "Temperature must be between 16°C and 30°C"

    def set_ambient_lighting(self, mode):
        valid_modes = ["off", "blue", "red", "green", "purple", "white"]
        if mode.lower() in valid_modes:
            self._ambient_lighting = mode.lower()
            return f"Ambient lighting set to {mode}"
        return f"Invalid mode. Choose from: {', '.join(valid_modes)}"

    def get_luxury_features(self):
        features = []
        if self.leather_interior:
            features.append("Leather Interior")
        if self.sunroof:
            features.append("Sunroof")
        if self.premium_sound_system:
            features.append("Premium Sound System")
        features.append(f"Massage Seats: {'Active' if self._massage_seats_active else 'Inactive'}")
        features.append(f"Climate Control: {self._climate_control_temp}°C")
        features.append(f"Ambient Lighting: {self._ambient_lighting}")
        return features

    def get_info(self):
        base_info = super().get_info()
        luxury_features = "\n".join([f"- {feature}" for feature in self.get_luxury_features()])
        return (f"{base_info}\n"
                f"Luxury Features:\n{luxury_features}") 