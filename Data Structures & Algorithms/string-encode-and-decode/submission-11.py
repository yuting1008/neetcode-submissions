class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        count = 0
        length_s = len(s)
        while count < length_s:
            idx = s.index("#")
            length = int(s[:idx])

            if length == 0:
                res.append("")
                count += 2
                
            else:
                decoded = s[idx + 1:idx + 1 + length]
                res.append(decoded)
                count += len(str(length)) + 1 + length

            if count != length_s:
                s = s[idx + length + 1:]

        return res
            
        
