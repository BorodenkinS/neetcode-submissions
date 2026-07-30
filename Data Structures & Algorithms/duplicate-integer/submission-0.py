class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = []

        for i in nums:
            if i in duplicate:
                return True
            else:
                duplicate.append(i)
        
        return False