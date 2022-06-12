from collections import deque

double_ended_queue = deque(["Eric", "John", "Michael"])

double_ended_queue.append("Terry")           # Terry arrives
double_ended_queue.append("Graham")          # Graham arrives
double_ended_queue.popleft()                 # The first to arrive now leaves

double_ended_queue.popleft()                 # The second to arrive now leaves

# Remaining queue in order of arrival
print(double_ended_queue)
#deque(['Michael', 'Terry', 'Graham'])

print(double_ended_queue.pop())
print(double_ended_queue)

double_ended_queue.appendleft("Graham")
print(double_ended_queue)
