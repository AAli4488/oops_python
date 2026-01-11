# smart_parking_oops.py
# Smart Parking Management System (Python)

#A Python OOPS-based system to calculate parking fees for different vehicle types using polymorphism.

## Concepts Used
#- Inheritance
#- Polymorphism
#- Encapsulation

class Vehicle:
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number

    def calculate_fee(self, hours):
        raise NotImplementedError("Subclasses must implement this method")


class Bike(Vehicle):
    def calculate_fee(self, hours):
        return hours * 20


class Car(Vehicle):
    def calculate_fee(self, hours):
        return hours * 40


class Truck(Vehicle):
    def calculate_fee(self, hours):
        return hours * 70


# -------- Main Program --------

print("---- Smart Parking Management System ----")
print("1. Bike")
print("2. Car")
print("3. Truck")

choice = input("Choose vehicle type (1/2/3 or bike/car/truck): ").lower()
vehicle_number = input("Enter vehicle number: ")
hours = int(input("Enter parking hours: "))

if choice == "1" or choice == "bike":
    vehicle = Bike(vehicle_number)

elif choice == "2" or choice == "car":
    vehicle = Car(vehicle_number)

elif choice == "3" or choice == "truck":
    vehicle = Truck(vehicle_number)

else:
    print("❌ Invalid vehicle type")
    exit()

fee = vehicle.calculate_fee(hours)

print("\n--- Parking Receipt ---")
print("Vehicle Number:", vehicle.vehicle_number)
print("Parking Hours:", hours)
print("Total Fee: ₹", fee)
