class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def info(self):
        return f"이름: {self.name}, 품종: {self.breed}"
