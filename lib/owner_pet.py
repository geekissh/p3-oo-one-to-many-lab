class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def __repr__(self):
        return f"Pet({self.name}, {self.pet_type}, {self.owner})"

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def pets(self):
        return self.pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")
        pet.owner = self
        self.pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self.pets, key=lambda pet: pet.name)

    def __repr__(self):
        return f"Owner({self.name}, {self.pets})"

Pet.all = []