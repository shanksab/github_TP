# Vehicle Management System

This is a simple Python project that demonstrates object-oriented programming concepts using a vehicle management system. The project includes a hierarchy of vehicle classes with different features and capabilities.

## Project Structure

- `vehicle.py`: Contains the base `Vehicle` class with common attributes and methods
- `car.py`: Contains the `Car` class that inherits from `Vehicle`
- `electric_car.py`: Contains the `ElectricCar` class that inherits from `Car`
- `luxury_car.py`: Contains the `LuxuryCar` class that inherits from `Car`
- `main.py`: Demonstrates the usage of all classes

## Features

### Vehicle Class
- Basic vehicle attributes (brand, model, year, color)
- Mileage tracking
- Fuel level management
- Engine control

### Car Class (inherits from Vehicle)
- Door management (lock/unlock)
- Transmission type
- Honking capability
- Detailed information display

### ElectricCar Class (inherits from Car)
- Battery capacity and level management
- Charging functionality
- Extended information display

### LuxuryCar Class (inherits from Car)
- Luxury features (leather interior, sunroof, premium sound system)
- Massage seats control
- Climate control system
- Ambient lighting with multiple modes
- Extended information display with luxury features

## How to Run

1. Make sure you have Python 3.x installed
2. Run the main.py file:
```bash
python main.py
```

## Example Output

The program will demonstrate:
- Creating and managing a regular car
- Creating and managing an electric car
- Creating and managing a luxury car
- Various operations like starting/stopping engines, charging, and displaying information

## Learning Points

This project demonstrates several OOP concepts:
- Inheritance
- Encapsulation
- Method overriding
- Protected attributes
- Polymorphism 