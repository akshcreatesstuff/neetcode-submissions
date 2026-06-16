class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ""
        res = []
        for s_ in strs:
            res.append(str(len(s_)))
            res.append("#")
            res.append(s_)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
