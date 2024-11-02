class InputHandler:
    @staticmethod
    def get_non_empty_input(prompt):
        while True:
            user_input = input(prompt).strip()
            if user_input:
                return user_input
            print("Input cannot be empty. Please try again.")

    @staticmethod
    def get_yes_no_input(prompt):
        while True:
            user_input = input(prompt).strip().lower()
            if user_input in ('yes', 'y'):
                return True
            elif user_input in ('no', 'n'):
                return False
            else:
                print("Invalid input. Please enter yes, no, y, or n.")