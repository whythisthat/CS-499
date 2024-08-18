# intake.py

# Import necessary classes and functions
from RescueAnimal import Dog, Monkey, Bird, Reptile
from animal_index import add_animal_to_indexes

# Initialize dictionaries to store each type of animal
dog_dict = {}
monkey_dict = {}
bird_dict = {}
reptile_dict = {}

# Generic function to intake a new animal
def intake_new_animal(animal_class, animal_dict, animal_type):
    name = input(f"What is the {animal_type}'s name? ")
    a_type = input(f"What is the {animal_type}'s species type? ")
    if name in animal_dict and animal_dict[name].animal_type.lower() == a_type.lower():
        print(f"\n\nThis {animal_type} is already in our system\n\n")
        return
    gender = input(f"Enter the {animal_type}'s gender: ")
    age = input(f"Enter the {animal_type}'s age: ")
    weight = input(f"Enter the {animal_type}'s weight: ")
    a_date = input(f"Enter the {animal_type}'s acquisition date: ")
    a_country = input(f"Enter the {animal_type}'s acquisition country: ")
    status = input(f"Enter the {animal_type}'s training status: ")
    reserved = input(f"Enter the {animal_type}'s reserved status (true/false): ").lower() == 'true'
    ser_country = input(f"Enter the {animal_type}'s in service country name: ")
    animal = animal_class(name, a_type, gender, age, weight, a_date, a_country, status, reserved, ser_country)
    animal_dict[name] = animal
    add_animal_to_indexes(animal, animal_type)

# Specific functions to intake each animal type
def intake_new_dog():
    intake_new_animal(Dog, dog_dict, "dog")

def intake_new_monkey():
    intake_new_animal(Monkey, monkey_dict, "monkey")

def intake_new_bird():
    intake_new_animal(Bird, bird_dict, "bird")

def intake_new_reptile():
    intake_new_animal(Reptile, reptile_dict, "reptile")

# Initialize functions for each animal type
def initialize_dog_list():
    dogs = [
        Dog("Spot", "German Shepherd", "male", "1", "25.6", "05-12-2019", "United States", "intake", False, "United States"),
        Dog("Rex", "Great Dane", "male", "3", "35.2", "02-03-2020", "United States", "Phase I", False, "United States"),
        Dog("Bella", "Chihuahua", "female", "4", "25.6", "12-12-2019", "Canada", "in service", True, "Canada")
    ]
    for dog in dogs:
        dog_dict[dog.name] = dog
        add_animal_to_indexes(dog, "dog")

def initialize_monkey_list():
    monkeys = [
        Monkey("Mony", "Capuchin Monkey", "male", "1", "9", "04-12-2019", "United States", "intake", False, "United States"),
        Monkey("Rexon", "Squirrel Monkey", "male", "5", "18.4", "02-03-2020", "United States", "intake", False, "United States"),
        Monkey("Della", "Spider Monkey", "female", "6", "25.6", "12-12-2019", "Canada", "in service", False, "Canada")
    ]
    for monkey in monkeys:
        monkey_dict[monkey.name] = monkey
        add_animal_to_indexes(monkey, "monkey")

def initialize_bird_list():
    birds = [
        Bird("Tweety", "Parrot", "female", "2", "0.5", "01-10-2021", "Australia", "intake", False, "Australia"),
        Bird("Sky", "Sparrow", "male", "1", "0.2", "11-11-2020", "United States", "Phase I", False, "United States")
    ]
    for bird in birds:
        bird_dict[bird.name] = bird
        add_animal_to_indexes(bird, "bird")

def initialize_reptile_list():
    reptiles = [
        Reptile("Slinky", "Iguana", "male", "3", "1.5", "07-12-2019", "Brazil", "in service", False, "Brazil"),
        Reptile("Creepy", "Snake", "female", "4", "2.1", "03-04-2020", "India", "Phase II", False, "India")
    ]
    for reptile in reptiles:
        reptile_dict[reptile.name] = reptile
        add_animal_to_indexes(reptile, "reptile")
