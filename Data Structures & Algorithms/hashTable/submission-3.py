class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = [None]*capacity

    def insert(self, key: int, value: int) -> None:
        index = key % self.getCapacity()
        while True:
            if self.map[index] is None:
                self.map[index] = Pair(key, value)
                self.size += 1
                if self.getSize() >= self.getCapacity() // 2:
                    self.resize()
                return
            elif self.map[index].key == key:
                self.map[index].val = value
                return
            else:
                index += 1
                index = index % self.getCapacity()
    
    def get(self, key: int) -> int:
        index = key % self.getCapacity()
        while self.map[index] is not None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.getCapacity()
        return -1

    def remove(self, key: int) -> bool:
        index = key % self.getCapacity()
        while self.map[index] is not None:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return True
            index += 1
            index = index % self.getCapacity()
        return False
        
    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.size = 0
        self.capacity *= 2
        newMap = [None]*self.getCapacity()
        oldMap = self.map
        self.map = newMap
        for pair in oldMap:
            if pair is not None:
                self.insert(pair.key, pair.val)

