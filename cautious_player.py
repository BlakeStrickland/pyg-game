import random
from player import Player

class CautiousPlayer(Player):
    def __init__(self):
        super().__init__()
        self.aggression_level = 25

    def play_again(self):
        return random.getrandbits(1)
