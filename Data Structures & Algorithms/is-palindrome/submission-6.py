class Solution:
    def isPalindrome(self, s: str) -> bool:
        symbols = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s = s.lower()

        t = ''

        for ch in s:
            if ch in symbols:
                t += ch

        left = 0
        right = len(t) - 1
        print(t)

        while left <= right:
            #if (s[left] in symbols) and (s[right] in symbols):
            if t[left] != t[right]:
                return False
            else:
                left += 1
                right -= 1
            
            '''if left < len(s) and s[left] not in symbols:
                left += 1
            if right >= 0 and s[right] not in symbols:
                right -= 1'''

        return True
        