import random

# Create a dictionary to store each game state as a matchbox with moves (beads)
matchboxes = {}

# Function to initialize a matchbox with beads for each possible move
def initialize_matchbox(state):
    matchboxes[state] = [1 for _ in range(9)]  # 9 possible moves (0-8)

# Function to choose a move based on the beads in the matchbox
def choose_move(state):
    if state not in matchboxes:
        initialize_matchbox(state)
    beads = matchboxes[state]
    total_beads = sum(beads)
    weighted_choices = [i for i, count in enumerate(beads) for _ in range(count)]
    return random.choice(weighted_choices)

# Function to update matchbox based on the outcome of the game
def update_matchbox(state, move, outcome):
    if state not in matchboxes:
        return
    if outcome == 'win':
        matchboxes[state][move] += 3  # Add beads if the game is won
    elif outcome == 'draw':
        matchboxes[state][move] += 1  # Add a bead for a draw
    elif outcome == 'lose':
        matchboxes[state][move] = max(1, matchboxes[state][move] - 1)  # Remove a bead if lost, min 1

# Simulate a simple game of Tic-tac-toe between MENACE and a random player
def play_game():
    states = []  # Store states and moves to update after the game
    board = [' '] * 9
    player = 'X'

    while ' ' in board:
        state = ''.join(board)
        if player == 'X':  # MENACE's turn
            move = choose_move(state)
        else:  # Random player move
            move = random.choice([i for i, x in enumerate(board) if x == ' '])

        board[move] = player
        states.append((state, move))

        # Check for a win or draw
        if check_win(board, player):
            return 'X' if player == 'X' else 'O', states
        if ' ' not in board:
            return 'draw', states

        player = 'O' if player == 'X' else 'X'

    return 'draw', states

# Function to check if a player has won
def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

# Train MENACE over multiple games
for _ in range(1000):
    outcome, states = play_game()
    for state, move in states:
        update_matchbox(state, move, outcome)

# Output the matchbox configuration after training
print(matchboxes)