class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        data = self.data[key]
        if timestamp < data[0][0]:
            return ""
        if timestamp >= data[-1][0]:
            return data[-1][1]

        l = 0
        r = len(data) - 1

        while l < r:
            m = l + (r-l+1) // 2

            if data[m][0] <= timestamp:
                l = m
            else:
                r = m - 1

        return data[l][1]
        
