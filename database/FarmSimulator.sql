create database FarmSimulator
-------------------------------------

-- Players table
CREATE TABLE Players (
    player_id INT PRIMARY KEY IDENTITY(1,1),
    username NVARCHAR(50) UNIQUE,
    password_hash NVARCHAR(256),
    current_farm_id INT
);

-- Farms table
CREATE TABLE Farms (
    farm_id INT PRIMARY KEY IDENTITY(1,1),
    player_id INT FOREIGN KEY REFERENCES Players(player_id),
    money FLOAT,
    food FLOAT,
    barn_level INT,
    day INT
);

-- Animals table
CREATE TABLE Animals (
    animal_id INT PRIMARY KEY IDENTITY(1,1),
    farm_id INT FOREIGN KEY REFERENCES Farms(farm_id),
    type NVARCHAR(50),
    name NVARCHAR(50),
    age INT,
    gender NVARCHAR(10),
    energy INT,
    hunger INT,
    health INT,
    is_pregnant BIT,
    pregnancy_days INT
);

-- Market table
CREATE TABLE MarketHistory (
    day INT,
    milk_price FLOAT,
    egg_price FLOAT,
    cow_price FLOAT
);