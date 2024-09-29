from collections import deque

def is_goal(state):
    # Check if the current state is the goal state
    return state == ('W', 'W', 'W', '_', 'E', 'E', 'E')

def get_neighbors(state):
    # Generate all valid neighboring states from the current state
    neighbors = []
    state_list = list(state)
    empty_index = state_list.index('_')
    
    # Possible moves: one step or two steps
    possible_moves = [-1, 1, -2, 2]
    
    for move in possible_moves:
        new_index = empty_index + move
        
        if 0 <= new_index < len(state_list):
            # Check if it's a valid move
            if abs(move) == 1 or (abs(move) == 2 and state_list[empty_index + move // 2] != '_'):
                # Swap the empty stone with the rabbit
                new_state_list = state_list[:]
                new_state_list[empty_index], new_state_list[new_index] = new_state_list[new_index], new_state_list[empty_index]
                neighbors.append(tuple(new_state_list))
                
    return neighbors

def dfs(initial_state):
    # DFS to find a path to the goal state
    stack = [(initial_state, [])]
    visited = set()
    visited.add(initial_state)
    
    while stack:
        current_state, path = stack.pop()
        
        if is_goal(current_state):
            return path + [current_state]
        
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [current_state]))
    
    return None



def bfs(initial_state):
    # BFS to find the shortest path to the goal state
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)
    
    while queue:
        current_state, path = queue.popleft()
        
        if is_goal(current_state):
            return path + [current_state]
        
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [current_state]))
    
    return None

# Initial state: W1 W2 W3 _ E1 E2 E3
initial_state = ('E', 'E', 'E', '_', 'W', 'W', 'W')

solution_d = dfs(initial_state)
solution_b = bfs(initial_state)

if solution_b:
    print("Rabbits can cross each other without stepping into the water. Using BFS")
    print("Number of moves:", len(solution_b) - 1)
    print("Sequence of moves:")
    for state in solution_b:
        print(state)
else:
    print("No solution found.")



if solution_d:
    print("Rabbits can cross each other without stepping into the water. using DFS")
    print("Number of moves:", len(solution_d) - 1)
    print("Sequence of moves:")
    for state in solution_d:
        print(state)
else:
    print("No solution found.")    