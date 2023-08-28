# sat-pr 👾 AKA Proyecto 2 - LM

Exploring the boolean satisfiability problem (SAT) by brute force and DPLL algorithm

## 🧐 Understanding the problem

The term "SAT" stands for *'satisfiability'*, which refers to the property of a logical formula being capable of being satisfied or made true. The Boolean satisfiability problem, often abbreviated as SAT, involves determining whether there exists an assignment of truth values to variables in a given Boolean formula such that the formula evaluates to true. 

It has been extensively studied due to its fundamental importance in computational complexity theory and its numerous applications in areas such as automated reasoning, formal verification, artificial intelligence, and circuit design.

In the SAT problem, a Boolean formula is typically expressed in conjunctive normal form (CNF), which is a conjunction (logical AND) of clauses, where each clause is a disjunction (logical OR) of literals (variables or their negations).

> 🧠 Remember, a boolean formula is called *'satisfiable'* if we can assign truth values to the atomic values so the entire formula becomes true ✅.

Before we can dive in the proposed solutions exposed on this repo lets see some examples:

1. **Formula with multiple variables and clauses.**

    Consider the formula ***(p OR q) AND (NOT p OR NOT q)***.
    
    To determine its satisfiability, we need to find an assignment of truth values to the variables p and q that makes the entire formula true. Let's consider the assignment where p is assigned true (T) and q is assigned false (F).

    Substituting these values into the formula, we get:
    
    *(T OR F) AND (NOT T OR NOT F)*

    This simplifies to:

    *T AND F*

    Which evaluates to false (F).

        Since the formula evaluates to false for this assignment, it is not satisfiable.

2. **Formula with a single variable.**

    Consider the formula p OR NOT p. 
    
    Again, we need to find an assignment of truth values to the variable p that makes the entire formula true.

    Let's consider the assignment where p is assigned true (T).

    Substituting this value into the formula, we get:

    *T OR NOT T*

    This simplifies to:

    *T OR F*

    Which evaluates to true (T).

        Since the formula evaluates to true for this assignment, it is satisfiable.

> It seems easy, ⚠️ but wait don't overestimate the situation... If needed you can found a very clearly explanation on [this site](https://davefernig.com/2018/05/07/solving-sat-in-python/). Also some funny approaches [here](https://math.stackexchange.com/questions/86210/what-is-the-3-sat-problem).

### 🦾 Brute force

The **conjunctive normal form** mentioned above is also know as *'fórmula booleana en forma de clausula'*. And is what we are intended to receive, analyze in order to return the correct asignation on the [brute force program](./brute-force/).  

> ℹ️ You may want to explore more about CNF on [Wikipedia](https://es.wikipedia.org/wiki/Forma_normal_conjuntiva).

### 👩‍💻 DPLL

On the other hand, we found the Davis-Putnam-Logemann-Loveland [DPLL](https://en.wikipedia.org/wiki/DPLL_algorithm) algorithm. For this solution we will receive again a 'fórmula booleana en forma de clausula'. And again we need report if that expression is or not satisfiable, but also return the partial interpretation that satisfies the expression.
