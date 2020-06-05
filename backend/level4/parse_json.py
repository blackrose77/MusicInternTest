import json 
class Parse:
    def __init__(self, name):
        f = open(name, "r")
        self.js = json.loads(f.read())

    def get_js(self):
        return self.js


class ObjectJson:
    def __init__(self, id, actions):
        self.id = id
        self.actions = actions
    
    def get_id(self):
        return self.id
    
    def get_price(self):
        return self.price
    
class ObjectJsonAction:

    def __init__(self, who, types, amount):
        self.who = who
        self.type = types
        self.amount = amount
    def get_who(self):
        return self.who

class ToJson:
    def __init__(self, rentals):
        self.rentals = rentals
    def get_rentals(self):
        return self.rentals
