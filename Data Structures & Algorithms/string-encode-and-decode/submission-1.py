class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ''
        for i in strs:
            text = i+'^|'
            code += text
        print(code)
        #code = ''.join(strs,"^|^") 
        return code

    def decode(self, s: str) -> List[str]:
        strs = []
        word = ''
        prev = ''
        for i in s:
            if i == '|' and prev == '^':
                strs.append(word[:-1:])
                word = ''
            else:
                word += i
                prev = i
        return strs
