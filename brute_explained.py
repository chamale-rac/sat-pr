def product(iterable, repeat=1):
    '''
    Cartesian product of input iterable.

    Args:
        *args: iterable objects
        repeat: number of repetitions of the cartesian product.

    Returns:
        cartesian product of input iterables, as tuples.
    '''
    # FIRST.  Define a pool of iterables, it means a list of repeated iterables to be combined in the cartesian product
    pools = [tuple(iterable)] * repeat
    result = [[]]

    # SECOND.  Iterate over the pool of iterables, and for each iterable, iterate over the result list, and append the iterable to each element of the result list.
    for pool in pools:
        # 🧠 the '+' works as concatenation in this context
        result = [x+[y] for x in result for y in pool]

    # THIRD.  Return the result a list of tuples, being immutable is the rule 😈
    return tuple(result)


def brute_force(clause):
    '''
    Given a clause, returns a satisfying assignment for the clause, or None if no such assignment exists.

    Args: 
        clause: a clause to be satisfied. May be in the next form: [{('<var name>', <T or F>), ...}, ...]

    Returns: a satisfying assignment for the given clause, or None if no such.
    '''

    # FIRST. Get all variables from the clause

    # 🧠 using set() initially to get rid of duplicates
    variables = list(set(disjunct[0]
                     for conjunct in clause for disjunct in conjunct))

    # SECOND. Get all possible assignments for the variables, it means all possible combinations of T and F given the number of variables

    # 🧠 without itertools.product() we would have to write a lot of nested loops


# SECOND. Get all possible assignments for the variables
