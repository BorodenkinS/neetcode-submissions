class Solution:
    # working result
    def encode(self, strs: List[str]) -> str:
        result = ''
        
        for s in strs:
            result += str(len(s)) + '#' + s

        return result

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        
        while i < len(s):
            j = 0
            while s[i+j] != '#':
                j += 1

            counter = int(s[i:i+j])

            result.append(s[i+j+1:i+j+counter+1])
            i += j + counter + 1

        return result