Memoization or Tabulation: Choose whether to use memoization or tabulation to store and reuse solutions to subproblems. Memoization involves caching the results of recursive calls to avoid redundant computations, while tabulation involves filling up a table iteratively. Memoization is often preferred for problems with complex recursive structures, while tabulation is suitable for problems with clear state transitions and subproblem dependencies.


Memoization: This is a top-down approach where the problem is solved recursively by breaking it down into smaller subproblems. The solutions to subproblems are memoized (stored) to avoid redundant computations. Memoization is often implemented using recursion with memoization dictionaries or arrays.

Tabulation: This is a bottom-up approach where the problem is solved iteratively by filling up a table or array. The solutions to smaller subproblems are used to build up solutions to larger subproblems until the final solution is obtained. Tabulation typically uses loops and arrays to store solutions.



Memoization and tabulation are two common techniques used in dynamic programming to optimize solutions by avoiding redundant calculations and improving time complexity. Both techniques are used to store and reuse solutions to subproblems, but they differ in their approach to storing these solutions.

**Memoization**:

Memoization is a top-down approach to dynamic programming. It involves storing the results of expensive function calls and returning the cached result when the same inputs occur again. In dynamic programming, this typically involves using a memoization table (often implemented as a dictionary or an array) to store the solutions to subproblems.

Here's how memoization works:

1. When solving a subproblem, the algorithm checks if the solution for that subproblem is already stored in the memoization table.
2. If the solution is found, it is returned directly without recomputing.
3. If the solution is not found, the algorithm computes the solution recursively, stores it in the memoization table, and returns it.
4. Subsequent calls to the same subproblem will retrieve the solution from the memoization table, avoiding redundant calculations.

Memoization is particularly useful for problems with overlapping subproblems, as it avoids recalculating solutions for the same subproblems multiple times.

**Tabulation**:

Tabulation is a bottom-up approach to dynamic programming. It involves solving larger subproblems by iteratively filling up a table with solutions to smaller subproblems. In tabulation, there is no recursion involved; instead, the algorithm systematically builds up solutions to larger subproblems based on solutions to smaller subproblems.

Here's how tabulation works:

1. The algorithm initializes a table (often implemented as a 1D or 2D array) to store solutions to subproblems.
2. It fills up the table iteratively, starting with the smallest subproblems and progressing to larger ones.
3. Each cell in the table represents the solution to a particular subproblem.
4. The algorithm uses previously computed solutions to smaller subproblems to build up solutions to larger subproblems.
5. Once the table is filled, the final solution to the original problem can be found in the last cell of the table.

Tabulation is typically used when the problem's optimal solution depends only on solutions to smaller subproblems, and there is no need to recompute solutions multiple times.

In summary, memoization and tabulation are both techniques used in dynamic programming to optimize solutions by storing and reusing solutions to subproblems. Memoization involves caching solutions to subproblems recursively, while tabulation involves iteratively filling up a table with solutions to subproblems. Each technique has its advantages and is suitable for different types of dynamic programming problems.

Choosing the right technique:

The best approach depends on the specific problem and its properties:

Use memoization: If the problem naturally lends itself to recursion and you only need solutions for specific subproblems encountered during the main calculation.
Use tabulation: If the problem requires calculating all possible subproblems, or if a bottom-up iterative approach is more efficient or memory-friendly.


https://medium.com/@aryan.jain19/memoization-vs-tabulation-in-dp-4ff137da8044
