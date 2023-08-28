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

> It seems easy, ⚠️ but wait don't overestimate the situation... if needed you can found a very clearly explanation on [this site](https://davefernig.com/2018/05/07/solving-sat-in-python/). Also very funny approaches [here](https://math.stackexchange.com/questions/86210/what-is-the-3-sat-problem).

### 🦾 Brute force

The **conjunctive normal form** mentioned above is also know as *'fórmula booleana en forma de clausula'*. And is what we are intended to receive, analyze in order to return the correct asignation on the [brute force program](./brute-force/).  

In the SAT problem, a formula is expressed as a conjunction of clauses.

> ℹ️ You may want to explore more about CNF on [Wikipedia](https://es.wikipedia.org/wiki/Forma_normal_conjuntiva).

In the SAT problem, a formula is expressed as a conjunction of clauses, and each clause is a disjunction of literals. To determine if a given assignment satisfies the entire formula, we need to check if the assignment intersects (shares at least one literal in common) with each conjunct (clause) in the formula.

🛑 If why this method ([naive approach](https://www.cs.rice.edu/~vardi/comp409/lec9.pdf)) works is still diffuse here is a better explanation (highly recommended):

> Imagine you have a room with a bunch of colorful toys 🧸 scattered all over the floor. Each toy represents a "literal" (a variable) in the SAT problem, and these literals can be either true or false.

> Now, you have a set of special cards, and each card represents an assignment of truth values to the literals (a combination). For example, one card might say, "Make the red toy true and the blue toy false." Another card might say, "Make the yellow toy true and the green toy true."

> To solve the SAT problem, you want to find a special card that makes all the toys happy, which means it satisfies the entire formula. In other words, you're looking for a card that intersects (shares at least one toy) with each group of toys.

> To check if a card intersects with a group of toys, you take the card and compare it with the toys in the group. You look for any toy that appears on both the card and in the group. If you find at least one toy that they have in common, it means the card satisfies that particular group of toys.

> Now, to solve the SAT problem, you need to check if there's a special card that intersects with every group of toys. If you find a card that has at least one toy in common with every group, then you've found a solution! The formula is satisfiable.

> On the other hand, if you can't find any card that intersects with every group of toys, it means there's no way to make all the toys happy at the same time. The formula is unsatisfiable.

> So, the notion of intersection is all about finding common elements between the special cards (assignments) and the groups of toys (conjuncts/clauses) to see if we can make all the toys happy. If we can, we have a solution. If we can't, we don't have a solution.

But why @#$ intersecting means that an assignment satisfies a particular group (clause)? 

Using the toys example. In the SAT problem, each group of toys represents a conjunct, which is essentially a set of literals connected by the logical OR operation. For example, let's say we have a group of toys: {red, blue, green}. This group represents the conjunct "(red OR blue OR green)".

Now, when we talk about intersecting, we are checking if the assignment ( combination | special card) and the group of toys (conjunct | clause) have at least one toy in common. In other words, we are looking for a toy that appears both in the assignment and in the group.

Remember that the CNF is the expression of the formula. But the combinations is the assignation of values. In other terms, we check for each clause because if we found an intersection it means that there is on of the next:

1. An assignation of True to True delivering True, and because is part of an OR it will return a complete True for the clause.
2. An assignation of False to a negation delivering a True, and because is part of an OR it will return a complete True for the clause.

After that we check if all the clause in the AND are true, so we can determine if is a 'satisfiable' combination.

### 👩‍💻 DPLL

On the other hand, we found the Davis-Putnam-Logemann-Loveland [DPLL](https://en.wikipedia.org/wiki/DPLL_algorithm) algorithm. For this solution we will receive again a 'fórmula booleana en forma de clausula'. And again we need report if that expression is or not satisfiable, but also return the partial interpretation that satisfies the expression.

The implementation is based on the pseudocode from the PDF instructions, but if you want to deep in it you can visit [this](https://math.stackexchange.com/questions/96080/in-satisfiability-what-is-the-difference-between-the-empty-clause-and-the-empty/96097#96097)

### Awesome!

After you long journey reading what I prepare for you 🤗, you are ready to dive into the code. This is the [brute-force](./brute.py) approach, and this the [DPLL implementation](./dpll.py). 

Some final advice is to remember that the *'forma clausal'* stablish that conjunction (∧) will be represented as first layer sets on the structure, while disjunction (∨) gonna be represented as the array inside each first layer sets. This are some examples:

![image](https://github.com/chamale-rac/sat-pr/assets/63200593/86d98ae5-624b-49d2-a6f9-ba598c309682)
