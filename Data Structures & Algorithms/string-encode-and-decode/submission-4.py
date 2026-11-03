class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for str in strs:
            code += f'{len(str)}#{str}'
        print(code)
        return code
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            n = ""
            while i < len(s) and s[i] != "#":
                n += s[i]
                i += 1
            strs.append(s[i+1:i+int(n)+1])
            # print(s[i:i+int(n) + 1]) 
            # print(i, (i+int(n) + 1), n, s[(i+int(n) + 1)%len(s)])
            i += int(n) + 1
            # print(strs)
        return strs

