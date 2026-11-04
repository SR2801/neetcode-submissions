class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        lcp = [None for i in range(201)]
        for _str in strs:
            for i in range(len(_str)+1):
                if i == len(_str):
                    lcp[i] = "$"
                    break
                if lcp[i] == None:
                    lcp[i] = _str[i]
                elif lcp[i] != _str[i]:
                    lcp[i] = ''
                    break

        for l in lcp:
            if l in ['', None, "$"]:
                break
            res += l
        return res



