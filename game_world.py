from pyexpat import features
import random

class Game_world:
    def __init__(self, time, weather, obstacles, flags):
        self.time = time
        self.weather = weather
        self.obstacles = obstacles
        self.features = features
        self.flags = flags

class Game_store:
    store_items = {
                     1:{
                        "item": "Extra Food",
                        "price": 10,
                        "use": "Adds 5 points to energy"},
                    2:{
                        "item": "Snow Shoes",
                        "price": 5,
                        "use": "Go faster on land in case of snow storms"},
                    3:{
                        "item": "Lightweight Gear",
                        "price": 10,
                        "use": "Go faster on land and water"},
                    4:{
                        "item": "Firewood & Starter",
                        "price": 10,
                        "use": "Stave off the cold"},
                    5:{
                        "item": "Canoe Cart",
                        "price": 2,
                        "use": "Go faster on land in good weather"
                    }}

    def __init__(self):
        # self.descriptor = descriptor
        # self.sales = sales
        # self.cash = cash
        pass

time_of_day = random.choice(["morning", "afternoon", "night"])
weather = random.choice(["rainy", "snowy", "hot", "beautiful"])

# Lake Louise - Level 1
def level_1(weather, time_of_day):
    num_obs = 3
    num_flags = 5

    lake_louise = Game_world(random.choice(time_of_day),random.choice(weather), num_obs, num_flags)
    print(f"It is a {weather} {time_of_day} on Lake Louise. ")


# Setup weather story descriptions