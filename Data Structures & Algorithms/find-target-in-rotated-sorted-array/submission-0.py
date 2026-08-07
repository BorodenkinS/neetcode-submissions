class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1

        while left < right:
            mid = (right + left) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        min_pos = left

        left = 0
        right = min_pos

        while left <= right:
            mid = left + (right - left) // 2

            if target > nums[mid]:
                left = mid + 1 
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid

        left = min_pos
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if target > nums[mid]:
                left = mid + 1 
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid


        return -1
            