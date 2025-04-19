from car import Car
from electric_car import ElectricCar

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

if __name__ == "__main__":
    main() 