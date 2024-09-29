# Marble Solitaire Solver

Implementation of AI agents to solve the game of marble solitaire using the following search strategies:
1. Priority queue based search
2. Best first search
3. A* search

**Note**: The goal of the solver is to get to a state with only one marble at the center of the board.

## Heuristic functions used:
1. Sum of manhattan distance of all the marbles left on the board from center.
2. Number of marbles left on the board.
