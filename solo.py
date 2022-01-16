class Player:
# Holds all characteristics of the player
    def __init__(self):
        # Set up player attributes
        self.player_name = ""
        self.player_happy = ""
        self.player_sad = ""
        self.player_energy = 20
        self.player_health = 20


    def player_tools(self):
        self.player_pack = ["compass"]
        self.player_skill = ""
        self.player_wallet = 10
