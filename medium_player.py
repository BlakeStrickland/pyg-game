import random
from player import Player

class MediumPlayer(Player):
    def __init__(self):
        super().__init__()
        self.aggression_level = [0, 0, 1, 1]

    def play_again(self):
        return random.getrandbits(1)

    def take_a_turn(self, turn_total=0):
        first_roll = random.randint(1, 6)
        if first_roll == 1:
            return self.score
        else:
            turn_total += first_roll
            if self.play_again() and random.choice(self.aggression_level):
                self.take_a_turn(turn_total)
            else:
                self.score += turn_total
