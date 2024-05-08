# Rock Paper Scissors

This is the boilerplate for the Rock Paper Scissors project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors

# Player Function Description

In RPS.py file the function, named `player`, is designed to play the game Rock-Paper-Scissors (RPS) against an opponent. It employs a strategy based on analyzing the opponent's previous moves and adapting its own moves accordingly.

## Parameters

- `prev_play`: A string representing the opponent's previous move ("R" for rock, "P" for paper, "S" for scissors), or an empty string if it's the first move.
- `opponent_history`: A list containing the opponent's previous moves.
- `my_history`: A list containing the function's own previous moves.
- `variations`: A dictionary storing the variations of moves observed in the game. Keys are strings representing sequences of six moves, and values are counts of how many times each sequence has occurred.

## Functionality

1. **Initialization**: The function initializes a dictionary `best_choices` that maps each move to its best counter-move.
   
2. **Random Play**: If there is not enough data available (i.e., if `prev_play` is an empty string or if the length of `opponent_history` is less than 15), the function plays randomly by selecting one of the moves ("R", "P", or "S"). It then appends the opponent's move to `opponent_history` and its own move to `my_history`.

3. **Learning**: If sufficient data is available, the function updates the `variations` dictionary based on the recent moves. It constructs a key representing the last six moves played and increments the corresponding value in the `variations` dictionary.

4. **Prediction**: The function identifies sequences of moves in the `variations` dictionary that match the last four moves played (`my_history[-3:]` and `opponent_history[-2:]`). It selects the most frequent sequence and predicts the opponent's next move based on the move that counters the last move in that sequence.

5. **Return**: The function returns its predicted move and appends it to `my_history`.

