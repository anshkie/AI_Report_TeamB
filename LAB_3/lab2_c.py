import itertools
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

def is_satisfiable(clauses, assignment):
    for clause in clauses:
        clause_result = False
        for var, value in clause:
            if (var > 0 and assignment[var-1]) or (var < 0 and not assignment[-var-1]):
                clause_result = True
                break
        if not clause_result:
            return False
    return True

def brute_force_3sat_solver(clauses, n):
    for assignment in itertools.product([True, False], repeat=n):
        if is_satisfiable(clauses, assignment):
            return assignment
    return None

def main():
    m_values = [10, 20, 30]  # Different values for m
    n_values = [10, 20, 30]  # Different values for n

    for m in m_values:
        for n in n_values:
            print(f"Solving 3-SAT problem with m={m}, n={n}")
            
            # Generate a random 3-SAT problem
            clauses = generate_random_3sat(m, n)
            print(clauses)
            
            # Measure the time taken by the brute-force solver
            start_time = time.time()
            solution = brute_force_3sat_solver(clauses, n)
            end_time = time.time()
            
            # Display the result and execution time
            print(f"Solution: {solution}")
            print(f"Execution Time: {end_time - start_time} seconds")
            print("=" * 30)

if __name__ == "__main__":
    main()
