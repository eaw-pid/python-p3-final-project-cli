from models.__init__ import CURSOR, CONN

class Player:

    positions = ['Goalie', 'Center', 'Winger' 'Defense']
    
    all = {}

    def __init__(self, name, age, position, team_id, id=None):
        self.name = name
        self.age = age
        self.position = position
        

    def __repr__(self):
        return (
            f"<Player: {self.name}, Age: {self.age}, Position: {self.position}, " +
            f"Team ID: {self.team_id}>")

    @property
    def name(self):
        return name._self
    
    @name.setter
    def name(self, name):
        if type(name) is str and len(name):
            self._name = name
        else:
            raise Exception('Name must be a non empty string!')
    
    @property
    def age(self):
        return age._self
    
    @age.setter
    def age(self, age):
        if type(age) is int and 10 <= age <= 15:
            self._age = age
        else:
            raise Exception('Age must be an int between 10 and 15!')

    @property
    def position(self):
        return position._self
    
    @position.setter
    def position(self, position):
        if type(position) is str and position in Player.positions:
            self._position = position
        else:
            raise Exception('Position must be an approved position!')
    
    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, team_id):
        if type(team_id) is int and Team.find_by_id(team_id):
            self._team_id = team_id 
        else:
            raise Exception('team_id must reference a team from the database')
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of a Player instance """
        sql = """
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                position TEXT,
                team_id INTEGER,
                FOREIGN KEY (team_id) REFERENCES teams(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Player instances """
        sql = """
            DROP TABLE IS EXISTS players;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """ Insert a new row with the name, age, position, and team_id values of the current Player object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionay key"""
        sql = """
            INSERT INTO players (name, age, position, team_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.age, self.position, self.team_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):
        """Update the table row corresponding to the current Player instance."""
        sql = """
            UPDATE players
            SET name = ?, age = ?, position = ?, team_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.age, self.position, self.team_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Player instance, 
        delete the dictionay entry, and reassing id attribute"""
        sql = """
            DELETE FROM players
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        #Delete from dictionary using id as the key
        del type(self).all[self.id]

        #Set id to None
        self.id = None
    
    @classmethod
    def create(cls, name, age, position, team_id):
        """Initialize a new Player instance and save the object to the database"""
        player = cls(name, age, position, team_id)
        player.save()
        return player
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a Player object having the attribute values from the table row."""

        #Check the dictionary for existing instances using the row's primary key
        player = cls.all.get(row[0])
        if player:
            #make sure attributes match the row values in case local instance was modified
            player.name = row[1]
            player.age = row[2]
            player.position = row[3]
            player.team_id = row[4]
        else:
            #not in the dictionary, create a new instance adn add to dictionary
            player = cls(row[1], row[2], row[3], row[4])
            player.id = row[0]
            cls.all[player.id] = player
        return player
    
    @classmethod
    def get_all(cls):
        """Return a list with one Player object per row"""
        sql = """
            SELECT *
            FROM players
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        """Return Player object corresponding to first table row matching specified name"""
        sql = """
            SELECT * 
            FROM players
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_position(cls, position):
        """Return Player objects matching specified position"""
        sql = """
            SELECT *
            FROM players
            WHERE position is ?
        """
        rows = CURSOR.execute(sql, (position,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
        






















# from __init__ import CURSOR, CONN

# class Family:

#     zip_codes = [
#         13901,
#         13903,
#         13904,
#         13905,
#         13850,
#         13732,
#         ]

#     all = []

#     def __init__(self, last_name, children, zip_code):
#         self.last_name = last_name
#         self.children = children
#         self.zip_code = zip_code
#         type(self).all.append(self)
    
#     def __repr__(self):
#         return f"<Family: {self.last_name}, Children: {self.children}, Zip:{self.zip_code}>"

#     @property
#     def last_name(self):
#         return self._last_name
    
#     @last_name.setter
#     def last_name(self, last_name):
#         if type(last_name) is str and len(last_name):
#             self._last_name = last_name
#         else:
#             raise Exception('Last Name must be a non empty string!')
    
#     @property
#     def children(self):
#         return self._children
    
#     @children.setter
#     def children(self, children):
#         if type(children) is int and 0 < children <= 10:
#             self._children = children
#         else:
#             raise Exception('Children must be a number between 1 and 10!')
    
#     @property
#     def zip_code(self):
#         return self._zip_code
    
#     @zip_code.setter
#     def zip_code(self, zip_code):
#         if type(zip_code) is int and zip_code in Family.zip_codes:
#             self._zip_code = zip_code
#         else:
#             raise Exception("Zip code must be from the zip_codes list")    

