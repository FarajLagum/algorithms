'''
Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
'''

def maxArea(height):
    # This algorithm runs in O(n) time complexity, 
    max_area = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        # Calculate the area
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        
        # Move the pointer corresponding to the shorter line towards the center
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Example usage:
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height1))  # Output: 49

height2 = [1, 1]
print(maxArea(height2))  # Output: 1


print("=============")


# brute-force solution:
def maxArea(height):
    max_area = 0
    
    # Consider all possible pairs of lines
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            # Calculate the area for the current pair
            area = min(height[i], height[j]) * (j - i)
            # Update the maximum area found so far
            max_area = max(max_area, area)
    
    return max_area

# Example usage:
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height1))  # Output: 49

height2 = [1, 1]
print(maxArea(height2))  # Output: 1




def hammingWeight(n):
    # Convert binary string to integer
    num = int(n, 2)
    
    count = 0
    while num != 0:
        count += num & 1  # Add LSB to count if it's 1
        num >>= 1        # Shift input number to the right by one bit
    return count

# Example usage:
n1 = "00000000000000000000000000001011"
print(hammingWeight(n1))  # Output: 3

