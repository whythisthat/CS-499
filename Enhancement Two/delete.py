# delete.py

# Import necessary dictionaries and functions
from intake import dog_dict, monkey_dict, bird_dict, reptile_dict
from animal_index import remove_animal_from_indexes

# Function to delete an animal from the dictionary and indexes
def delete_animal(name, animal_dict, animal_type):
    if name in animal_dict:
        animal = animal_dict.pop(name)
        remove_animal_from_indexes(animal, animal_type)
        print(f"Animal '{name}' has been deleted.")
    else:
        print(f"No animal found with the name '{name}'.")

# Generic function to handle deletion based on type
def handle_delete(animal_dict, animal_type):
    name = input(f"Enter the name of the {animal_type} to delete: ")
    delete_animal(name, animal_dict, animal_type)

# Function to delete a dog
def delete_dog():
    handle_delete(dog_dict, "dog")

# Function to delete a monkey
def delete_monkey():
    handle_delete(monkey_dict, "monkey")

# Function to delete a bird
def delete_bird():
    handle_delete(bird_dict, "bird")

# Function to delete a reptile
def delete_reptile():
    handle_delete(reptile_dict, "reptile")
