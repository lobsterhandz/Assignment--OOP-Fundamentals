# vehicle.py
# Task 1: Vehicle Registration System
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    # Method to update the owner of the vehicle
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated to: {new_owner}")

    # Method to print vehicle details
    def display_info(self):
        print(f"Registration Number: {self.registration_number}, Type: {self.type}, Owner: {self.owner}")
