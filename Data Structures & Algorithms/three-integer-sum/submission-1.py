class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        result = []
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i+1
            right = n-1

            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    result.append([nums[i], nums[left], nums[right]])

                    while nums[right] == nums[right-1] and right > left:
                        right -= 1
                    while nums[left] == nums[left+1] and left < right:
                        left += 1

                    left += 1
                    right -= 1

                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1

        return result