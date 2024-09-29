import random
import time

def generate_random_3sat(m, n):
    variables = range(1, n+1)
    clauses = []
    for _ in range(m):
        clause = random.sample(variables, 3)
        clause = [(var, random.choice([True, False])) for var in clause]
        clauses.append(clause)
    return clauses

def generate_random_assignment(n):
    return [random.choice([True, False]) for _ in range(n)]

def evaluate_assignment(clauses, assignment):
    unsatisfied_clauses = 0
    for clause in clauses:
        clause_result = any((var > 0 and assignment[var-1]) or (var < 0 and not assignment[-var-1]) for var, _ in clause)
        if not clause_result:
            unsatisfied_clauses += 1
    return unsatisfied_clauses

def hill_climbing_3sat_solver(clauses, n, max_iterations=1000):
    current_assignment = generate_random_assignment(n)
    current_cost = evaluate_assignment(clauses, current_assignment)

    for _ in range(max_iterations):
        neighbor_assignment = current_assignment.copy()
        flip_index = random.randint(0, n-1)
        neighbor_assignment[flip_index] = not neighbor_assignment[flip_index]

        neighbor_cost = evaluate_assignment(clauses, neighbor_assignment)

        if neighbor_cost < current_cost:
            current_assignment = neighbor_assignment
            current_cost = neighbor_cost

        if current_cost == 0:
            return current_assignment  # Solution found

    return None  # Solution not found within the given iterations

def main():
    m = 10
    n = 20
    clauses = generate_random_3sat(m, n)

    print(f"Solving 3-SAT problem with m={m}, n={n} using Hill Climbing")
    print(clauses)
    
    start_time = time.time()
    solution = hill_climbing_3sat_solver(clauses, n)
    end_time = time.time()

    print(f"Solution: {solution}")
    print(f"Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
