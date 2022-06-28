from typing import List

class minHeap(list):
	def __init__(self,vals:List[int] = []):
		super().__init__()

		for val in vals:
			self.insert(val)

	def insert(self,val:int=0):
		# append the value
		self.append(val)

		# get the new len
		n = len(self)

		# traverse the tree, swapping as needed
		while n > 1:
			ndeeper = n
			n //= 2
			if self[ndeeper-1] < self[n-1]:
				buf = self[n-1]
				self[n-1] = self[ndeeper-1]
				self[ndeeper-1] = buf

	def remove(self) -> int:
		# pop min val
		res, self[:] = self[0], self[1:] # python you are so dumb I hate you so much having to splice this to make it work in-place is so arcane...
		# well anyway here's the helpful stackoverflow post that actually told me what's up: https://stackoverflow.com/questions/9459648/subclassing-a-list-in-python-why-does-slice-and-empty-list-not-work

		# move last val to root
		self[:]   = self[-1:] + self[:-1]

		# swaps
		parentnode = 0
		while True:
			parentval  = self[parentnode]
			childnodes = [2*(parentnode+1)-1,2*(parentnode+1)]
			childnodes = [childnode for childnode in childnodes if childnode < len(self)]

			if len(childnodes) == 0:
				return res

			childvals    = [self[childnode] for childnode in childnodes]
			minchildval  = min(childvals)
			minchildidx  = childvals.index(minchildval)
			minchildnode = childnodes[minchildidx]

			if parentval > minchildval:
				self[minchildnode] = parentval
				self[parentnode]   = minchildval
			else:
				return res # this BETTER be a valid stopping condition, otherwise your initial minheap wasn't actually a minheap...

			parentnode = minchildnode

# "unit tests" which are oh-so-properly written, organized, and documented
q = minHeap()
print(q)

q.insert(2)
print(q)

q.insert(3)
print(q)

q.insert(1)
print(q)

q = minHeap([3,2,1,0,-1])
print(q)
q.insert(5)
print(q)

q.insert(7)
print(q)

q.insert(4)
print(q)

mval = q.remove()
print(mval,q)