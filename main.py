# main.py
from accounts.player import Player
from animals.cow import Cow
from animals.chicken import Chicken
from animals.horse import Horse
from economy.market import Market
from simulation.engine import simulate_day

def main():
    print("=== Welcome to Farm Simulator ===")
    choice = input("Do you want to [1] Sign Up or [2] Login? ")
    username = input("Username: ")
    password = input("Password: ")

    player = None
    if choice == "1":
        Player.signup(username, password)
        
    else:
        player = Player.login(username, password)

    if not player:
        return

    farm = player.farm
    market = Market()

    # Menu loop
    while True:
        print(f"\nDay {farm.day}")
        print(f"Money: {farm.money} | Food: {farm.food} | Barn level: {farm.barn_level}")
        print("Animals on farm:", [(a.name, type(a).__name__, a.age, a.energy, a.health) for a in farm.animals])
        print("Market prices:", market.prices)

        print("\nActions:")
        print("1. Feed animals")
        print("2. Simulate next day")
        print("3. Buy animal (Cow, Chicken, Horse)")
        print("4. Exit")

        action = input("Choose action: ")

        if action == "1":
            farm.feed_animals()
            print("Animals fed. Food decreased.")
        elif action == "2":
            simulate_day(farm, market)
        elif action == "3":
            animal_type = input("Which animal to buy? (Cow/Chicken/Horse) ")
            if animal_type.lower() == "cow":
                a = Cow("Cow" + str(len(farm.animals)+1), 1, "female")
            elif animal_type.lower() == "chicken":
                a = Chicken("Chicken" + str(len(farm.animals)+1), 1, "female")
            elif animal_type.lower() == "horse":
                a = Horse("Horse" + str(len(farm.animals)+1), 1, "female")
            else:
                print("Unknown animal type")
                continue
            farm.add_animal(a)
            print(f"{a.name} added to farm!")
        elif action == "4":
            print("Exiting game. All data saved to database!")
            farm.save()
            break
        else:
            print("Invalid action")

if __name__ == "__main__":
    main()