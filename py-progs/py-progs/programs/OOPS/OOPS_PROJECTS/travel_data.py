class travel_data_n_cost:
    def __init__(self):
        self.travel_famous_places = [
            {"1": "Eiffel Tower", "location_1": "Paris, France", "land": 1000,
                "sea": 700, "air": 300, "hotel": 200, "food": 100, "extra_charges": 50},
            {"2": "Statue of Liberty", "location_2": "New York City, USA", "land": 1200,
                "sea": 800, "air": 500, "hotel": 250, "food": 150, "extra_charges": 60},
            {"3": "Ram Mandir", "location_3": "Uttar Pradesh, India", "land": 800,
                "sea": 500, "air": 400, "hotel": 150, "food": 80, "extra_charges": 40},
            {"4": "Great Wall of China", "location_4": "Beijing, China", "land": 900,
                "sea": 600, "air": 400, "hotel": 180, "food": 90, "extra_charges": 45},
            {"5": "Sydney Opera House", "location_5": "Sydney, Australia", "land": 1100,
                "sea": 750, "air": 550, "hotel": 300, "food": 120, "extra_charges": 70},
            {"6": "Machu Picchu", "location_6": "Cusco Region, Peru", "land": 950,
                "sea": 650, "air": 450, "hotel": 250, "food": 100, "extra_charges": 55},
            {"7": "Colosseum", "location_7": "Rome, Italy", "land": 1000,
                "sea": 700, "air": 500, "hotel": 200, "food": 100, "extra_charges": 50},
            {"8": "Pyramids of Giza", "location_8": "Giza, Egypt", "land": 850,
                "sea": 550, "air": 350, "hotel": 150, "food": 80, "extra_charges": 35},
            {"9": "Petra", "location_9": "Ma'an Governorate, Jordan", "land": 950,
                "sea": 650, "air": 450, "hotel": 250, "food": 120, "extra_charges": 55},
            {"10": "Angkor Wat", "location_10": "Siem Reap, Cambodia", "land": 900,
                "sea": 600, "air": 400, "hotel": 200, "food": 100, "extra_charges": 50}
        ]

        self.months = ["January", "February", "March", "April", "May", "June",
                       "July", "August", "September", "October", "November", "December"]

class cost_calculation:
    def fetch_specific_info(self, travel_data_n_cost, place_name):
        for place in travel_data_n_cost.travel_famous_places:
            if place_name in place.values():
                totalcost = sum(value for key,value in place.items() if isinstance(value, int))
                return place , totalcost
        return None

TD = travel_data_n_cost()
OC = cost_calculation()

# Fetch specific information for a given place name
place_name = input("Enter your location: ")
specific_info = OC.fetch_specific_info(TD, place_name)
if specific_info:
    plan_details , totalcost = specific_info 
    print(f"Information for {place_name}: {plan_details}")
    print(f"the total cost for the location {place_name} trip is: {totalcost} $ only")
else:
    print(f"Information for {place_name} not found.")
    

