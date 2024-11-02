# Task 2: Organ Donor Registration System (Event Management)

# organ_donor_event.py
class OrganDonorEvent:
    def __init__(self, name):
        self.name = name
        self.participant_count = 0

    # Method to add a donor to the event
    def add_donor(self):
        try:
            self.participant_count += 1
            print(f"Donor added successfully. Total donors: {self.participant_count}")
        except Exception as e:
            print(f"An unexpected error occurred while adding donor: {e}")

    # Method to add a participant to the event
    def add_participant(self):
        try:
            self.participant_count += 1
            print(f"Participant added successfully. Total participants: {self.participant_count}")
        except Exception as e:
            print(f"An unexpected error occurred while adding participant: {e}")

    # Method to get the current participant count
    def get_participant_count(self):
        try:
            return self.participant_count
        except Exception as e:
            print(f"An unexpected error occurred while retrieving participant count: {e}")
            return None
