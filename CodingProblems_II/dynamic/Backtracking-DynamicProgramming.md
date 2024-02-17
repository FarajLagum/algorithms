# Backtracking and Dynamic Programming:

**Backtracking**:
- Backtracking is a technique for finding all (or some) solutions to computational problems, particularly constraint satisfaction problems.
- It incrementally builds candidates for the solutions, but abandons a candidate as soon as it determines that the candidate cannot possibly be extended to a valid solution.
- Backtracking is useful when you need to find all possible solutions and have constraints to consider⁴.

**Dynamic Programming**:
- Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems.
- It solves each subproblem just once and stores the result of each subproblem to avoid duplicate work.
- DP relies on the principle of optimality, which means that the solution to a problem is composed of solutions to its subproblems.
- DP is used to find the optimal solution and reuses previously computed results.

**Key Differences**:
- The major difference between the two is that dynamic programming is used for optimization problems where we need to find the best solution, while backtracking is used to find all possible solutions.
- In dynamic programming, subproblems overlap and are solved many times, while in backtracking, each potential solution is generated and checked only once.
- Dynamic programming uses a bottom-up approach, solving all related subproblems first, while backtracking uses a top-down approach, generating potential solutions and discarding those that fail to satisfy the constraints.