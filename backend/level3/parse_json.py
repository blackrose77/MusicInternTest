import json 
class Parse:
    def __init__(self, name):
        f = open(name, "r")
        self.js = json.loads(f.read())

    def get_js(self):
        return self.js


class ObjectJson:
    def __init__(self, id, price, commission):
        self.id = id
        self.price = price
        self.commission = commission
    
    def get_id(self):
        return self.id
    
    def get_price(self):
        return self.price
    
class ObjectJsonCommission:

    def __init__(self, insurance, assistance, drivy):
        self.insurance_fee = insurance
        self.assistance_fee = assistance
        self.drivy_fee = drivy
    def get_insurance(self):
        return self.insurance_fee

class ToJson:
    def __init__(self, rentals):
        self.rentals = rentals
    def get_rentals(self):
        return self.rentals
