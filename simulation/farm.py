from database.queries import save_farm, update_farm, save_animal, load_animals

class Farm:
    def __init__(self, player_id, money=1000, food=500, barn_level=1, day=1, farm_id=None):
        self.player_id = player_id
        self.money = money
        self.food = food
        self.barn_level = barn_level
        self.day = day
        if farm_id:
            self.farm_id = farm_id
            self.animals = load_animals(farm_id)
        else:
            self.animals = []
            self.farm_id = save_farm(self)

    def feed_animals(self):
        for animal in self.animals:
            if self.food >= 5:
                animal.feed(20)
                self.food -= 5
                if hasattr(animal, "animal_id"):
                    save_animal(self.farm_id, animal)  # Save new animal if not already saved

    def add_animal(self, animal):
        self.animals.append(animal)
        save_animal(self.farm_id, animal)

    def save(self):
        update_farm(self)
        for animal in self.animals:
            if hasattr(animal, "animal_id"):
                # update if already exists
                from database.queries import update_animal
                update_animal(animal.animal_id, animal)
            else:
                save_animal(self.farm_id, animal)