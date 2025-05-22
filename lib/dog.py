class Dog:
    approved_breeds = ["Pug", "Beagle", "Labrador", "German Shepherd", "Golden Retriever"]

    def __init__(self, name="Fido", breed="Pug"):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
            # Don't print anything here
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in Dog.approved_breeds:
            self._breed = value
            # Don't print anything here
        else:
            print("Breed must be in list of approved breeds.")




