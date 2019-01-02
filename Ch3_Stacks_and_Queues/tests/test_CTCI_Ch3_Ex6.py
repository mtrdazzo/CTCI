from unittest import TestCase
from CTCI.Ch3_Stacks_and_Queues.exercises.CTCI_Ch3_Ex6 import AnimalShelter, Empty, Cat, Dog


class TestAnimalShelter(TestCase):

    def setUp(self):
        self.A = AnimalShelter()

    def tearDown(self):
        pass

    def test_empty_animal_shelter(self):

        with self.assertRaises(Empty):
            self.A.dequeueCat()

        with self.assertRaises(Empty):
            self.A.dequeueDog()

        with self.assertRaises(Empty):
            self.A.dequeueAny()

    def test_single_animal(self):
        cat = Cat("Kitten")
        dog = Dog("Jessie")

        self.A.enqueue(cat)
        self.assertTrue(self.A.dequeueCat() is cat)

        self.A.enqueue(cat)
        self.assertTrue(self.A.dequeueAny() is cat)

        self.A.enqueue(dog)
        self.assertTrue(self.A.dequeueDog() is dog)

        self.A.enqueue(dog)
        self.assertTrue(self.A.dequeueAny() is dog)

    def test_multiple_animals(self):
        self.A.enqueue(Dog("Jessie"))
        self.A.enqueue(Dog("Tilly"))
        self.A.enqueue(Cat("Turbo"))
        self.A.enqueue(Cat("Kitten"))
        self.A.enqueue(Dog("Mace"))

        self.assertTrue(self.A.dequeueAny().name == "Jessie")
        self.assertTrue(self.A.dequeueCat().name == "Turbo")
        self.assertTrue(self.A.dequeueDog().name == "Tilly")

        self.assertTrue(self.A.dequeueAny().name == "Kitten")

        with self.assertRaises(Empty):
            self.A.dequeueCat()

        self.A.enqueue(Cat("Turbo"))
        self.A.enqueue(Cat("Kitty"))

        self.assertTrue(self.A.dequeueDog().name == "Mace")

        with self.assertRaises(Empty):
            self.A.dequeueDog()

