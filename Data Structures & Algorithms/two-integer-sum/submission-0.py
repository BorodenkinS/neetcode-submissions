class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = dict()

        for i in range(len(nums)):
            if nums[i] in difference.keys():
                return sorted([i, difference[nums[i]]])
            else:
                difference.update({target - nums[i]: i})