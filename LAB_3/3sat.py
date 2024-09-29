def is_3_sat(expression):
    clauses = expression.split(" AND ")

    for clause in clauses:
        literals = clause.strip("()").split(" OR ")

        # Check if the clause has exactly three literals
        if len(literals) != 3:
            return False

        for literal in literals:
            # Check if the literal is a valid variable or its negation
            if not (literal.startswith("~x") and literal[2:].isdigit()):
                return False

    return True

# Example usage:
expression = "((~x1 OR ~x2 OR ~x4) AND (~x3 OR ~x1 OR ~x4) AND (~x4 OR ~x3 OR ~x2) AND (~x3 OR ~x1 OR ~x2) AND (~x2 OR ~x4 OR ~x3))"
result = is_3_sat(expression)

print(f"The given expression is 3-SAT: {result}")
