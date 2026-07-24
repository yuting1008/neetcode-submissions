class TimeMap:

    def __init__(self):
        self.mood = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mood[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.mood[key]
        l, r = 0, len(pairs) - 1
        timestamp_prev = 0
        res = ""
        while l <= r:
            m = l + ((r - l) // 2)
            if timestamp == pairs[m][0]:
                return pairs[m][1]
            if timestamp > pairs[r][0]:
                return pairs[r][1]
            if timestamp < pairs[m][0]:
                r = m - 1
            elif timestamp > pairs[m][0]:
                l = m + 1
                timestamp_prev = max(timestamp_prev, pairs[m][0])
                if timestamp_prev == pairs[m][0]:
                    res = pairs[m][1]
        return res
