# database/queries.py
from connection import get_connection

def execute_query(query, params=()):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def fetch_one(query, params=()):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    row = cursor.fetchone()
    conn.close()
    return row

def fetch_all(query, params=()):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows

# -----------------------------
# New helpers for Farm & Animals
# -----------------------------
def save_farm(farm):
    execute_query("""
        INSERT INTO Farms (player_id, money, food, barn_level, day) 
        VALUES (?, ?, ?, ?, ?)
    """, (farm.player_id, farm.money, farm.food, farm.barn_level, farm.day))
    # Fetch the ID of the inserted farm
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(farm_id) FROM Farms WHERE player_id = ?", (farm.player_id,))
    farm_id = cursor.fetchone()[0]
    conn.close()
    return farm_id

def update_farm(farm):
    execute_query("""
        UPDATE Farms SET money=?, food=?, barn_level=?, day=?
        WHERE farm_id=?
    """, (farm.money, farm.food, farm.barn_level, farm.day, farm.farm_id))

def save_animal(farm_id, animal):
    execute_query("""
        INSERT INTO Animals
        (farm_id, type, name, age, gender, energy, hunger, health, is_pregnant, pregnancy_days)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        farm_id,
        type(animal).__name__,
        animal.name,
        animal.age,
        animal.gender,
        animal.energy,
        animal.hunger,
        animal.health,
        int(animal.is_pregnant),
        animal.pregnancy_days
    ))

def update_animal(animal_id, animal):
    execute_query("""
        UPDATE Animals SET age=?, energy=?, hunger=?, health=?, is_pregnant=?, pregnancy_days=?
        WHERE animal_id=?
    """, (
        animal.age,
        animal.energy,
        animal.hunger,
        animal.health,
        int(animal.is_pregnant),
        animal.pregnancy_days,
        animal_id
    ))

def load_animals(farm_id):
    from animals.cow import Cow
    from animals.chicken import Chicken
    from animals.horse import Horse

    cls_map = {"Cow": Cow, "Chicken": Chicken, "Horse": Horse}
    rows = fetch_all("SELECT * FROM Animals WHERE farm_id=?", (farm_id,))
    animals = []
    for r in rows:
        cls = cls_map[r.type]
        animal = cls(r.name, r.age, r.gender)
        animal.energy = r.energy
        animal.hunger = r.hunger
        animal.health = r.health
        animal.is_pregnant = bool(r.is_pregnant)
        animal.pregnancy_days = r.pregnancy_days
        animal.animal_id = r.animal_id  # keep track for updates
        animals.append(animal)
    return animals