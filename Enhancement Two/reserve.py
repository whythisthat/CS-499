# reserve.py

# Import necessary dictionaries
from intake import dog_dict, monkey_dict, bird_dict, reptile_dict

# Function to reserve an animal
def reserve_animal():
    a_type = input("Enter the desired animal type: ")
    country = input("Enter the desired country name: ")

    # Check if any animal of the specified type and country is available for reservation
    for animal_dict in [dog_dict, monkey_dict, bird_dict, reptile_dict]:
        for animal in animal_dict.values():
            if animal.animal_type.lower() == a_type.lower() and animal.in_service_country.lower() == country.lower() and not animal.reserved:
                animal.reserved = True
                print("Animal is reserved successfully")
                return

    print("No animal type and location of your desired choice is available")
