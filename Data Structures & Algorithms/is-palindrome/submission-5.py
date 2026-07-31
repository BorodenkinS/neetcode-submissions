class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        symbols = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s = s.lower()

        while left <= right < len(s):
            if (s[left] in symbols) and (s[right] in symbols):
                if s[left] != s[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            
            if left < len(s) and s[left] not in symbols:
                left += 1
            if right >= 0 and s[right] not in symbols:
                right -= 1

        return True
        