from numpy import random

list1 = []
list2 = []

N = 20000

for i in range(N):
	r = random.randint(0,2)
	if r == 0:
		list1.append(i)
	else:
		list2.append(i)

print(list1[:1000])
print(list2[:1000])