import random
import time
from collections import Counter

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

def flip_random_variable(assignment, clauses):
    flip_index = random.randint(0, len(assignment) - 1)
    assignment[flip_index] = not assignment[flip_index]
    return assignment

def evaluate_assignment(clauses, assignment):
    unsatisfied_clauses = 0
    for clause in clauses:
        clause_result = any((var > 0 and assignment[var-1]) or (var < 0 and not assignment[-var-1]) for var, _ in clause)
        if not clause_result:
            unsatisfied_clauses += 1
    return unsatisfied_clauses

def random_heuristic(assignment, clauses):
    return flip_random_variable(assignment, clauses)

def clause_coverage_heuristic(assignment, clauses):
    unsatisfied_clause_indices = [i for i, clause in enumerate(clauses) if evaluate_assignment([clause], assignment) > 0]
    
    if unsatisfied_clause_indices:
        clause_counter = Counter()
        for clause_index in unsatisfied_clause_indices:
            for var, _ in clauses[clause_index]:
                clause_counter[abs(var) - 1] += 1
        
        most_common_variable = clause_counter.most_common(1)[0][0]
        assignment[most_common_variable] = not assignment[most_common_variable]
    
    return assignment

def variable_neighborhood_descent_3sat_solver(clauses, n, heuristic_function, max_iterations=1000):
    current_assignment = generate_random_assignment(n)
    current_cost = evaluate_assignment(clauses, current_assignment)

    for _ in range(max_iterations):
        candidate_assignment = heuristic_function(current_assignment.copy(), clauses)
        candidate_cost = evaluate_assignment(clauses, candidate_assignment)

        if candidate_cost < current_cost:
            current_assignment = candidate_assignment
            current_cost = candidate_cost

        if current_cost == 0:
            return current_assignment  # Solution found

    return None  # Solution not found within the given iterations

def main():
    m = 10
    n = 20
    clauses = generate_random_3sat(m, n)

    print(f"Solving 3-SAT problem with m={m}, n={n} using Variable Neighborhood Descent with Random Heuristic")
    print(clauses)

    start_time = time.time()
    solution_random = variable_neighborhood_descent_3sat_solver(clauses, n, random_heuristic)
    end_time = time.time()
    print(f"Solution: {solution_random}")
    print(f"Execution Time: {end_time - start_time} seconds")

    print("\n")

    print(f"Solving 3-SAT problem with m={m}, n={n} using Variable Neighborhood Descent with Clause Coverage Heuristic")
    start_time = time.time()
    solution_clause_coverage = variable_neighborhood_descent_3sat_solver(clauses, n, clause_coverage_heuristic)
    end_time = time.time()
    print(f"Solution: {solution_clause_coverage}")
    print(f"Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
