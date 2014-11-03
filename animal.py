class Animal:
    def __init__(self, species, age, name, gender, weight, life_expectancy):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.is_alive = True
        self.life_expectancy = life_expectancy

    def grow(self, weight, days):
        self.weight += weight
        self.age += days

    def eat(self, food):
        self.weight += food

    def dying(self):
        if self.is_alive:
            self.is_alive = False

    def chance_of_dying(self):
        return((self.age // 365) / self.life_expectancy)
