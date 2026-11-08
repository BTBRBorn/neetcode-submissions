class DynamicArray:
    
    def __init__(self, capacity: int):
        self.data = [0]*capacity
        self.length = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.data[self.length] = n
        self.length += 1

    def popback(self) -> int:
        val = self.get(self.length-1)
        self.length -= 1
        return val

    def resize(self) -> None:
        new_arr = [0]*self.capacity*2
        for i in range(self.length):
            new_arr[i] = self.data[i]
        self.capacity *= 2
        self.data = new_arr

    def getSize(self) -> int:
        return self.length
        
    def getCapacity(self) -> int:
        return self.capacity
