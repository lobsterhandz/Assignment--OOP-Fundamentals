Vehicle and Organ Donor Management System

Overview

This project is a Python-based command-line management system that allows users to register vehicles, update owners, and register as organ donors. The system features classes for vehicles, organ donors, and a menu-driven interface, alongside input handling for validation.

Key Components

Vehicle Registration System: Allows users to register vehicles, update vehicle owners, and display all registered vehicles.

Organ Donor Event Management: Offers users the ability to register as organ donors and display the list of all registered donors. Organ donation is treated as a public event where participants can opt-in.

Input Handling Module: Ensures user inputs are validated and consistent, improving the user experience.

Project Structure

vehicle.py: Contains the Vehicle class, used for vehicle registration and owner management.

organ_donor_event.py: Contains the OrganDonorEvent class, which manages organ donation participation as an event.

input_handling.py: Handles user input validation, ensuring inputs are not empty and supporting yes/no questions with flexibility.

menu.py: Implements the Menu class, which presents a user-friendly command-line interface for managing vehicles and organ donation events.

main.py: The entry point of the program that initializes the menu and starts the management loop.

Features

1. Vehicle Management

Register a Vehicle: Users can register a new vehicle by providing the registration number, vehicle type, and owner's name.

Update Vehicle Owner: Change the ownership of a registered vehicle.

Display All Vehicles: View the details of all registered vehicles.

2. Organ Donor Event Management

Register as an Organ Donor: Users can opt-in to become an organ donor. They are prompted to do so after registering a vehicle or directly from the menu.

Display All Organ Donors: Lists all the donors registered in the system.

3. User Input Handling

The InputHandler class handles all user inputs:

Non-Empty Input: Prompts the user until a valid non-empty input is provided.

Yes/No Input: Accepts variations like yes, no, y, n in any casing.

How to Run the Project

Clone the repository to your local machine.

Navigate to the project directory.

Run the main.py file using Python:

python main.py

Follow the on-screen prompts to interact with the system.

Example Usage

After running main.py, users will be presented with the main menu.

Users can select options such as registering a vehicle, updating vehicle owners, and opting to register as organ donors.

After registering a vehicle, users are smoothly prompted to decide if they want to become an organ donor.
