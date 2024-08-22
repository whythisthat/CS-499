# main.py

# Import necessary functions from other modules
from intake import (
    initialize_dog_list, initialize_monkey_list, initialize_bird_list, 
    initialize_reptile_list, intake_new_dog, intake_new_monkey, 
    intake_new_bird, intake_new_reptile
)
from reserve import reserve_animal
from lookup import look_up_animal_by_name, look_up_animals_by_type
from print_animals import (
    print_dogs, print_monkeys, print_birds, print_reptiles, 
    print_available_animals
)
from delete import delete_dog, delete_monkey, delete_bird, delete_reptile

# Display functions for menus
def display_menu(title, options):
    print(f"\n\t\t\t{title}")
    for i, option in enumerate(options, 1):
        print(f"[{i}] {option}")
    print("Enter a menu selection: ")

# Helper function for input validation
def get_menu_selection(prompt, valid_range):
    while True:
        try:
            selection = int(input(prompt))
            if selection in valid_range:
                return selection
            else:
                print(f"Invalid input. Please enter a number between {valid_range.start} and {valid_range.stop - 1}.")
        except ValueError:
            print(f"Invalid input. Please enter a number between {valid_range.start} and {valid_range.stop - 1}.")

# Menu options
main_menu_options = [
    "Intake an animal", "Look up animal information", 
    "Print lists of animals", "Reserve an animal", 
    "Delete an animal", "Quit the application"
]

intake_menu_options = [
    "Intake a new dog", "Intake a new monkey", 
    "Intake a new bird", "Intake a new reptile", 
    "Return to main menu"
]

lookup_menu_options = [
    "Look up dog information", "Look up monkey information", 
    "Look up bird information", "Look up reptile information", 
    "Return to main menu"
]

print_menu_options = [
    "Print a list of all dogs", "Print a list of all monkeys", 
    "Print a list of all birds", "Print a list of all reptiles", 
    "Print a list of all animals that are not reserved", 
    "Return to main menu"
]

delete_menu_options = [
    "Delete a dog", "Delete a monkey", "Delete a bird", 
    "Delete a reptile", "Return to main menu"
]

def handle_intake_sub_menu():
    while True:
        display_menu("Intake Animal Sub-Menu", intake_menu_options)
        sub_option = get_menu_selection("Enter a menu selection: ", range(1, 6))
        if sub_option == 1:
            intake_new_dog()
        elif sub_option == 2:
            intake_new_monkey()
        elif sub_option == 3:
            intake_new_bird()
        elif sub_option == 4:
            intake_new_reptile()
        elif sub_option == 5:
            break

def handle_lookup_sub_menu():
    while True:
        display_menu("Look Up Animal Information Sub-Menu", lookup_menu_options)
        sub_option = get_menu_selection("Enter a menu selection: ", range(1, 6))
        if sub_option == 1:
            look_up_animals_by_type('dog')
        elif sub_option == 2:
            look_up_animals_by_type('monkey')
        elif sub_option == 3:
            look_up_animals_by_type('bird')
        elif sub_option == 4:
            look_up_animals_by_type('reptile')
        elif sub_option == 5:
            break

def handle_print_sub_menu():
    while True:
        display_menu("Print Animal Lists Sub-Menu", print_menu_options)
        sub_option = get_menu_selection("Enter a menu selection: ", range(1, 7))
        if sub_option == 1:
            print_dogs()
        elif sub_option == 2:
            print_monkeys()
        elif sub_option == 3:
            print_birds()
        elif sub_option == 4:
            print_reptiles()
        elif sub_option == 5:
            print_available_animals()
        elif sub_option == 6:
            break

def handle_delete_sub_menu():
    while True:
        display_menu("Delete Animal Sub-Menu", delete_menu_options)
        sub_option = get_menu_selection("Enter a menu selection: ", range(1, 6))
        if sub_option == 1:
            delete_dog()
        elif sub_option == 2:
            delete_monkey()
        elif sub_option == 3:
            delete_bird()
        elif sub_option == 4:
            delete_reptile()
        elif sub_option == 5:
            break

# Main function to run the program
def main():
    # Initialize the dictionaries with some predefined animals
    initialize_dog_list()
    initialize_monkey_list()
    initialize_bird_list()
    initialize_reptile_list()

    while True:
        display_menu("Rescue Animal System Menu", main_menu_options)
        option = get_menu_selection("Enter a menu selection: ", range(1, 7))

        if option == 1:
            handle_intake_sub_menu()
        elif option == 2:
            handle_lookup_sub_menu()
        elif option == 3:
            handle_print_sub_menu()
        elif option == 4:
            reserve_animal()
        elif option == 5:
            handle_delete_sub_menu()
        elif option == 6:
            print("You Exited the application. Good Bye!!!")
            break

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
