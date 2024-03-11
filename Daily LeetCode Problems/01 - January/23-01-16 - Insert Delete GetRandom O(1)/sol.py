import random 

class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.arrayList = []

    def insert(self, val: int) -> bool:
        self.hashmap[val] = len(self.hashmap)
        self.arrayList.append(val)
        return True 
    
    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        
        lastElement, idx = self.arrayList[-1], self.dict[val]
        self.arrayList[idx], self.dict[lastElement] = lastElement, idx 
        self.arrayList.pop()
        del self.dict[val]
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()