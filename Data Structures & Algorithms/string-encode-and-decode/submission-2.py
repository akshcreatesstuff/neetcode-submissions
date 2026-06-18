class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ""
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        n = len(s)
        res = []
        i = 0
        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j+ 1
            j = i+ length
            res.append(s[i:j])
            i = j
        return res
