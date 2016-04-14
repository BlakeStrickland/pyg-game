from player import Player
from medium_player import MediumPlayer
from aggressive_player import AggressivePlayer
from cautious_player import CautiousPlayer

class Game():
    def __init__(self):
        self.turn_limit = 7
        self.turn_count = 0

    def player_rolls(self, player):
        player.take_a_turn(self.turn_count)

    def main(self):
        player = MediumPlayer()
        player2 = AggressivePlayer()

        while self.turn_count < self.turn_limit and player.score < 100 and player2.score < 100:
            self.player_rolls(player)
            self.player_rolls(player2)


        # print("Final scores are: \n CP: {}\n AP: {}".format(player2.score, player.score))
        return (player.score, player2.score)

if __name__ == "__main__":
    game = Game()
    game.main()
