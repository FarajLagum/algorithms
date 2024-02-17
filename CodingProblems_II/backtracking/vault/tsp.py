# Python3 implementation of the approach
# V = 4
answer = []
def get_candidate(n):
    return range(n)

def is_valid_state(graph, currPos, n, count):
    return (count == n and graph[currPos][0])

# Function to find the minimum weight 
# Hamiltonian Cycle
def search_tsp(graph, visited, curr_city, n, count, cost):

	# If last node is reached and it has 
	# a link to the starting node i.e 
	# the source then keep the minimum 
	# value out of the total cost of 
	# traversal and "ans"
	# Finally return to check for 
	# more possible values
	if is_valid_state(graph, curr_city, n, count):
		answer.append(cost + graph[curr_city][0])
		return

	# BACKTRACKING STEP
	# Loop to traverse the adjacency list
	# of currPos node and increasing the count
	# by 1 and cost by graph[currPos][i] value
	for candidate in get_candidate(n):
		if (visited[candidate] == False and graph[curr_city][candidate]):
			
			# Mark as visited
			visited[candidate] = True
			search_tsp(graph, visited, candidate, n, count + 1, 
				cost + graph[curr_city][candidate])
			# Mark ith node as unvisited
			visited[candidate] = False



# Driver code

# n is the number of nodes i.e. V
if __name__ == '__main__':
	n = 4
	graph= [[ 0, 10, 15, 20 ],
			[ 10, 0, 35, 25 ],
			[ 15, 35, 0, 30 ],
			[ 20, 25, 30, 0 ]]

	# Boolean array to check if a node
	# has been visited or not
	visited = [False for _ in range(n)]
	
	# Mark 0th node as visited
	visited[0] = True

	# Find the minimum weight Hamiltonian Cycle
	search_tsp(graph, visited, 0, n, 1, 0)

	# ans is the minimum weight Hamiltonian Cycle
	print(min(answer))

# This code is contributed by mohit kumar
