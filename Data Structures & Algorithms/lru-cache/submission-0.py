class LRUCache:

    def __init__(self, capacity: int):
        self.data = {}
        self.q = []
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1

        qidx = self.q.index(key)
        it = self.q.pop(qidx)
        self.q.append(it)
        return self.data[key]        

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.get(key)
        else:
            if len(self.q) >= self.capacity:
                self.data.pop(self.q[0])
                self.q = self.q[1:]

            self.q.append(key)
        self.data[key] = value