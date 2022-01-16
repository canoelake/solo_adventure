class Player:
    
    def __init__(self, name, happy, sad, pack, skill):
        # Player Attributes
        self.player_name = name
        self.player_happy = happy
        self.player_sad = sad
        self.player_energy = 20
        self.player_health = 20
        # Player tools
        self.player_pack = ['Compass', pack]
        self.player_skill = skill
        self.player_wallet = 10
