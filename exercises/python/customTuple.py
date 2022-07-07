from functools import total_ordering

@total_ordering
class customTuple(tuple):
    def __init__(self,thisTuple:tuple = ()):
        super().__init__()
        self = thisTuple
    def __eq__(self,other): # no recursive type hints :( :( :(
        if len(self)==0 or len(other) == 0:
            return False
        else:
            return self[0] == other[0]

    def __lt__(self,other):
        if len(self)==0 or len(other)==0:
            return False
        else:
            return self[0] < other[0]

    def __gt__(self,other):
        if len(self)==0 or len(other)==0:
            return False
        else:
            return self[0] > other[0]

t1 = (1,2)
t2 = (1,3)

ct1 = customTuple(t1)
ct2 = customTuple(t2)

print(t1 < t2)
print(ct1 < ct2)