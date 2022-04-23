class MyHashMap:

    def __init__(self):
        # is SEEMS like only non-negative integers will be given as keys
        # and we know they won't go above 1e6. 
        # So if we can just set the buffer big enough, we don't have to worry about collisions.
        # and because it's just non-negative integers, we can just have the hashing function be equal to unity.
        # also instead of "none" we return "-1" for unallocated values (values also must be nonnegative otherwise)
        self.buffer = [-1]*(int(1e6) + 1) # list multiplication is a generalization of list addition (which is concatentation)
        
    def put(self, key: int, value: int) -> None:
        self.buffer[key] = value

    def get(self, key: int) -> int:
        return self.buffer[key]

    def remove(self, key: int) -> None:
        self.buffer[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

## better solution which uses less memory and runs faster (presumably due to less init overhead)
class Node:
    
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next # ooo reserved for low-level traversal of an iterator, bad form!
    

class MyHashMap_superiorSolution:

    def __init__(self):        
        self.data = [Node() for _ in range(1000)]
    
    def getHead(self, key):
        return self.data[key % len(self.data)] # hash function, classic modulo operation (could just be hardcoded as 1000, although I guess the python interpreter is smart enough to optimize that for you?)
                

    def put(self, key: int, value: int) -> None:
        
        head = self.getHead(key)
        while head.next: # loop to handle collisions 
            
            if head.next.key == key:
                head.next.val = value
                return
            head = head.next
        
        head.next = Node(key, value)
        

    def get(self, key: int) -> int:
        
        head = self.getHead(key)
        while head.next: # loop to handle collisions
            if head.next.key == key:
                return head.next.val
            head = head.next
        
        return -1
        

    def remove(self, key: int) -> None:
        
        
        head = self.getHead(key)
        while head.next: # loop to handle collisions
            if head.next.key == key:
                head.next = head.next.next
                return
            head = head.next