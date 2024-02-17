
def knapsack(capacity, wt, profit, n): 
    K = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)] 

    for i in range(n + 1): 
        for j in range(capacity + 1): 
            if i == 0 or j == 0: 
                K[i][j] = 0
            elif wt[i-1] <= j: 
                K[i][j] = max(profit[i-1] 
                          + K[i-1][j-wt[i-1]],   
                              K[i-1][j]) 
            else: 
                K[i][j] = K[i-1][j] 
  
    return K[n][capacity] 

values = [60, 100, 120] 
weights = [10, 20, 30] 
capacity = 50
n = len(values) 
print(knapsack(capacity, weights, values, n))