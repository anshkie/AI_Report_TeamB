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

def flip_random_variable(assignment, clauses):
    flip_index = random.randint(0, len(assignment) - 1)
    assignment[flip_index] = not assignment[flip_index]
    return assignment

def flip_random_clause(assignment, clauses):
    unsatisfied_clause_indices = [i for i, clause in enumerate(clauses) if evaluate_assignment([clause], assignment) > 0]
    if unsatisfied_clause_indices:
        flip_clause_index = random.choice(unsatisfied_clause_indices)
        flip_index = random.choice(range(3))
        variable_to_flip = clauses[flip_clause_index][flip_index][0]
        assignment[abs(variable_to_flip) - 1] = not assignment[abs(variable_to_flip) - 1]
    return assignment

def swap_two_variables(assignment, clauses):
    index1, index2 = random.sample(range(len(assignment)), 2)
    assignment[index1], assignment[index2] = assignment[index2], assignment[index1]
    return assignment

def variable_neighborhood_descent_3sat_solver(clauses, n, max_iterations=1000):
    current_assignment = generate_random_assignment(n)
    current_cost = evaluate_assignment(clauses, current_assignment)

    neighborhood_functions = [flip_random_variable, flip_random_clause, swap_two_variables]

    for _ in range(max_iterations):
        for neighborhood_function in neighborhood_functions:
            candidate_assignment = neighborhood_function(current_assignment.copy(), clauses)
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

    print(f"Solving 3-SAT problem with m={m}, n={n} using Variable Neighborhood Descent")
    print(clauses)

    start_time = time.time()
    solution = variable_neighborhood_descent_3sat_solver(clauses, n)
    end_time = time.time()

    print(f"Solution: {solution}")
    print(f"Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
