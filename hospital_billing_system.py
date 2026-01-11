# hospital_billing_system.py
#An OOPS-based Python program to calculate hospital consultation charges for different patient types.

## Concepts Used
#- Inheritance
#- Polymorphism
#- Method Overriding
#- Abstraction

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def calculate_bill(self):
        raise NotImplementedError("Subclasses must implement this method")


class GeneralPatient(Patient):
    def calculate_bill(self):
        consultation_fee = 300
        return consultation_fee


class SpecialistPatient(Patient):
    def calculate_bill(self):
        consultation_fee = 700
        return consultation_fee


class EmergencyPatient(Patient):
    def calculate_bill(self):
        consultation_fee = 1000
        emergency_charge = 500
        return consultation_fee + emergency_charge


# -------- MAIN PROGRAM --------

print("---- Hospital Appointment & Billing System ----")
print("1. General Patient")
print("2. Specialist Patient")
print("3. Emergency Patient")

choice = input("Choose patient type (1/2/3 or general/specialist/emergency): ").lower()

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

if choice == "1" or choice == "general":
    patient = GeneralPatient(name, age)

elif choice == "2" or choice == "specialist":
    patient = SpecialistPatient(name, age)

elif choice == "3" or choice == "emergency":
    patient = EmergencyPatient(name, age)

else:
    print("❌ Invalid choice")
    exit()

bill = patient.calculate_bill()

print("\n--- Patient Bill Summary ---")
print("Patient Name:", patient.name)
print("Age:", patient.age)
print("Total Bill: ₹", bill)
