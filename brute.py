def product(iterable, repeat=1):
    '''
    Cartesian product of input iterable.

    Args:
        iterable: an iterable to be combined in the cartesian product.
        repeat: number of repetitions of the cartesian product.

    Returns:
        cartesian product of input iterables, as tuples.
    '''

    # FIRST. Define a pool of iterables, it means a list of repeated iterables to be combined in the cartesian product
    pools = [tuple(iterable)] * repeat
    result = [[]]

    # SECOND. Iterate over the pool of iterables, and for each iterable, iterate over the result list, and append the iterable to each element of the result list.
    for pool in pools:
        # 🧠 the '+' works as concatenation in this context
        result = [x+[y] for x in result for y in pool]

        '''
        Example: iterable=[True, False], repeat=3

        pool_0 --> [[True], [False]]
        pool_1 --> [[True, True], [True, False], [False, True], [False, False]]
        pool_2 --> [[True, True, True], [True, True, False], [True, False, True], [True, False, False], [False, True, True], [False, True, False], [False, False, True], [False, False, False]]
        '''

    # THIRD.  Return the result a list of tuples, being immutable is the rule 😈
    return tuple(result)


def brute_force(clauses):
    '''
    Given a clause, returns a satisfying assignment for the clause, or None if no such assignment exists.

    Args: 
        clause: a clause to be satisfied. May be in the next form: [{('<var name>', <T or F>), ...}, ...]

    Returns: a satisfying assignment for the given clause, or None if no such.
    '''

    # FIRST. Get all variables from the clause

    # 🧠 using set() initially to get rid of duplicates
    variables = list(set(variable[0]
                     for clause in clauses for variable in clause))

    n = len(variables)

    # SECOND. Get all possible assignments for the variables, it means all possible combinations of T and F given the number of variables
    combinations = product(iterable=[True, False], repeat=n)

    # THIRD. Iterate over the combinations, and for each combination, check if it satisfies the clause
    for combination in combinations:
        # 🧠 Using the built-in function zip() to iterate over two iterables at the same time. More info: https://docs.python.org/3/library/functions.html?highlight=zip#zip
        x = set(zip(variables, combination))

        # 🧠 Using the built-in function all() to check if all the elements of an iterable are True. More info: https://docs.python.org/3/library/functions.html?highlight=all#all
        # 🧠 Using the built-in sets function intersection() to check if there is some value of the combination in clause.
        if not False in [bool(clause.intersection(x)) for clause in clauses]:
            return True, x

    # FOURTH. If no satisfying assignment is found, return None
    return False, None
