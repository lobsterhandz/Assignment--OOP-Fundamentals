# menu.py
from vehicle import Vehicle
from organ_donor_event import OrganDonorEvent
from input_handling import InputHandler

class Menu:
    def __init__(self):
        self.vehicles = []
        self.organ_donors = []

    def display_menu(self):
        print("\n--- Management System Menu ---")
        print("1. Register a new vehicle")
        print("2. Display all vehicles")
        print("3. Update vehicle owner")
        print("4. Register as an organ donor (Event)")
        print("5. Display all organ donors")
        print("6. Exit")

    def register_vehicle(self):
        try:
            reg_num = InputHandler.get_non_empty_input("Enter registration number: ")
            if any(vehicle.registration_number == reg_num for vehicle in self.vehicles):
                raise ValueError("A vehicle with this registration number already exists.")

            type = InputHandler.get_non_empty_input("Enter vehicle type: ")
            owner = InputHandler.get_non_empty_input("Enter owner name: ")

            new_vehicle = Vehicle(reg_num, type, owner)
            self.vehicles.append(new_vehicle)
            print("Vehicle registered successfully.")

            # Smoothly ask if they want to be an organ donor after registering a vehicle
            if InputHandler.get_yes_no_input("Would you like to register as an organ donor as well? (yes/no): "):
                self.register_organ_donor(owner)
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_all_vehicles(self):
        try:
            if not self.vehicles:
                print("No vehicles registered.")
            else:
                print("\n--- Vehicle Information ---")
                for vehicle in self.vehicles:
                    vehicle.display_info()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def update_vehicle_owner(self):
        try:
            reg_num = InputHandler.get_non_empty_input("Enter registration number of the vehicle to update: ")

            vehicle_found = False
            for vehicle in self.vehicles:
                if vehicle.registration_number == reg_num:
                    new_owner = InputHandler.get_non_empty_input("Enter new owner's name: ")
                    vehicle.update_owner(new_owner)
                    vehicle_found = True
                    break
            if not vehicle_found:
                print("Vehicle not found.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def register_organ_donor(self, owner_name=None):
        try:
            if not owner_name:
                name = InputHandler.get_non_empty_input("Enter donor name: ")
            else:
                name = owner_name

            if any(donor.name == name for donor in self.organ_donors):
                raise ValueError("A donor with this name already exists.")

            new_donor = OrganDonorEvent(name)
            new_donor.add_participant()  # Use add_participant method for consistency
            self.organ_donors.append(new_donor)
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_all_organ_donors(self):
        try:
            if not self.organ_donors:
                print("No organ donors registered.")
            else:
                print("\n--- Organ Donor Information ---")
                for donor in self.organ_donors:
                    print(f"Donor Name: {donor.name}, Total Donors: {donor.get_participant_count()}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")