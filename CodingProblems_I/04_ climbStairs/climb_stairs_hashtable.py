def climb_stairs(n):
    nways={0:0, 1:1, 2:2}
    if n in nways:
        return nways[n]


    for i in range(3, n+1):
        nways[i] = nways[i-1] + nways[i-2]
    
    return nways[n]


print(climb_stairs(5))


'''

Time complexity analysis: O(n).
This is because we are simply iterating from 2 to n once.

Space complexity analysis: O(n)
, ecause we are using a hashtable of size n+1 to store the number of ways to reach each step. 

This is the same as the space complexity of the dynamic programming solution using an array. 
However, if the input n is large, the dynamic programming solution with constant space would be more suitable.

      
      
        
      
    
  

  
  
  
  
  
  
    
    
     
  

         
        
    
  

    
    
    
    
    
  

'''