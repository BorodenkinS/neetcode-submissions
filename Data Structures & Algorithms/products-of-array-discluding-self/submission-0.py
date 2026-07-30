class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1]
        suffix = [1]

        for i in range(1, n):
            prefix.append(prefix[i-1] * nums[i-1])
            suffix.append(suffix[i-1] * nums[-i])
        
        result = []

        for i in range(n):
            result.append(prefix[i] * suffix[n-1-i])

        return result