class HashTable:
    
    def __init__(self, capacity: int):
        self.data = {}
        self.size = 0
        self.capacity = capacity


    def insert(self, key: int, value: int) -> None:
        if key not in self.data:
            self.size += 1
            if self.size >= (self.capacity // 2):
                self.resize()

        self.data[key] = value

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        return self.data[key]


    def remove(self, key: int) -> bool:
        if key not in self.data:
            return False
        del self.data[key]
        self.size -= 1
        return True

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
