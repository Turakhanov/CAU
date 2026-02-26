def simulate_day(farm, market):
    print("\n--- Simulating a day ---")
    farm.feed_animals()
    new_animals = []
    for animal in farm.animals:
        animal.daily_decay()
        baby = animal.handle_pregnancy()
        if baby:
            print(f"A new {baby.name} was born!")
            farm.add_animal(baby)
    farm.day += 1
    farm.save()
    market.update_prices()
    print("Day complete. Market prices updated.")