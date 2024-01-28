class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        return sum(self.nums[left:right+1])


class NumArray:

    def __init__(self, nums):
        self.cumulative_sum = [0]
        for num in nums:
            self.cumulative_sum.append(self.cumulative_sum[-1] + num)

    def sumRange(self, left, right):
        return self.cumulative_sum[right + 1] - self.cumulative_sum[left]

numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))  # Output: 1
print(numArray.sumRange(2, 5))  # Output: -1
print(numArray.sumRange(0, 5))  # Output: -3
