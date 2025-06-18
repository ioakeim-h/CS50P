

class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return self.size * "🍪"        

    def deposit(self, n):
        if self.capacity <= self.size:
            raise ValueError(f"Can deposit up to {self.capacity - self.size} cookies!")
        self.size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError(f"Can withdraw {self.size} cookies!")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("capacity must be a non-negative integer")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not isinstance(size, int) or size < 0:
            raise ValueError("Provide your cookies in a non-negative integer form!")
        self._size = size

