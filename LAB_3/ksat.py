import random

def generate_k_sat(k, m, n):
    variables = [f"x{i}" for i in range(1, n + 1)]
    formula = []

    for _ in range(m):
        clause = random.sample(variables + [f"~{var}" for var in variables], k)
        formula.append("(" + " OR ".join(clause) + ")")

    return formula

k_value = int(input("Enter the length of clause: "))
m_value = int(input("Enter the no. of clauses: "))
n_value = int(input("Enter the no. of variables: "))

random_k_sat_formula = generate_k_sat(k_value, m_value, n_value)

print("Generated k-SAT formula:")
print("(" + " AND ".join(random_k_sat_formula) + ")")

