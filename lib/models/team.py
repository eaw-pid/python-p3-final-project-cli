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