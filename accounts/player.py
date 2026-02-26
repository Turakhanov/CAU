from database.queries import execute_query, fetch_one, save_farm, load_animals

class Player:
    def __init__(self, player_id, username, farm_id):
        self.player_id = player_id
        self.username = username
        self.farm_id = farm_id
        self.farm = None

    @staticmethod
    def signup(username, password):
        # Save password as-is
        execute_query(
            "INSERT INTO Players (username, password_hash) VALUES (?, ?)",
            (username, password)
        )
        print(f"Account {username} created!")

    @staticmethod
    def login(username, password):
        row = fetch_one(
            "SELECT player_id, password_hash, current_farm_id FROM Players WHERE username = ?",
            (username,)
        )
        if row and row.password_hash == password:  # Compare directly
            player = Player(row.player_id, username, row.current_farm_id)
            from simulation.farm import Farm
            if row.current_farm_id is None:
                farm = Farm(player_id=player.player_id)
                player.farm_id = farm.farm_id
                player.farm = farm
            else:
                farm = Farm(player_id=player.player_id, farm_id=row.current_farm_id)
                player.farm = farm
            print(f"Login successful! Welcome {username}")
            return player
        else:
            print("Login failed!")
            return None