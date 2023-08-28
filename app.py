from brute import brute_force
from dpll import dpll

clauses_arr = [
    [{("p", True), ("q", False)}, {("p", True), ("r", True)}]
]

for clauses in clauses_arr:
    _bf_is, bf_result = brute_force(clauses)
    _dpll_is, dpll_result = dpll(clauses)

    assert _bf_is == _dpll_is, "The results are not the same"
    print("Brute force: ", bf_result)
    print("DPLL: ", dpll_result)
    print("The results are the same")
