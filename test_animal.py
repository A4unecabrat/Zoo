from animal import Animal
import unittest


class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.cat_animal = Animal("cat", 365, "Pena", "Female", 5, 5475)

    def test_animal_init(self):
        self.assertEqual("cat", self.cat_animal.species)
        self.assertEqual(365, self.cat_animal.age)
        self.assertEqual("Pena", self.cat_animal.name)
        self.assertEqual("Female", self.cat_animal.gender)
        self.assertEqual(5, self.cat_animal.weight)
        self.assertEqual(5475, self.cat_animal.life_expectancy)

    def test_grow(self):
        self.cat_animal.grow(2, 1)
        self.assertEqual(366, self.cat_animal.age)
        self.assertEqual(7, self.cat_animal.weight)

    def test_eat(self):
        self.cat_animal.eat(2)
        self.assertEqual(7, self.cat_animal.weight)

    def test_dying(self):
        self.assertFalse(self.cat_animal.dying())

if __name__ == '__main__':
    unittest.main()
