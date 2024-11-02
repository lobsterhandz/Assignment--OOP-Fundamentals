 # main loop for the program
# main.py
from menu import Menu

def main():
    menu = Menu()
    while True:
        try:
            menu.display_menu()
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                menu.register_vehicle()
            elif choice == "2":
                menu.display_all_vehicles()
            elif choice == "3":
                menu.update_vehicle_owner()
            elif choice == "4":
                menu.register_organ_donor()
            elif choice == "5":
                menu.display_all_organ_donors()
            elif choice == "6":
                print("Exiting Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
