def select_literal(clauses):
    '''
    Selects a literal from a clauses, this make the code non-deterministic

    Args:
        clauses: a CNF formula

    Returns:
        a variable (literal) from the given formula
    '''
    for clause in clauses:
        for variable, _ in clause:
            return variable


def dpll(clauses, pa={}):
    '''
    DPLL algorithm

    Args:
        cnf: a CNF formula
        pa: a partial assignation


    Returns:
        a satisfying assignation for the given formula, or None if no such.
    '''

    if clauses == []:
        return True, pa

    # 🧠 Use built-in any(function) to check if there is an empty clause in the formula
    # This means there is a disjunction with an empty clause, which is always False
    if any(len(c) == 0 for c in clauses):
        return False, None

    selected = select_literal(clauses)

    # FIRST. Remove the clauses that contains the selected. But also remove the occurrences of the complementary literal of selected by building CNF'

    # 🧠 Use subtraction to remove the literal from each clause that contains it.
    new_clauses = [c - {(selected, False)}
                   for c in clauses if (selected, True) not in c]

    # 🧠 Using | to merge two dictionaries into a new dictionary XD.
    _is, vals = dpll(new_clauses, pa | {selected: True})
    if _is:
        return _is, vals

    new_clauses = [c - {(selected, True)}
                   for c in clauses if (selected, False) not in c]

    # 🧠 Using | to merge two dictionaries into a new dictionary XD.
    _is, vals = dpll(new_clauses, pa | {selected: False})
    if _is:
        return _is, vals

    return False, None
