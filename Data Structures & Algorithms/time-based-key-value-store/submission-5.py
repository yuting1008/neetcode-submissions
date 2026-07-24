class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store.get(key, [])
        l, r = 0, len(pairs) - 1
        res = ""
        while l <= r:
            m = l + ((r - l) // 2)
            if timestamp < pairs[m][0]:
                r = m - 1
            elif timestamp >= pairs[m][0]:
                l = m + 1
                res = pairs[m][1]
        return res
