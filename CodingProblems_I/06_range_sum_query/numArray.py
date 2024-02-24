class NumArray:
    def __init__(self, nums):
        self.cumulative_sums = [0]
        for num in nums:
            self.cumulative_sums.append(self.cumulative_sums[-1] + num)

    def sumRange(self, left, right):
        return self.cumulative_sums[right + 1] - self.cumulative_sums[left]


numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))  # Output: 1
print(numArray.sumRange(2, 5))  # Output: -1
print(numArray.sumRange(0, 5))  # Output: -3

'''
it is a great use case of classes as I don't need to repeate creating the cumulative_sums 
each time I want to perform a query 
'''