import random

class Player():
    def __init__(self):
       self.score = 0

    def roll(self):
       return random.randint(1, 6)

    def take_a_turn(self, turn_total=0):
        first_roll = random.randint(1, 6)
        if first_roll == 1:
            return self.score
        else:
            turn_total += first_roll
            if self.play_again():
                self.take_a_turn(turn_total)
            else:
                self.score += turn_total

    def play_again():
        False
