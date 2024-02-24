def threeSum(nums):
    nums.sort()  # Sort the array; to avoid duplicate 
    n = len(nums)
    triplets = set()

    for i in range(n - 2):  # Iterate over array up to third-last element
        if i > 0 and nums[i] == nums[i - 1]:  # Avoid duplicate first elements
            continue

        # Two-sum with hash set
        complement_set = set()
        for j in range(i + 1, n):
            complement = - (nums[i] + nums[j])
            if complement in complement_set:
                triplets.add((nums[i], nums[j], complement))
            complement_set.add(nums[j])

    return list(triplets)

# Example usage:
nums1 = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums1))  # Output: [(-1, -1, 2), (-1, 0, 1)]

nums1 = [-1, -1, 0, 1, 2, -1, -4]
print(threeSum(nums1))  # Output: [(-1, -1, 2), (-1, 0, 1)]

nums2 = [0, 1, 1]
print(threeSum(nums2))  # Output: []

nums3 = [0, 0, 0]
print(threeSum(nums3))  # Output: [(0, 0, 0)]







def threeSum(nums):
    nums.sort()  # Sort the array
    n = len(nums)
    triplets = []

    for i in range(n - 2):  # Iterate over array up to third-last element
        if i > 0 and nums[i] == nums[i - 1]:  # Avoid duplicate first elements
            continue

        left, right = i + 1, n - 1  # Set pointers for two-sum problem
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicates for second and third elements
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return triplets

# Example usage:
nums1 = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums1))  # Output: [[-1, -1, 2], [-1, 0, 1]]

nums2 = [0, 1, 1]
print(threeSum(nums2))  # Output: []

nums3 = [0, 0, 0]
print(threeSum(nums3))  # Output: [[0, 0, 0]]

