# Define the base class for all rescue animals
class RescueAnimal:
    def __init__(self, name, animal_type, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country):
        self.name = name
        self.animal_type = animal_type
        self.gender = gender
        self.age = age
        self.weight = weight
        self.acquisition_date = acquisition_date
        self.acquisition_country = acquisition_country
        self.training_status = training_status
        self.reserved = reserved
        self.in_service_country = in_service_country

    def __str__(self):
        return f"Name: {self.name}\nAnimal Type: {self.animal_type}\nGender: {self.gender}\nAge: {self.age}\nWeight: {self.weight}\nAcquisition Date: {self.acquisition_date}\nAcquisition Country: {self.acquisition_country}\nTraining Status: {self.training_status}\nReserved: {self.reserved}\nIn Service Country: {self.in_service_country}"


# Define subclasses for each animal type
class Dog(RescueAnimal):
    pass


class Monkey(RescueAnimal):
    pass


class Bird(RescueAnimal):
    pass


class Reptile(RescueAnimal):
    pass


# Initialize dictionaries to store each type of animal
dog_dict = {}
monkey_dict = {}
bird_dict = {}
reptile_dict = {}

# Define indexes
name_index = {}
type_index = {
    "dog": {},
    "monkey": {},
    "bird": {},
    "reptile": {}
}


# Function to add animal to indexes
def add_animal_to_indexes(animal, animal_type):
    # Update name index
    name_index[animal.name] = animal
    
    # Update type index
    if animal_type not in type_index:
        type_index[animal_type] = {}
    type_index[animal_type][animal.name] = animal


# Function to remove animal from indexes
def remove_animal_from_indexes(animal, animal_type):
    # Update name index
    if animal.name in name_index:
        del name_index[animal.name]
    
    # Update type index
    if animal.name in type_index[animal_type]:
        del type_index[animal_type][animal.name]


# Function to display the main menu options
def display_main_menu():
    print("\n\t\t\tRescue Animal System Menu")
    print("[1] Intake an animal")
    print("[2] Look up animal information")
    print("[3] Print lists of animals")
    print("[4] Reserve an animal")
    print("[5] Delete an animal")
    print("[6] Quit the application")
    print("Enter a menu selection: ")


# Function to display the sub-menu options for intake
def display_intake_sub_menu():
    print("\n\t\t\tIntake Animal Sub-Menu")
    print("[1] Intake a new dog")
    print("[2] Intake a new monkey")
    print("[3] Intake a new bird")
    print("[4] Intake a new reptile")
    print("[5] Return to main menu")
    print("Enter a menu selection: ")


# Function to display the sub-menu options for lookup
def display_lookup_sub_menu():
    print("\n\t\t\tLook Up Animal Information Sub-Menu")
    print("[1] Look up dog information")
    print("[2] Look up monkey information")
    print("[3] Look up bird information")
    print("[4] Look up reptile information")
    print("[5] Return to main menu")
    print("Enter a menu selection: ")


# Function to display the sub-menu options for print
def display_print_sub_menu():
    print("\n\t\t\tPrint Animal Lists Sub-Menu")
    print("[1] Print a list of all dogs")
    print("[2] Print a list of all monkeys")
    print("[3] Print a list of all birds")
    print("[4] Print a list of all reptiles")
    print("[5] Print a list of all animals that are not reserved")
    print("[6] Return to main menu")
    print("Enter a menu selection: ")


# Function to display the sub-menu options for delete
def display_delete_sub_menu():
    print("\n\t\t\tDelete Animal Sub-Menu")
    print("[1] Delete a dog")
    print("[2] Delete a monkey")
    print("[3] Delete a bird")
    print("[4] Delete a reptile")
    print("[5] Return to main menu")
    print("Enter a menu selection: ")


# Function to initialize the dog dictionary with some dogs
def initialize_dog_list():
    dog1 = Dog("Spot", "German Shepherd", "male", "1", "25.6", "05-12-2019", "United States", "intake", False, "United States")
    dog2 = Dog("Rex", "Great Dane", "male", "3", "35.2", "02-03-2020", "United States", "Phase I", False, "United States")
    dog3 = Dog("Bella", "Chihuahua", "female", "4", "25.6", "12-12-2019", "Canada", "in service", True, "Canada")
    dog_dict[dog1.name] = dog1
    dog_dict[dog2.name] = dog2
    dog_dict[dog3.name] = dog3
    add_animal_to_indexes(dog1, "dog")
    add_animal_to_indexes(dog2, "dog")
    add_animal_to_indexes(dog3, "dog")


# Function to initialize the monkey dictionary with some monkeys
def initialize_monkey_list():
    mon1 = Monkey("Mony", "Capuchin Monkey", "male", "1", "9", "04-12-2019", "United States", "intake", False, "United States")
    mon2 = Monkey("Rexon", "Squirrel Monkey", "male", "5", "18.4", "02-03-2020", "United States", "intake", False, "United States")
    mon3 = Monkey("Della", "Spider Monkey", "female", "6", "25.6", "12-12-2019", "Canada", "in service", False, "Canada")
    monkey_dict[mon1.name] = mon1
    monkey_dict[mon2.name] = mon2
    monkey_dict[mon3.name] = mon3
    add_animal_to_indexes(mon1, "monkey")
    add_animal_to_indexes(mon2, "monkey")
    add_animal_to_indexes(mon3, "monkey")


# Function to initialize the bird dictionary with some birds
def initialize_bird_list():
    bird1 = Bird("Tweety", "Parrot", "female", "2", "0.5", "01-10-2021", "Australia", "intake", False, "Australia")
    bird2 = Bird("Sky", "Sparrow", "male", "1", "0.2", "11-11-2020", "United States", "Phase I", False, "United States")
    bird_dict[bird1.name] = bird1
    bird_dict[bird2.name] = bird2
    add_animal_to_indexes(bird1, "bird")
    add_animal_to_indexes(bird2, "bird")


# Function to initialize the reptile dictionary with some reptiles
def initialize_reptile_list():
    reptile1 = Reptile("Slinky", "Iguana", "male", "3", "1.5", "07-12-2019", "Brazil", "in service", False, "Brazil")
    reptile2 = Reptile("Creepy", "Snake", "female", "4", "2.1", "03-04-2020", "India", "Phase II", False, "India")
    reptile_dict[reptile1.name] = reptile1
    reptile_dict[reptile2.name] = reptile2
    add_animal_to_indexes(reptile1, "reptile")
    add_animal_to_indexes(reptile2, "reptile")


# Function to intake a new dog
def intake_new_dog():
    name = input("What is the dog's name? ")

    # Check if the dog is already in the system
    if name in dog_dict:
        print("\n\nThis dog is already in our system\n\n")
        return

    a_type = input("Enter the dog's breed: ")
    gender = input("Enter the dog's gender: ")
    age = input("Enter the dog's age: ")
    weight = input("Enter the dog's weight: ")
    a_date = input("Enter the dog's acquisition date: ")
    a_country = input("Enter the dog's acquisition country: ")
    status = input("Enter the dog's training status: ")
    reserved = input("Enter the dog's reserved status (true/false): ").lower() == 'true'
    ser_country = input("Enter the dog's in service country name: ")

    # Add the new dog to the dictionary
    dog1 = Dog(name, a_type, gender, age, weight, a_date, a_country, status, reserved, ser_country)
    dog_dict[name] = dog1

    # Add to indexes
    add_animal_to_indexes(dog1, "dog")


# Function to intake a new monkey
def intake_new_monkey():
    name = input("What is the monkey's name? ")
    a_type = input("What is the monkey's species type? ")

    # Check if the monkey is already in the system
    if name in monkey_dict and monkey_dict[name].animal_type.lower() == a_type.lower():
        print("\n\nThis monkey is already in our system\n\n")
        return

    gender = input("Enter the monkey's gender: ")
    age = input("Enter the monkey's age: ")
    weight = input("Enter the monkey's weight: ")
    a_date = input("Enter the monkey's acquisition date: ")
    a_country = input("Enter the monkey's acquisition country: ")
    status = input("Enter the monkey's training status: ")
    reserved = input("Enter the monkey's reserved status (true/false): ").lower() == 'true'
    ser_country = input("Enter the monkey's in service country name: ")

    # Add the new monkey to the dictionary
    mon1 = Monkey(name, a_type, gender, age, weight, a_date, a_country, status, reserved, ser_country)
    monkey_dict[name] = mon1

    # Add to indexes
    add_animal_to_indexes(mon1, "monkey")


# Function to intake a new bird
def intake_new_bird():
    name = input("What is the bird's name? ")
    a_type = input("What is the bird's species type? ")

    # Check if the bird is already in the system
    if name in bird_dict and bird_dict[name].animal_type.lower() == a_type.lower():
        print("\n\nThis bird is already in our system\n\n")
        return

    gender = input("Enter the bird's gender: ")
    age = input("Enter the bird's age: ")
    weight = input("Enter the bird's weight: ")
    a_date = input("Enter the bird's acquisition date: ")
    a_country = input("Enter the bird's acquisition country: ")
    status = input("Enter the bird's training status: ")
    reserved = input("Enter the bird's reserved status (true/false): ").lower() == 'true'
    ser_country = input("Enter the bird's in service country name: ")

    # Add the new bird to the dictionary
    bird1 = Bird(name, a_type, gender, age, weight, a_date, a_country, status, reserved, ser_country)
    bird_dict[name] = bird1

    # Add to indexes
    add_animal_to_indexes(bird1, "bird")


# Function to intake a new reptile
def intake_new_reptile():
    name = input("What is the reptile's name? ")
    a_type = input("What is the reptile's species type? ")

    # Check if the reptile is already in the system
    if name in reptile_dict and reptile_dict[name].animal_type.lower() == a_type.lower():
        print("\n\nThis reptile is already in our system\n\n")
        return

    gender = input("Enter the reptile's gender: ")
    age = input("Enter the reptile's age: ")
    weight = input("Enter the reptile's weight: ")
    a_date = input("Enter the reptile's acquisition date: ")
    a_country = input("Enter the reptile's acquisition country: ")
    status = input("Enter the reptile's training status: ")
    reserved = input("Enter the reptile's reserved status (true/false): ").lower() == 'true'
    ser_country = input("Enter the reptile's in service country name: ")

    # Add the new reptile to the dictionary
    reptile1 = Reptile(name, a_type, gender, age, weight, a_date, a_country, status, reserved, ser_country)
    reptile_dict[name] = reptile1

    # Add to indexes
    add_animal_to_indexes(reptile1, "reptile")


# Function to reserve an animal
def reserve_animal():
    a_type = input("Enter the desired animal type: ")
    country = input("Enter the desired country name: ")

    # Attempt to reserve a dog
    for dog in dog_dict.values():
        if dog.animal_type.lower() == a_type.lower() and dog.in_service_country.lower() == country.lower() and not dog.reserved:
            dog.reserved = True
            print("Animal is reserved successfully")
            return

    # Attempt to reserve a monkey
    for monkey in monkey_dict.values():
        if monkey.animal_type.lower() == a_type.lower() and monkey.in_service_country.lower() == country.lower() and not monkey.reserved:
            monkey.reserved = True
            print("Animal is reserved successfully")
            return

    # Attempt to reserve a bird
    for bird in bird_dict.values():
        if bird.animal_type.lower() == a_type.lower() and bird.in_service_country.lower() == country.lower() and not bird.reserved:
            bird.reserved = True
            print("Animal is reserved successfully")
            return

    # Attempt to reserve a reptile
    for reptile in reptile_dict.values():
        if reptile.animal_type.lower() == a_type.lower() and reptile.in_service_country.lower() == country.lower() and not reptile.reserved:
            reptile.reserved = True
            print("Animal is reserved successfully")
            return

    # If no animal is available for the given type and location
    print("No animal type and location of your desired choice is available")


# Function to print all dogs
def print_dogs():
    print("Dog Details")
    print("-----------------------------------")
    for dog in dog_dict.values():
        print(dog)


# Function to print all monkeys
def print_monkeys():
    print("Monkey Details")
    print("-----------------------------------")
    for monkey in monkey_dict.values():
        print(monkey)


# Function to print all birds
def print_birds():
    print("Bird Details")
    print("-----------------------------------")
    for bird in bird_dict.values():
        print(bird)


# Function to print all reptiles
def print_reptiles():
    print("Reptile Details")
    print("-----------------------------------")
    for reptile in reptile_dict.values():
        print(reptile)


# Function to print all available animals (not reserved and in service)
def print_available_animals():
    print("Displaying all Available Animals")
    print("-----------------------------------")

    for dog in dog_dict.values():
        if not dog.reserved and dog.training_status.lower() == "in service":
            print(dog)

    for monkey in monkey_dict.values():
        if not monkey.reserved and monkey.training_status.lower() == "in service":
            print(monkey)

    for bird in bird_dict.values():
        if not bird.reserved and bird.training_status.lower() == "in service":
            print(bird)

    for reptile in reptile_dict.values():
        if not reptile.reserved and reptile.training_status.lower() == "in service":
            print(reptile)


# Function to look up an animal by name
def look_up_animal_by_name(name):
    if name in name_index:
        print(name_index[name])
    else:
        print(f"No animal found with the name '{name}'.")


# Function to look up animals by type
def look_up_animals_by_type(animal_type):
    if animal_type in type_index:
        for animal in type_index[animal_type].values():
            print(animal)
    else:
        print(f"No animals of type '{animal_type}' found.")


# Function to delete an animal
def delete_animal(name, animal_dict, animal_type):
    if name in animal_dict:
        animal = animal_dict.pop(name)
        
        # Remove from indexes
        remove_animal_from_indexes(animal, animal_type)
        
        print(f"Animal '{name}' has been deleted.")
    else:
        print(f"No animal found with the name '{name}'.")

def delete_dog():
    name = input("Enter the name of the dog to delete: ")
    delete_animal(name, dog_dict, "dog")

def delete_monkey():
    name = input("Enter the name of the monkey to delete: ")
    delete_animal(name, monkey_dict, "monkey")

def delete_bird():
    name = input("Enter the name of the bird to delete: ")
    delete_animal(name, bird_dict, "bird")

def delete_reptile():
    name = input("Enter the name of the reptile to delete: ")
    delete_animal(name, reptile_dict, "reptile")


# Main function to run the program
def main():
    # Initialize the dictionaries with some predefined animals
    initialize_dog_list()
    initialize_monkey_list()
    initialize_bird_list()
    initialize_reptile_list()

    while True:
        # Display the main menu options
        display_main_menu()
        try:
            # Get the user's menu selection
            option = int(input())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        if option == 1:
            # Display the intake sub-menu options
            while True:
                display_intake_sub_menu()
                try:
                    sub_option = int(input())
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 5.")
                    continue

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
                else:
                    print("Invalid menu choice. Please try again...")

        elif option == 2:
            # Display the lookup sub-menu options
            while True:
                display_lookup_sub_menu()
                try:
                    sub_option = int(input())
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 5.")
                    continue

                if sub_option == 1:
                    look_up_animal_by_name(input("Enter the name of the dog to look up: "))
                elif sub_option == 2:
                    look_up_animal_by_name(input("Enter the name of the monkey to look up: "))
                elif sub_option == 3:
                    look_up_animal_by_name(input("Enter the name of the bird to look up: "))
                elif sub_option == 4:
                    look_up_animal_by_name(input("Enter the name of the reptile to look up: "))
                elif sub_option == 5:
                    break
                else:
                    print("Invalid menu choice. Please try again...")

        elif option == 3:
            # Display the print sub-menu options
            while True:
                display_print_sub_menu()
                try:
                    sub_option = int(input())
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 6.")
                    continue

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
                else:
                    print("Invalid menu choice. Please try again...")

        elif option == 4:
            reserve_animal()

        elif option == 5:
            # Display the delete sub-menu options
            while True:
                display_delete_sub_menu()
                try:
                    sub_option = int(input())
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 5.")
                    continue

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
                else:
                    print("Invalid menu choice. Please try again...")

        elif option == 6:
            print("You Exited the application. Good Bye!!!")
            break
        else:
            print("Invalid menu choice. Please try again...")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
