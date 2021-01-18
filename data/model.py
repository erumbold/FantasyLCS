import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('flcs.db')
        self.create_team_table()
        self.create_user_table()
        self.create_player_table()
        self.create_position_table()

    def create_player_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Player" (
        id INTEGER PRIMARY KEY,
        PlayerName TEXT,
        OwnerId INTEGER FOREIGN KEY REFERENCES User(id)
        TeamId INTEGER FOREIGN KEY REFERENCES Team(id),
        PositionId INTEGER FOREIGN KEY REFERENCES Position(id),
        Kills INTEGER,
        Deaths INTEGER,
        Assists INTEGER,
        AvgCS FLOAT,
        TripleKills INTEGER,
        QuadraKills INTEGER,
        PentaKills INTEGER,
        SplitPoints FLOAT
        );
        """
        self.conn.execute(query)

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "User" (
        id INTEGER PRIMARY KEY,
        UserName TEXT,
        TeamName TEXT,
        Points FLOAT,
        Wins INTEGER,
        Losses INTEGER,
        Ties INTEGER
        );
        """
        self.conn.execute(query)

    def create_team_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Team" (
        id INTEGER PRIMARY KEY,
        TeamName TEXT,
        Abbreviation TEXT,
        Wins INTEGER,
        Loses INTEGER,
        OwnerId INTEGER FOREIGN KEY REFERENECES User(id)
        );
        """
        self.conn.execute(query)

    def create_position_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Position" (
        id INTEGER PRIMARY KEY,
        Position TEXT
        ); 
        """
        self.conn.execute(query)

    def create_league_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "League" (
        id INTEGER PRIMARY KEY,
        Name TEXT NOT NULL
        );
        """
        self.conn.execute(query)

    def create_league_to_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "LeagueToUser" (
        LeagueId INTEGER NOT NULL,
        UserId INTEGER NOT NULL
        );
        """
        self.conn.execute(query)