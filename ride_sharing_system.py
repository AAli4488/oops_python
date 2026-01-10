# ride_sharing_system.py

class Ride:
    def calculate_fare(self, distance):
        raise NotImplementedError


class BikeRide(Ride):
    def calculate_fare(self, distance):
        return distance * 10


class CarRide(Ride):
    def calculate_fare(self, distance):
        return distance * 20


class LuxuryRide(Ride):
    def calculate_fare(self, distance):
        surge = 1.5
        return distance * 40 * surge


# ----------- MAIN PROGRAM -----------

print("---- Ride Sharing System ----")
print("1. Bike")
print("2. Car")
print("3. Luxury")

choice = input("Choose ride type (1/2/3 or bike/car/luxury): ").lower()
distance = float(input("Enter distance (km): "))

if choice == "1" or choice == "bike":
    ride = BikeRide()

elif choice == "2" or choice == "car":
    ride = CarRide()

elif choice == "3" or choice == "luxury":
    ride = LuxuryRide()

else:
    print("❌ Invalid choice")
    exit()

fare = ride.calculate_fare(distance)

print("\n--- Ride Summary ---")
print("Distance:", distance, "km")
print("Total Fare:", fare)