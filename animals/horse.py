# animals/horse.py
from animals.base import Animal
import random

class Horse(Animal):
    def produce(self):
        """Horses dont produce goods daily, but can be sold for money"""
        return {}

    def reproduce(self, partner):
        """Horses reproduction is slower but more valuable"""
        if (
            self.alive and partner.alive and
            self.gender == "female" and partner.gender == "male" and
            not self.is_pregnant and
            self.energy > 80
        ):
            self.is_pregnant = True
            self.pregnancy_days = 5  # Slower gestation
            return True
        return False