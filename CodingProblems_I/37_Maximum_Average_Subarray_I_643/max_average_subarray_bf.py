# time complexity:  O((n-k)*k)
#   *  n-k for loop & k for sum
# space complexity O(1)



def max_sum_subarray(array, k):
    max_avge = float("-Inf")

    for i in range(len(array)-k):
        print(i)

        max_avge = max(max_avge, sum(array[i:i+k]))


    return max_avge/k

nums = [1,12,-5,-6,50,3]
k=4
print(max_sum_subarray(nums, k))
i=1
print(nums[i:i+k])