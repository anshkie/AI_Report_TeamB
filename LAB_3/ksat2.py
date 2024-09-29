import random

def generate_random_ksat(m, n, k):
    variables = range(1, n+1)
    clauses = []
    
    for _ in range(m):
        clause = random.sample(variables, k)
        clause = [(var, random.choice([True, False])) for var in clause]
        clauses.append(clause)
    
    return clauses

# Example usage for a 4-SAT problem with 20 variables and 10 clauses
m = 10
n = 20
k = 4
ksat_instance = generate_random_ksat(m, n, k)

print(f"Generated {k}-SAT instance:")
for clause in ksat_instance:
    print(clause)
