class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            curr = temperatures[i]
            future_temperatures = temperatures[i+1:]
            day = 0
            for j in range(len(future_temperatures)):
                day += 1
                if (curr >= future_temperatures[j] and 
                    j == len(future_temperatures) - 1):
                    day = 0
                elif curr > future_temperatures[j]:
                    continue
                elif curr < future_temperatures[j]:
                    break
            res.append(day)
        return res