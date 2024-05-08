# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
from itertools import product

def player(prev_play, opponent_history=[], my_history=[], variations = {"".join(var): 0 for var in product(["P", "S", "R"], repeat=6)}):

    best_choices = {'R' : 'P', 'P' : 'S', 'S' : 'R'}

    #if there is no enough data just play random
    if (prev_play == "") or (len(opponent_history) < 15):
        guess = random.choice(['R', 'S', 'P'])
        if prev_play != "":
            opponent_history.append(prev_play)
        my_history.append(guess)
        return guess

    opponent_history.append(prev_play)

    variations[my_history[-4] + opponent_history[-3] + my_history[-3] + opponent_history[-2] + my_history[-2] + opponent_history[-1] ]  += 1

    s_keys = [key for key in variations.keys() if key.startswith(my_history[-3] + opponent_history[-2] + my_history[-2] + opponent_history[-1] + my_history[-1] )]
    max_key = max(s_keys, key=lambda k: variations[k])
    guess = best_choices[max_key[-1]]
    my_history.append(guess)
    #print('-------------')
    #print(max_key)
    #print(variations[max_key])

    return guess


