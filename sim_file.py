from game import *
from player import *
from medium_player import *
from aggressive_player import *
from cautious_player import *


times_to_play = 1

mp_wins = 0
ap_wins = 0
score_tuple_list = []

while times_to_play < 1000:
    game = Game().main()
    if game[0] == game[1]:
        mp_wins += 1
        ap_wins += 1
    elif game[0] > game[1]:
        mp_wins += 1
    else:
        ap_wins += 1
    print(game)
    score_tuple_list.append(game)
    times_to_play += 1

if mp_wins > ap_wins:
    print("mp_wins")
else:
    print("ap_wins")
