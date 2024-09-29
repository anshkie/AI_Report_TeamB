import random

def generate_k_sat(k, m, n):
    if k > n:
        print("Error: k must be less than or equal to n.")
        return

    if m <= 0 or n <= 0:
        print("Error: m and n must be positive integers.")
        return

    if k <= 0 or k > n:
        print("Error: k must be a positive integer less than or equal to n.")
        return

    if m % k != 0:
        print(f"Warning: The number of clauses (m={m}) may not be a multiple of k ({k}).")

    clauses = []

    for _ in range(m):
        clause = []
        available_variables = list(range(1, n + 1))

        for _ in range(k):
            var = random.choice(available_variables + [-v for v in available_variables])
            clause.append(var)
            available_variables.remove(abs(var))

        clauses.append(clause)

    return clauses

def print_k_sat_problem(clauses):
    for clause in clauses:
        print(" ".join(map(str, clause)))

# Example usage:
k_value = 3
m_value = 9
n_value = 5

k_sat_instance = generate_k_sat(k_value, m_value, n_value)

print(f"Generated {k_value}-SAT instance with {m_value} clauses and {n_value} variables:")
print_k_sat_problem(k_sat_instance)
