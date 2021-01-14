DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;
DROP TABLE IF EXISTS position;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    team_name TEXT UNIQUE NOT NULL,
    points FLOAT NOT NULL
);

CREATE TABLE player (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    team_id INTEGER NOT NULL,
    position_id INTEGER NOT NULL,
    kills INTEGER NOT NULL,
    deaths INTEGER NOT NULL,
    assists INTEGER NOT NULL,
    average_cs FLOAT NOT NULL,
    triple_kills INTEGER NOT NULL,
    quadra_kills INTEGER NOT NULL,
    penta_kills INTEGER NOT NULL,
    total_points FLOAT NOT NULL,
    owner_id INTEGER,
    FOREIGN KEY (team_id) REFERENCES team (id),
    FOREIGN KEY (position_id) REFERENCES position (id),
    FOREIGN KEY (owner_id) REFERENCES user (id)
);

CREATE TABLE team (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    owner_id INTEGER,
    wins INTEGER NOT NULL,
    losses INTEGER NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES user (id)
)

CREATE TABLE position (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    position TEXT NOT NULL
);