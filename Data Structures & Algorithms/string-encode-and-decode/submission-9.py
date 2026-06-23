class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            length = str(len(s))
            output += length + "#" + s
        return output

    def decode(self, s: str) -> List[str]:
        start_idx = 0
        output = []
        while start_idx < len(s):
            slash_idx = s.find("#", start_idx)
            length = int(s[start_idx:slash_idx])
            string = s[slash_idx+1:slash_idx+1+length]
            output.append(string)
            start_idx = slash_idx + 1 + length
        return output

