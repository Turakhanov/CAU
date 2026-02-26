# animals/base.py
from abc import ABC, abstractmethod
import random

class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.energy = 100
        self.hunger = 0
        self.health = 100
        self.alive = True
        self.is_pregnant = False
        self.pregnancy_days = 0

    def feed(self, amount):
        self.hunger = max(0, self.hunger - amount)
        self.energy = min(100, self.energy + 10)

    def daily_decay(self):
        self.hunger += 10
        self.energy -= 5
        if self.hunger > 100:
            self.health -= 20
        if self.health <= 0:
            self.alive = False

    def handle_pregnancy(self):
        if self.is_pregnant:
            self.pregnancy_days -= 1
            if self.pregnancy_days <= 0:
                self.is_pregnant = False
                return self.__class__(name=f"Baby{self.__class__.__name__}", age=0, gender=random.choice(["male", "female"]))
        return None

    @abstractmethod
    def produce(self):
        pass

    @abstractmethod
    def reproduce(self, partner):
        pass