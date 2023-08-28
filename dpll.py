def select_literal(clauses):
    '''
    Selects a literal from a clauses

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
        return pa

    # This means there is a disjunction with an empty clause, which is always False
    if [] in clauses:
        return False, None

    # FIRST remove al the cla
