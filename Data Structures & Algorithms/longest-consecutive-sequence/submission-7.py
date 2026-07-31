class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums_set = set(nums)
        seqs = dict()
        max_len = 1

        for num in nums_set:
            if num - 1 not in nums_set:
                seqs.update({num: 1})
                counter = num
                while counter + 1 in nums_set:
                    counter += 1
                    seqs[num] += 1
                if seqs[num] > max_len:
                    max_len = seqs[num]
        
        return max_len
