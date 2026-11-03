
def is_variable(x):
    return isinstance(x, str) and x.islower()


def occurs_check(var, expr, subst):
    expr = apply_substitution(expr, subst)

    if var == expr:
        return True

    if isinstance(expr, tuple):
        return any(occurs_check(var, arg, subst) for arg in expr[1:])

    return False


def apply_substitution(expr, subst):
    if isinstance(expr, str):
        while expr in subst:
            expr = subst[expr]
        return expr

    if isinstance(expr, tuple):
        return (expr[0],) + tuple(
            apply_substitution(arg, subst) for arg in expr[1:]
        )

    return expr


def unify(x, y, subst=None):
    if subst is None:
        subst = {}

    x = apply_substitution(x, subst)
    y = apply_substitution(y, subst)

    # Step 1: If both expressions are identical
    if x == y:
        return subst

    # Step 2: Check if x is a variable
    if is_variable(x):
        if occurs_check(x, y, subst):
            return None
        subst[x] = y
        return subst

    # Step 3: Check if y is a variable
    if is_variable(y):
        if occurs_check(y, x, subst):
            return None
        subst[y] = x
        return subst

    # Step 4: Check predicate/function symbols
    if isinstance(x, tuple) and isinstance(y, tuple):

        # Check initial symbols
        if x[0] != y[0]:
            return None

        # Check number of arguments
        if len(x) != len(y):
            return None

        # Step 5: Unify corresponding arguments
        for a, b in zip(x[1:], y[1:]):
            subst = unify(a, b, subst)

            if subst is None:
                return None

        return subst

    # Step 6: If expressions cannot be unified
    return None


# Main Program
print("UNIFICATION ALGORITHM")

expr1 = ("Knows", "x", "John")
expr2 = ("Knows", "Mary", "y")

print("\nExpression 1:", expr1)
print("Expression 2:", expr2)

result = unify(expr1, expr2)

if result is None:
    print("\nUnification Failed!")
elif result == {}:
    print("\nExpressions are identical. No substitution needed.")
else:
    print("\nUnification Successful!")
    print("Substitution Set:", result)
