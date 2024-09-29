import random

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

def beam_search_3sat_solver(clauses, n, beam_width):
    beam = [generate_random_assignment(n) for _ in range(beam_width)]

    for _ in range(1000):  # Maximum number of iterations
        next_beam = []

        for assignment in beam:
            for flip_index in range(n):
                neighbor_assignment = assignment.copy()
                neighbor_assignment[flip_index] = not neighbor_assignment[flip_index]

                if evaluate_assignment(clauses, neighbor_assignment) == 0:
                    return neighbor_assignment  # Solution found

                next_beam.append(neighbor_assignment)

        # Select top beam_width candidates based on the number of unsatisfied clauses
        next_beam.sort(key=lambda x: evaluate_assignment(clauses, x))
        beam = next_beam[:beam_width]

    return None  # Solution not found within the given iterations

def main():
    m = 10
    n = 20
    clauses = generate_random_3sat(m, n)
    print(clauses)

    print(f"Solving 3-SAT problem with m={m}, n={n} using Beam Search (beam width = 3)")
    solution = beam_search_3sat_solver(clauses, n, beam_width=3)
    print(f"Solution: {solution}")

    print(f"\nSolving 3-SAT problem with m={m}, n={n} using Beam Search (beam width = 4)")
    solution = beam_search_3sat_solver(clauses, n, beam_width=4)
    print(f"Solution: {solution}")

if __name__ == "__main__":
    main()
