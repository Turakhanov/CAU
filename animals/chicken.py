# animals/chicken.py
from animals.base import Animal
import random

class Chicken(Animal):
    def produce(self):
        """Produce eggs if alive and has enough energy"""
        if self.alive and self.energy > 20:
            eggs = random.randint(1, 3)
            self.energy -= 10
            return {"eggs": eggs}
        return {"eggs": 0}

    def reproduce(self, partner):
        """Chickens can lay eggs if female and healthy"""
        if (
            self.alive and partner.alive and
            self.gender == "female" and partner.gender == "male" and
            not self.is_pregnant and
            self.energy > 50
        ):
            self.is_pregnant = True
            self.pregnancy_days = 2  # Shorter than cows
            return True
        return False