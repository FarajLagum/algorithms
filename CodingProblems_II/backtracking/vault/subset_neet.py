def search(array, result, subset_state, index):
	# Add the current subset to the result list
	#print(subset)
	result.append(subset_state.copy())

	# Generate subsets by recursively including and excluding elements
	for i in range(index, len(array)):
		# Include the current element in the subset
		subset_state.append(array[i])

		# Recursively generate subsets with the current element included
		search(array, result, subset_state, i + 1)

		# Exclude the current element from the subset (backtracking)
		subset_state.pop()


def subsets(array):
	subset = []
	result = []
	index = 0
	search(array, result, subset, index)
	return result


# Driver code
if __name__ == "__main__":
	array = [1, 2, 3]
	result = subsets(array)

	#Print the generated subsets
	# for subset in result:
	# 	print(*subset)
	print(result)
