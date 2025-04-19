from car import Car
from electric_car import ElectricCar
from luxury_car import LuxuryCar

def main():
    # Create a regular car
    my_car = Car("Toyota", "Camry", 2022, "Silver", 4, "Automatic")
    print("Regular Car Demo:")
    print(my_car.get_info())
    print(my_car.start_engine())
    print(my_car.honk())
    print(my_car.add_mileage(50))
    print(my_car.get_mileage())
    print(my_car.stop_engine())
    print()

    # Create an electric car
    my_electric = ElectricCar("Tesla", "Model 3", 2023, "Red", 4, "Automatic", 75)
    print("Electric Car Demo:")
    print(my_electric.get_info())
    print(my_electric.start_engine())
    print(my_electric.start_charging())
    print(my_electric.charge_battery(20))
    print(my_electric.get_battery_level())
    print(my_electric.stop_charging())
    print(my_electric.stop_engine())
    print()

    # Create a luxury car
    my_luxury = LuxuryCar("Mercedes-Benz", "S-Class",

                          2023, "Black", 4, "Automatic")
    print("Luxury Car Demo:")
    print(my_luxury.get_info())
    print(my_luxury.start_engine())
    print(my_luxury.activate_massage_seats())
    print(my_luxury.set_climate_control(24))
    print(my_luxury.set_ambient_lighting("blue"))
    print(my_luxury.get_luxury_features())
    print(my_luxury.deactivate_massage_seats())
    print(my_luxury.stop_engine())

if __name__ == "__main__":
    main() 