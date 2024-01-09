from __init__ import CURSOR, CONN

class Sitter:

    zip_codes = [
        13901,
        13903,
        13904,
        13905,
        13850,
        13732,
        ]

    all = []

    def __init__(self, name, zip_code, rate):
        self.name = name
        self.zip_code = zip_code
        self.rate = rate

    def __repr__(self):
        return f"<Name: {self.name}, Zip:{self.zip_code}, Rate: {self.rate}>"

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if type(name) is str and len(name):
            self._name = name
        else:
            raise Exception("Name must be a non-empty string!")
    
    @property
    def zip_code(self):
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, zip_code):
        if type(zip_code) is int and zip_code in Sitter.zip_codes:
            self._zip_code = zip_code
        else:
            raise Exception("Zip code must be from the zip_codes list")
    
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        if type(rate) is int and 1 <= rate <= 40:
            self._rate = rate
        else:
            raise Exception("Rate must be an integer between 1 and 40")
    

