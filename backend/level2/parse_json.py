import json 
class Parse:
    def __init__(self, name):
        f = open(name, "r")
        self.js = json.loads(f.read())

    def get_js(self):
        return self.js


class ObjectJson:
    def __init__(self, id, price):
        self.id = id
        self.price = price
    
    def get_id(self):
        return self.id
    
    def get_price(self):
        return self.price
    

class ToJson:
    def __init__(self, rentals):
        self.rentals = rentals
    def get_rentals(self):
        return self.rentals
