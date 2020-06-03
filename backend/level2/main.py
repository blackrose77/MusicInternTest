from parse_json import *
from datetime import datetime

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


def main():
    js = Parse("data/input.json")
    rentals = []
    for rents in js.get_js()["rentals"]:
        start = datetime.strptime(rents["start_date"], '%Y-%m-%d').date()
        end = datetime.strptime(rents["end_date"], '%Y-%m-%d').date()
        days = end - start
        price = get_price(js, days.days + 1, rents["distance"], rents["car_id"])
        rent = ObjectJson(rents["id"], price)
        rentals.append(json.loads(json.dumps(rent.__dict__)))

    res = ToJson(rentals)

    result = json.dumps(res.__dict__, sort_keys = True, indent = 2)
    fp = open("expected_output.json", "w")
    fp.write(result)
    fp.close()

main()



