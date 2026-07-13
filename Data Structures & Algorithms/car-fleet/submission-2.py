class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        # [4,1,0,7] & [2,2,1,1] -> [(4,2),(1,2),(0,1),(7,1)]
        # [10,8,0,5,3] & [2,4,1,1,3] -> [(10,2),(8,4),(0,1),(5,1),(3,3)]

        sortedPair = sorted(pair)
        # [(4,2),(1,2),(0,1),(7,1)] -> [(0,1),(1,2),(4,2),(7,1)]
        # [(10,2),(8,4),(0,1),(5,1),(3,3)] -> [(0,1),(3,3),(5,1),(8,4),(10,2)]

        time = []
        for pair in sortedPair:
            t = (target - pair[0]) / pair[1]
            time.append(t)
        # [10,4.5,3,3]
        # [(0,1),(3,3),(5,1),(8,4),(10,2)]
        # [12,3,7,1,1]
        
        stack = [time[-1]] #[3] [1]
        for i in range(len(time) - 2, -1, -1):
            if time[i] > stack[-1]:
                stack.append(time[i])
        return len(stack) # [10,4.5,3] [12,7,1]
            