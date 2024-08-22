# animal_index.py

# Initialize dictionaries to store indexes
name_index = {}
type_index = {
    "dog": {},
    "monkey": {},
    "bird": {},
    "reptile": {}
}

# Function to add animal to indexes
def add_animal_to_indexes(animal, animal_type):
    name_index[animal.name] = animal
    if animal_type not in type_index:
        type_index[animal_type] = {}
    type_index[animal_type][animal.name] = animal

# Function to remove animal from indexes
def remove_animal_from_indexes(animal, animal_type):
    if animal.name in name_index:
        del name_index[animal.name]
    if animal.name in type_index[animal_type]:
        del type_index[animal_type][animal.name]
