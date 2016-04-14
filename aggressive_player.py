import random
from player import Player

class AggressivePlayer(Player):
    def __init__(self):
        super().__init__()
        self.aggression_level = 75

    def play_again(self):
        return random.getrandbits(1)
