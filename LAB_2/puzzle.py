import heapq
import random

class Node:
    def _init_(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def _lt_(self, other):
        return self.f < other.f

def heuristic(node, goal_state):
    h = 0
    for i in range(len(node.state)):
        value = node.state[i]
        if value != 0:
            target_index = goal_state.index(value)
            h += abs(i // 3 - target_index // 3) + abs(i % 3 - target_index % 3)
    return h

def get_successors(node):
    successors = []
    index = node.state.index(0)
    quotient = index // 3
    remainder = index % 3

    moves = []
    if quotient > 0:
        moves.append(-3)
    if quotient < 2:
        moves.append(3)

    if remainder > 0:
        moves.append(-1)
    if remainder < 2:
        moves.append(1)

    for move in moves:
        im = index + move
        if 0 <= im < 9:
            new_state = list(node.state)
            new_state[im], new_state[index] = new_state[index], new_state[im]
            h = heuristic(Node(new_state), goal_state)
            successor = Node(new_state, node, node.g + 1, h)
            successors.append(successor)
    return successors

def search_agent(start_state, goal_state):
    start_node = Node(start_state, None, 0, heuristic(Node(start_state), goal_state))
    frontier = []
    heapq.heappush(frontier, start_node)
    visited = set()
    
    while frontier:
        node = heapq.heappop(frontier)
        
        if tuple(node.state) in visited:
            continue
        visited.add(tuple(node.state))
        
        if node.state == goal_state:
            path = []
            while node:
                path.append(node.state)
                node = node.parent
            return path[::-1]
        
        for successor in get_successors(node):
            heapq.heappush(frontier, successor)
    
    return None

start_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
goal_state = [1, 2, 3, 4, 5, 0, 7, 8, 6]

D = 20
d = 0
while d <= D:
    s_node = Node(start_state)
    goal_state = random.choice(get_successors(s_node)).state
    d += 1

solution = search_agent(start_state, goal_state)
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")