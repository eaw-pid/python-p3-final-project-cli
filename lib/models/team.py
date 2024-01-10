from models.__init__ import CURSOR, CONN

class Team:
    
    all = {}

    def __init__(self, name, color, mascot, id=None):
        self.name = name
        self.color = color
        self.mascot = mascot
    
    def __repr__(self):
        return f"<Team: {self.name}, Color: {self.color}, Mascot: {self.mascot}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) is str and len(name):
            self._name = name
        else:
            raise Exception('Name must be a non empty string!')
    
    @property
    def color(self):
        return self._color 
    
    @color.setter
    def color(self, color):
        if type(color) is str and len(color):
            self._color = color
        else:
            raise Exception('Color must be a non empty string!')

    @property
    def mascot(self):
        return self._mascot
    
    @mascot.setter
    def mascot(self, mascot):
        if type(mascot) is str and len(mascot):
            self._mascot = mascot
        else:
            raise Exception('Mascot must be a non empty string!')

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Team instances """
        sql = """
            CREATE TABLE IF NOT EXISTS teams (
                id INTEGER PRIMARY KEY,
                name TEXT,
                color TEXT,
                mascot TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Team instances """
        sql = """
            DROP TABLE IF EXISTS teams;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """Insert a new row with the name and location valueso f the current Team instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO teams (name, color, mascot)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.color, self.mascot))
        CONN.commit()

        self.id - CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(self, name, color, mascot):
        """Initialize a new Team instance and save the obj to database"""
        team = cls(name, color, mascot)
        team.save()
        return team
    
    def update(self):
        """Update a table row corresponding to the current Team instance."""
        sql = """
            UPDATE teams
            SET name = ?, color = ?, mascot = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.color, self.mascot))
        CONN.commit()
    
    def delete(self):
        """Delete the table row corresponding to the current Department instance,
        delete the dictionary entry, and reassing id attribute"""
        sql = """
            DELETE from teams
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        #Delete the dictionary using id as key
        del type(self).all[self.id]

        #Set the id to None
        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a Team obj having the attribute values form the table row."""

        #Check the dictionary for an existing instance using the row's primary key
        team = cls.all.get(row[0])
        if team:
            #ensure attributes match row values in case local instance was modified
            team.name = row[1]
            team.color = row[2]
            team.mascot = row[3]
        else:
            #not in dictionary, create a new instance and add to dictionary
            team = cls(row[1], row[2], row[3])
            team.id = row[0]
            cls.all[team.id] = team
        return team
    
    @classmethod
    def get_all(cls):
        """Return a list containing a Team object per row in the table"""
        sql = """
            SELECT *
            FROM teams
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        """Return a Team  object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM teams
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def players(self):
        """Return list of players associated with current department"""
        from models.player import Player
        sql = """
            SELECT * FROM players
            WHERE department_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [Player.instance_from_db(row) for row in rows]
































# from __init__ import CURSOR, CONN
# import re


# class Job:

#     all = []

#     def __init__(self, family, sitter, date):
#         self.family = family
#         self.sitter = sitter
#         self.data = date
#         type(self).all.append(self)
    
#     @property
#     def family(self):
#         return self._family
    
#     @family.setter
#     def family(self, family):
#         if isinstance(family, Family):
#             self._family = family
#         else:
#             raise Exception('Family must be a family object!')

#     @property
#     def sitter(self):
#         return self._sitter
    
#     @sitter.setter
#     def sitter(self, sitter):
#         if isinstance(sitter, Sitter):
#             self._sitter = sitter
#         else:
#             raise Exception('Sitter my a sitter object!')
    
#     @property
#     def date(self):
#         return self._date

#     @date.setter
#     def date(self, date):
#         ##Define the regex pattern
#         pattern = r"\d{2}/\d{2}/\d{4}"

#         if re.match(pattern, date) and type(date) is str:
#             self._date = date
#         else:
#             raise Exception("Date must be in format '02/04/2024!'")