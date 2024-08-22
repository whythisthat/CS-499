# RescueAnimal.py

# Base class for all rescue animals
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

# Subclass for dogs
class Dog(RescueAnimal):
    pass

# Subclass for monkeys
class Monkey(RescueAnimal):
    pass

# Subclass for birds
class Bird(RescueAnimal):
    pass

# Subclass for reptiles
class Reptile(RescueAnimal):
    pass
