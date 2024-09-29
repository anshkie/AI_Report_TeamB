from pysat.solvers import Glucose3

def is_satisfiable(expression):
    solver = Glucose3()

    # Map variable names to numbers
    var_map = {}
    num_vars = 1
    for clause in expression:
        for lit in clause:
            var = lit.strip("~")
            if var not in var_map:
                var_map[var] = num_vars
                num_vars += 1

    # Create variables and add clauses using mapped numbers
    for clause in expression:
        solver.add_clause([abs(var_map[lit.strip("~")]) for lit in clause])
    
    print(var_map)

    # ... rest of the code remains unchanged ...


    # Solve and print results
    if solver.solve():
        model = solver.get_model()
        print("Satisfiable! Model:", model)
        return True
    else:
        print("Unsatisfiable.")
        return False

# Given 3-SAT expression
expression = [
    ["~x3", "~x1", "x4"],
    ["x4", "~x4", "x1"],
    ["x1", "~x4", "x4"],
    ["~x1", "~x4", "~x2"],
    ["x3", "~x4", "~x1"]
]

# Check satisfiability and print the value of the expression
is_satisfiable(expression)
