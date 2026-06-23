class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        output  = []
        for num in nums:
            product = 1
            for n in count:
                if n != num:
                    product = product * (n ** count[n])
                else:
                    product = product * (n ** (count[n] - 1))
            output.append(product)
        return output