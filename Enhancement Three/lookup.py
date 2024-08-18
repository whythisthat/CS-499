# lookup.py

# Import necessary indexes
from animal_index import name_index, type_index

# Function to look up an animal by name
def look_up_animal_by_name(name):
    if name in name_index:
        print(name_index[name])
    else:
        print(f"No animal found with the name '{name}'.")

# Function to look up animals by type
def look_up_animals_by_type(animal_type):
    if animal_type in type_index:
        animals = list(type_index[animal_type].values())
        sorted_animals = quick_sort(animals, key='name')
        for animal in sorted_animals:
            print(animal)
    else:
        print(f"No animals of type '{animal_type}' found.")

# Quick sort function
def quick_sort(arr, key):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x[key] < pivot[key]]
        middle = [x for x in arr if x[key] == pivot[key]]
        right = [x for x in arr if x[key] > pivot[key]]
        return quick_sort(left, key) + middle + quick_sort(right, key)
