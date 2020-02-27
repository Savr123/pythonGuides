# guide heapq
# this module provide heap queue algorithm, also known as the priority queue algorithm.

import heapq

# Push the value item onto the heap, maintaining the heap invariant.
#----------------------------------------------------------------------------------------------------------------
# heapq.heappush(heap, item)
#----------------------------------------------------------------------------------------------------------------

#Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, 
# 	IndexError is raised. To access the smallest item without popping it, use heap[0].
#----------------------------------------------------------------------------------------------------------------
# heapq.heappop(heap)
#----------------------------------------------------------------------------------------------------------------

#Push item on the heap, then pop and return the smallest item from the heap. 
# 	The combined action runs more efficiently than heappush() followed by a separate call to heappop().
#----------------------------------------------------------------------------------------------------------------
# heapq.heappushpop(heap, item)
#----------------------------------------------------------------------------------------------------------------

#Transform list x into a heap, in-place, in linear time.
#----------------------------------------------------------------------------------------------------------------
# heapq.heapify(x)
#----------------------------------------------------------------------------------------------------------------

# Exaples:

Countries = ["Canada", "USA", "England"]
print(Countries)

Grades = [x**x for x in range(0,8)]
print(Grades)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

def appendItem(heap, value):
		heapq.heappush(heap, value)
		print(heap)

def rmLastItem(heap):
	temp = heapq.heappop(heap)
	print(temp)
	print(heap)

appendItem(Countries, "Russia")
rmLastItem(Countries)
