class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += s + "我"
        return output

    def decode(self, s: str) -> List[str]:
        strs = s.split("我")
        return strs[0:len(strs)-1]

