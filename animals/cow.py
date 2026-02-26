# animals/cow.py
from animals.base import Animal
import random

class Cow(Animal):
    def produce(self):
        if self.alive and self.energy > 30:
            milk = random.randint(5, 10)
            self.energy -= 20
            return {"milk": milk}
        return {"milk": 0}

    def reproduce(self, partner):
        if self.alive and partner.alive and self.gender=="female" and partner.gender=="male" and not self.is_pregnant and self.energy>70:
            self.is_pregnant = True
            self.pregnancy_days = 3
            return True
        return False