
import random
class Player:
    
    def __init__(self, name, happy, sad, canoe, skill):
        # Player Attributes
        luck = random.randint(0,5)
        self.player_name = name
        self.player_happy = happy
        self.player_sad = sad
        self.player_energy = 20
        self.player_luck = luck
        self.player_canoe = canoe
        self.player_skill = skill
