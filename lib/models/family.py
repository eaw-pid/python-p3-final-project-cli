from __init__ import CURSOR, CONN

class Family:

    zip_codes = [
        13901,
        13903,
        13904,
        13905,
        13850,
        13732,
        ]

    all = []

    def __init__(self, last_name, children, zip_code):
        self.last_name = last_name
        self.children = children
        self.zip_code = zip_code
        type(self).all.append(self)
    
    def __repr__(self):
        return f"<Family: {self.last_name}, Children: {self.children}, Zip:{self.zip_code}>"

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        if type(last_name) is str and len(last_name):
            self._last_name = last_name
        else:
            raise Exception('Last Name must be a non empty string!')
    
    @property
    def children(self):
        return self._children
    
    @children.setter
    def children(self, children):
        if type(children) is int and 0 < children <= 10:
            self._children = children
        else:
            raise Exception('Children must be a number between 1 and 10!')
    
    @property
    def zip_code(self):
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, zip_code):
        if type(zip_code) is int and zip_code in Family.zip_codes:
            self._zip_code = zip_code
        else:
            raise Exception("Zip code must be from the zip_codes list")    

