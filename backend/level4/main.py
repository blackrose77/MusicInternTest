from parse_json import *
from datetime import datetime
from collections import OrderedDict

def get_price(js, days, distance, car_id):

    price_days = 0
    for cars in js.get_js()["cars"]:
        if (car_id == cars["id"]):
        
            for i in range(1, days + 1):
                if (i > 10):
                    price_day = cars["price_per_day"] - (cars["price_per_day"] * 50) / 100
                    price_days = price_days + price_day
                    continue
                elif (i > 4):
                    price_day = cars["price_per_day"] - (cars["price_per_day"] * 30) / 100
                    price_days = price_days + price_day
                    continue
                elif (i > 1):
                    price_day = cars["price_per_day"] - (cars["price_per_day"] * 10) / 100
                    price_days = price_days + price_day
                    continue
                else:
                    price_days = price_days + cars["price_per_day"] 

            #price_day = days * cars["price_per_day"]
            price_km = distance * cars["price_per_km"]
            return price_days + price_km



def parse_action(who, types, amount):
    action = ObjectJsonAction(who, types, amount)
    return json.loads(json.dumps(action.__dict__, sort_keys = False))

def get_actions(days, price):
    actions = []
    commission = price * 30 / 100
    insurance = commission / 2
    assistance = 100 * days
    drivy = insurance - assistance
    action1 = parse_action("driver", "debit", price)
    action2 = parse_action("owner", "credit", price - commission)
    action3 = parse_action("insurance", "credit", insurance)
    action4 = parse_action("assistance", "credit", assistance)
    action5 = parse_action("drivy", "credit", drivy)
    
    actions.append(action1)
    actions.append(action2)
    actions.append(action3)
    actions.append(action4)
    actions.append(action5)
    return actions

def main():
    js = Parse("data/input.json")
    rentals = []
    for rents in js.get_js()["rentals"]:
        start = datetime.strptime(rents["start_date"], '%Y-%m-%d').date()
        end = datetime.strptime(rents["end_date"], '%Y-%m-%d').date()
        days = end - start
        price = get_price(js, days.days + 1, rents["distance"], rents["car_id"])
        actions = get_actions(days.days + 1, price)
        rent = ObjectJson(rents["id"], actions)
        rentals.append(json.loads(json.dumps(rent.__dict__)))

    res = ToJson(rentals)

    result = json.dumps(res.__dict__, sort_keys = False, indent = 2)
 
    fp = open("expected_output.json", "w")
    fp.write(result)
    fp.close()

main()



