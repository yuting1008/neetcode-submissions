class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0  # 使用指標 i 來追蹤目前處理到編碼字串的哪個位置
        
        while i < len(s):
            # 1. 尋找從目前位置 i 開始的第一個 '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # 2. 提取長度（i 到 j 之間就是數字）
            length = int(s[i:j])
            
            # 3. 根據長度切出真正的字串內容
            # 字串起點在 j + 1，終點在 j + 1 + length
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # 4. 將指標 i 移動到下一個字串長度資訊的起點
            i = end

        return res