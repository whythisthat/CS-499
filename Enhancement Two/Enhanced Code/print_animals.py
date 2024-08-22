# print_animals.py

# Import necessary dictionaries from intake module
from intake import dog_dict, monkey_dict, bird_dict, reptile_dict

# Generic function to print animals, sorted by name
def print_animals(animal_dict, animal_type):
    print(f"{animal_type.capitalize()} Details")
    print("-----------------------------------")
    for animal in sorted(animal_dict.values(), key=lambda x: x.name):
        print(animal)

# Function to print all dogs
def print_dogs():
    print_animals(dog_dict, "dog")

# Function to print all monkeys
def print_monkeys():
    print_animals(monkey_dict, "monkey")

# Function to print all birds
def print_birds():
    print_animals(bird_dict, "bird")

# Function to print all reptiles
def print_reptiles():
    print_animals(reptile_dict, "reptile")

# Function to print all available animals (not reserved and in service), sorted by name
def print_available_animals():
    print("Displaying all Available Animals")
    print("-----------------------------------")
    available_animals = [
        animal for animal_dict in [dog_dict, monkey_dict, bird_dict, reptile_dict]
        for animal in animal_dict.values()
        if not animal.reserved and animal.training_status.lower() == "in service"
    ]
    for animal in sorted(available_animals, key=lambda x: x.name):
        print(animal)
