from __init__ import CURSOR, CONN
import re


class Job:

    all = []

    def __init__(self, family, sitter, date):
        self.family = family
        self.sitter = sitter
        self.data = date
        type(self).all.append(self)
    
    @property
    def family(self):
        return self._family
    
    @family.setter
    def family(self, family):
        if isinstance(family, Family):
            self._family = family
        else:
            raise Exception('Family must be a family object!')

    @property
    def sitter(self):
        return self._sitter
    
    @sitter.setter
    def sitter(self, sitter):
        if isinstance(sitter, Sitter):
            self._sitter = sitter
        else:
            raise Exception('Sitter my a sitter object!')
    
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        ##Define the regex pattern
        pattern = r"\d{2}/\d{2}/\d{4}"

        if re.match(pattern, date) and type(date) is str:
            self._date = date
        else:
            raise Exception("Date must be in format '02/04/2024!'")